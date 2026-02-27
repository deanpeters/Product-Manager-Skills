"""PM Skills Playground — Streamlit app for browsing and test-driving PM skills.

Usage:
    cd /path/to/product-manager-skills
    pip install -r app/requirements.txt
    streamlit run app/main.py
"""

import os
import re
from pathlib import Path

import anthropic
import streamlit as st
import yaml
from dotenv import load_dotenv
try:
    from openai import AuthenticationError as OpenAIAuthenticationError
    from openai import OpenAI
except ImportError:  # pragma: no cover - optional dependency for multi-provider mode
    OpenAI = None

    class OpenAIAuthenticationError(Exception):
        pass

load_dotenv(Path(__file__).parent / ".env")

# ─── Constants ────────────────────────────────────────────────────────────────

SKILLS_DIR = Path(__file__).parent.parent / "skills"
PROVIDERS = {
    "anthropic": {
        "label": "Anthropic",
        "key_env": "ANTHROPIC_API_KEY",
        "default_model_env": "ANTHROPIC_MODEL",
        "models_env": "ANTHROPIC_MODELS",
        "default_models": ["claude-haiku-4-5-20251001", "claude-sonnet-4-6"],
        "model_help": {
            "claude-haiku-4-5-20251001": "Fast (cheaper; may miss depth in long workflows)",
            "claude-sonnet-4-6": "Capable (best for full workflow quality)",
        },
    },
}
if OpenAI is not None:
    PROVIDERS["openai"] = {
        "label": "OpenAI",
        "key_env": "OPENAI_API_KEY",
        "default_model_env": "OPENAI_MODEL",
        "models_env": "OPENAI_MODELS",
        "default_models": ["gpt-4o-mini", "gpt-4o"],
        "model_help": {
            "gpt-4o-mini": "Fast (cheaper; may miss depth in long workflows)",
            "gpt-4o": "Capable (best for full workflow quality)",
        },
    }
    PROVIDERS["ollama"] = {
        "label": "Ollama",
        "key_env": None,
        "default_model_env": "OLLAMA_MODEL",
        "models_env": "OLLAMA_MODELS",
        "default_models": ["qwen2.5:latest", "llama3.2:latest"],
        "model_help": {
            "qwen2.5:latest": "Fast (local; may miss depth in long workflows)",
            "llama3.2:latest": "Capable (local; best for full workflow quality)",
        },
    }

THEMES = {
    "career-leadership": {
        "label": "Career & Leadership",
        "icon": "🚀",
        "description": "PM→Director→VP/CPO transitions, readiness advisors, executive onboarding",
    },
    "discovery-research": {
        "label": "Discovery & Research",
        "icon": "🔍",
        "description": "Customer interviews, opportunity mapping, problem framing, jobs-to-be-done",
    },
    "strategy-positioning": {
        "label": "Strategy & Positioning",
        "icon": "🎯",
        "description": "Positioning, roadmaps, product strategy, market analysis",
    },
    "pm-artifacts": {
        "label": "Writing PM Artifacts",
        "icon": "📝",
        "description": "User stories, PRDs, epics, press releases, personas, storyboards",
    },
    "finance-metrics": {
        "label": "Finance & Metrics",
        "icon": "📊",
        "description": "SaaS metrics, unit economics, pricing, business health",
    },
    "ai-agents": {
        "label": "AI & Agents",
        "icon": "🤖",
        "description": "AI-shaped thinking, agent orchestration, context engineering, PoL probes",
    },
    "workshops-facilitation": {
        "label": "Workshops & Facilitation",
        "icon": "🎭",
        "description": "Journey mapping, facilitation, canvas tools, story mapping workshops",
    },
}

TYPE_BADGES = {
    "component": ("🧱", "Component"),
    "interactive": ("🔄", "Interactive"),
    "workflow": ("🎭", "Workflow"),
}

# ─── Skill Loading ─────────────────────────────────────────────────────────────

@st.cache_data
def load_skills():
    """Parse all SKILL.md files. Returns list of skill dicts."""
    skills = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            continue

        body = parts[2].strip()

        # Extract ## sections into a dict
        sections: dict[str, str] = {}
        current: str | None = None
        buf: list[str] = []
        for line in body.split("\n"):
            if line.startswith("## "):
                if current is not None:
                    sections[current] = "\n".join(buf).strip()
                current = line[3:].strip()
                buf = []
            else:
                buf.append(line)
        if current is not None:
            sections[current] = "\n".join(buf).strip()

        # First non-empty paragraph of Purpose as a short excerpt
        purpose_text = sections.get("Purpose", "")
        purpose_short = next(
            (p.strip() for p in purpose_text.split("\n\n") if p.strip()), ""
        )

        skills.append(
            {
                "name": fm.get("name", skill_dir.name),
                "description": fm.get("description", ""),
                "type": fm.get("type", "component"),
                "theme": fm.get("theme"),
                "best_for": fm.get("best_for") or [],
                "scenarios": fm.get("scenarios") or [],
                "estimated_time": fm.get("estimated_time"),
                "body": body,
                "sections": sections,
                "purpose_short": purpose_short,
                "has_examples": (skill_dir / "examples").exists(),
            }
        )
    return skills


# ─── API ──────────────────────────────────────────────────────────────────────

def _csv_models(raw: str) -> list[str]:
    values = [m.strip() for m in raw.split(",") if m.strip()]
    return list(dict.fromkeys(values))


def provider_key(provider: str) -> str:
    env_key = PROVIDERS[provider]["key_env"]
    if not env_key:
        # Ollama can run without auth; OpenAI-compatible clients still require a placeholder key.
        return os.getenv("OLLAMA_API_KEY", "ollama").strip()
    return os.getenv(env_key, "").strip()


def provider_enabled(provider: str) -> bool:
    if provider != "ollama":
        return bool(provider_key(provider))

    enabled_flag = os.getenv("OLLAMA_ENABLED", "").strip().lower()
    has_base = bool(os.getenv("OLLAMA_BASE_URL", "").strip())
    return enabled_flag in {"1", "true", "yes", "on"} or has_base


def ollama_base_url() -> str:
    base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").strip().rstrip("/")
    if base.endswith("/v1"):
        return base
    return f"{base}/v1"


def available_providers() -> list[str]:
    return [p for p in PROVIDERS if provider_enabled(p)]


def provider_default_model(provider: str) -> str:
    env_name = PROVIDERS[provider]["default_model_env"]
    return os.getenv(env_name, "").strip() or PROVIDERS[provider]["default_models"][0]


def provider_model_options(provider: str) -> list[str]:
    env_models_name = PROVIDERS[provider]["models_env"]
    env_models_raw = os.getenv(env_models_name, "")
    models = list(PROVIDERS[provider]["default_models"])
    if env_models_raw:
        models.extend(_csv_models(env_models_raw))
    default_model = provider_default_model(provider)
    if default_model not in models:
        models.insert(0, default_model)
    return list(dict.fromkeys(models))


def provider_model_help(provider: str) -> dict[str, str]:
    return PROVIDERS[provider]["model_help"]


def is_auth_error(error: Exception) -> bool:
    return isinstance(error, (anthropic.AuthenticationError, OpenAIAuthenticationError))


def call_model(provider: str, api_key: str, model: str, system: str, messages: list) -> str:
    if provider == "anthropic":
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=2048,
            system=system,
            messages=messages,
        )
        return response.content[0].text

    if provider == "openai":
        if OpenAI is None:
            raise RuntimeError("openai package is not installed. Run: pip install -r app/requirements.txt")
        client = OpenAI(api_key=api_key)
        openai_messages = [{"role": "system", "content": system}] + messages
        response = client.chat.completions.create(
            model=model,
            messages=openai_messages,
            max_tokens=2048,
        )
        return response.choices[0].message.content or ""

    if provider == "ollama":
        if OpenAI is None:
            raise RuntimeError("openai package is not installed. Run: pip install -r app/requirements.txt")
        client = OpenAI(api_key=api_key, base_url=ollama_base_url())
        openai_messages = [{"role": "system", "content": system}] + messages
        response = client.chat.completions.create(
            model=model,
            messages=openai_messages,
            max_tokens=2048,
        )
        return response.choices[0].message.content or ""

    raise ValueError(f"Unsupported provider: {provider}")


def build_system_prompt(skill: dict) -> str:
    extra = ""
    if skill["type"] == "interactive":
        extra = (
            "\n\nFacilitation rules:\n"
            "- Ask ONE question at a time with numbered options as the skill specifies.\n"
            "- Show progress labels (e.g., Q1/3) so the user knows where they are.\n"
            "- Be conversational but stay true to the skill's structure exactly.\n"
            "- Do not improvise beyond what the skill defines."
        )
    return f"You are running the following PM skill for the user. Follow it exactly as written.\n\n{skill['body']}{extra}"


# ─── State Helpers ─────────────────────────────────────────────────────────────

def nav(view: str, **kwargs):
    """Navigate to a new view, resetting session state cleanly."""
    st.session_state.view = view
    for k, v in kwargs.items():
        st.session_state[k] = v
    if view != "session":
        st.session_state.messages = []
        st.session_state.phase = 0
        st.session_state.workflow_outputs = {}
        st.session_state.scenario = st.session_state.get("scenario_input", "")
    elif "scenario" in kwargs or "skill" in kwargs:
        # Fresh session starts should not carry prior workflow/chat artifacts.
        st.session_state.messages = []
        st.session_state.phase = 0
        st.session_state.workflow_outputs = {}
    st.rerun()


def detect_progress(messages: list) -> tuple[int | None, int | None]:
    """Parse Q1/3-style progress labels from the most recent assistant message."""
    for msg in reversed(messages):
        if msg["role"] == "assistant":
            match = re.search(
                r"\b(?:Context\s+)?Q(\d+)/(\d+)\b|\bStep\s+(\d+)\s+of\s+(\d+)\b",
                msg["content"],
                re.IGNORECASE,
            )
            if match:
                groups = [g for g in match.groups() if g is not None]
                if len(groups) >= 2:
                    return int(groups[0]), int(groups[1])
    return None, None


def extract_workflow_phases(app_text: str) -> list[dict[str, str]]:
    """Extract phase headings and their bodies from a workflow Application section."""
    phase_re = re.compile(r"(?m)^#{2,3}\s+(Phase\s+\d+[^\n#]*)\s*$")
    matches = list(phase_re.finditer(app_text))
    if not matches:
        return [{"name": "Full workflow", "body": app_text.strip()}]

    phases: list[dict[str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(app_text)
        phases.append(
            {
                "name": match.group(1).strip(),
                "body": app_text[start:end].strip(),
            }
        )
    return phases


def build_phase_prompt(
    scenario: str, phase_name: str, phase_body: str, phase_index: int, total_phases: int
) -> str:
    return (
        f"Scenario:\n{scenario or 'No additional scenario provided.'}\n\n"
        f"You are running workflow phase {phase_index}/{total_phases}: {phase_name}\n\n"
        f"Phase definition from the skill:\n{phase_body}\n\n"
        "Do this now:\n"
        "1) Complete this phase only (do not skip).\n"
        "2) Produce concrete draft outputs/artifacts for this phase.\n"
        "3) End with:\n"
        "   - Decisions made\n"
        "   - Open questions\n"
        "   - What is needed for the next phase\n"
    )


# ─── Sidebar ──────────────────────────────────────────────────────────────────

def render_sidebar(skill: dict | None = None):
    with st.sidebar:
        st.markdown("## 🧰 PM Skills Playground (beta)")

        providers = available_providers()
        if providers:
            labels = ", ".join(PROVIDERS[p]["label"] for p in providers)
            st.success(f"✅ API providers ready: {labels}")
        else:
            st.error("⚠️ No API providers configured")

        with st.expander("ℹ API Setup Instructions", expanded=not providers):
            st.markdown(
                "Configure one or more providers via environment variables (or `app/.env`), then restart:"
            )
            st.code(
                "ANTHROPIC_API_KEY=sk-ant-...\n"
                "OPENAI_API_KEY=sk-...\n"
                "OLLAMA_ENABLED=1\n"
                "OLLAMA_BASE_URL=http://localhost:11434\n"
                "# Optional defaults\n"
                "ANTHROPIC_MODEL=claude-sonnet-4-6\n"
                "OPENAI_MODEL=gpt-4o-mini\n"
                "OLLAMA_MODEL=qwen2.5:latest\n"
                "# Optional model lists (comma-separated)\n"
                "ANTHROPIC_MODELS=claude-haiku-4-5-20251001,claude-sonnet-4-6\n"
                "OPENAI_MODELS=gpt-4o-mini,gpt-4o\n"
                "OLLAMA_MODELS=qwen2.5:latest,llama3.2:latest",
                language="bash",
            )

        if providers:
            selected_provider = st.session_state.get("selected_provider", providers[0])
            if selected_provider not in providers:
                selected_provider = providers[0]
                st.session_state["selected_provider"] = selected_provider

            st.selectbox(
                "API provider",
                options=providers,
                index=providers.index(selected_provider),
                format_func=lambda p: PROVIDERS[p]["label"],
                key="selected_provider",
                help="Switch between available providers loaded from environment keys.",
            )

            provider = st.session_state.get("selected_provider", providers[0])
            model_options = provider_model_options(provider)
            default_model = provider_default_model(provider)
            model_help = provider_model_help(provider)

            selected_model = st.session_state.get("selected_model", default_model)
            if selected_model not in model_options:
                selected_model = default_model
                st.session_state["selected_model"] = selected_model

            st.selectbox(
                "Model",
                options=model_options,
                index=model_options.index(selected_model),
                format_func=lambda m: f"{m} — {model_help.get(m, 'Model')}",
                key="selected_model",
                help="Pick a cheaper model for routine testing, and premium models for final checks.",
            )

        st.divider()

        # During a session: show bail options prominently
        if skill and st.session_state.get("view") == "session":
            icon, type_label = TYPE_BADGES.get(skill["type"], ("", "Skill"))
            st.markdown(f"**{icon} {skill['name']}**")
            st.caption(f"{type_label} skill")
            if skill.get("estimated_time"):
                st.caption(f"⏱ {skill['estimated_time']}")
            st.divider()
            st.caption("Navigation")
            if st.button("↩ Start over", use_container_width=True):
                nav("skill", skill=skill, theme=st.session_state.get("theme"))
            if st.button("← Different skill", use_container_width=True):
                theme = st.session_state.get("theme")
                if theme:
                    nav("theme", theme=theme)
                else:
                    nav("home")
            if st.button("🏠 Home", use_container_width=True):
                nav("home")
        else:
            if st.button("🏠 Home", use_container_width=True):
                nav("home")

        st.divider()
        st.caption("Streamlit (beta) · New feature in flight")
        st.caption(
            "[Feedback via GitHub ↗](https://github.com/deanpeters/Product-Manager-Skills/issues) · "
            "[Connect on LinkedIn ↗](https://linkedin.com/in/deanpeters)"
        )
        st.caption("46 PM skills · CC BY-NC-SA 4.0")
        st.caption("[GitHub ↗](https://github.com/deanpeters/product-manager-skills)")


# ─── Screen: Home ─────────────────────────────────────────────────────────────

def render_home(skills: list):
    st.title("PM Skills Playground (beta)")
    st.markdown(
        "Streamlit (beta): a new feature in flight. Browse 46 battle-tested PM frameworks, pick a theme, and test-drive skills. "
        "Feedback welcome via [GitHub issues](https://github.com/deanpeters/Product-Manager-Skills/issues) "
        "or [LinkedIn](https://linkedin.com/in/deanpeters)."
    )
    st.divider()

    # Group skills by theme
    theme_skills: dict[str, list] = {}
    for s in skills:
        key = s.get("theme") or "_unthemed"
        theme_skills.setdefault(key, []).append(s)

    cols = st.columns(3)
    for i, (slug, meta) in enumerate(THEMES.items()):
        skill_list = theme_skills.get(slug, [])
        type_counts: dict[str, int] = {}
        for s in skill_list:
            type_counts[s["type"]] = type_counts.get(s["type"], 0) + 1
        count_str = "  ·  ".join(
            f"{v} {k}" for k, v in sorted(type_counts.items())
        )

        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"### {meta['icon']} {meta['label']}")
                st.caption(meta["description"])
                st.caption(count_str or "Skills coming soon")
                if skill_list:
                    if st.button("Browse →", key=f"theme_{slug}", use_container_width=True):
                        nav("theme", theme=slug)

    # Unthemed fallback
    unthemed = theme_skills.get("_unthemed", [])
    if unthemed:
        st.divider()
        with st.expander(f"All other skills ({len(unthemed)} without theme tag)"):
            for s in sorted(unthemed, key=lambda x: x["name"]):
                icon, label = TYPE_BADGES.get(s["type"], ("", "Skill"))
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"**{s['name']}** · {icon} {label}")
                    desc = s["description"]
                    st.caption(desc[:120] + "…" if len(desc) > 120 else desc)
                with c2:
                    if st.button("Try →", key=f"unthemed_{s['name']}"):
                        nav("skill", skill=s, theme=None)


# ─── Screen: Theme ────────────────────────────────────────────────────────────

def render_theme(skills: list, theme_slug: str):
    meta = THEMES.get(theme_slug, {"label": theme_slug, "icon": "📦", "description": ""})

    if st.button("← Back to themes"):
        nav("home")

    st.title(f"{meta['icon']} {meta['label']}")
    st.markdown(meta["description"])
    st.divider()

    theme_skills = [s for s in skills if s.get("theme") == theme_slug]

    if not theme_skills:
        st.info("No skills tagged with this theme yet — check back soon.")
        return

    for s in sorted(theme_skills, key=lambda x: x["name"]):
        icon, type_label = TYPE_BADGES.get(s["type"], ("", "Skill"))
        with st.container(border=True):
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"**{icon} {s['name']}**")
                desc = s["description"]
                st.caption(desc[:150] + "…" if len(desc) > 150 else desc)

                if s.get("best_for"):
                    for bf in s["best_for"][:3]:
                        st.markdown(f"- {bf}")
                elif s.get("purpose_short"):
                    st.caption(s["purpose_short"][:220])

                if s.get("estimated_time"):
                    st.caption(f"⏱ {s['estimated_time']}")
            with c2:
                st.caption(f"{type_label} skill")
                if st.button("Try it →", key=f"skill_{s['name']}", use_container_width=True):
                    nav("skill", skill=s, theme=theme_slug)


# ─── Screen: Skill Detail ─────────────────────────────────────────────────────

def render_skill_detail(skill: dict, theme_slug: str | None):
    if skill is None:
        st.error("No skill selected.")
        nav("home")
        return

    meta = THEMES.get(theme_slug or "", {"label": "All Skills"})
    icon, type_label = TYPE_BADGES.get(skill["type"], ("", "Skill"))

    # Breadcrumb nav
    bc = st.columns([1, 1, 6])
    with bc[0]:
        if st.button("🏠 Home"):
            nav("home")
    with bc[1]:
        if theme_slug and st.button(f"← {meta['label']}"):
            nav("theme", theme=theme_slug)

    st.title(skill["name"])
    st.caption(f"{icon} {type_label} skill{'  ·  ⏱ ' + skill['estimated_time'] if skill.get('estimated_time') else ''}")
    st.divider()

    # Purpose
    if skill["sections"].get("Purpose"):
        st.markdown(skill["sections"]["Purpose"])

    # Best for
    if skill.get("best_for"):
        st.markdown("**Best for:**")
        for bf in skill["best_for"]:
            st.markdown(f"- {bf}")

    st.divider()

    # Pre-flight for interactive / workflow skills
    if skill["type"] == "interactive":
        st.info(
            "💬 **Guided conversation**  \n"
            "This skill asks you questions one at a time and gives you personalised "
            "recommendations based on your answers.  \n\n"
            + (f"Estimated time: **{skill['estimated_time']}**  \n\n" if skill.get("estimated_time") else "")
            + "You can bail at any time — use **Start over** or **← Different skill** in the sidebar."
        )
    elif skill["type"] == "workflow":
        st.info(
            "🔄 **Multi-phase workflow**  \n"
            "This skill walks you through a structured process in phases. "
            "Work through them in sequence, or jump to the phase you need."
        )

    # Scenario input
    st.markdown("### Your scenario")

    # Pre-built scenario chips
    if skill.get("scenarios"):
        st.caption("Quick-start with a pre-built scenario, or write your own below:")
        for i, scenario in enumerate(skill["scenarios"][:4]):
            label = f'"{scenario[:70]}{"…" if len(scenario) > 70 else ""}"'
            if st.button(label, key=f"chip_{i}"):
                nav("session", skill=skill, theme=theme_slug, scenario=scenario)

    scenario = st.text_area(
        "Your situation:",
        value=st.session_state.get("scenario_input", ""),
        placeholder=(
            "Describe your context — who you are, what you're working on, "
            "and what you're trying to figure out…"
        ),
        height=110,
        key="scenario_text_area",
    )

    btn_label = {
        "component": "Generate artifact →",
        "interactive": "Start guided session →",
        "workflow": "Start workflow →",
    }.get(skill["type"], "Run skill →")

    disabled = not scenario.strip()
    if st.button(btn_label, type="primary", disabled=disabled):
        nav("session", skill=skill, theme=theme_slug, scenario=scenario.strip())
    if disabled:
        st.caption("↑ Add your scenario above to continue")


# ─── Screen: Session ──────────────────────────────────────────────────────────

def render_session(skill: dict | None):
    if skill is None:
        st.error("No skill selected.")
        nav("home")
        return

    providers = available_providers()
    if not providers:
        st.warning(
            "⚠️ Configure at least one provider: "
            "`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `OLLAMA_ENABLED=1` with `OLLAMA_BASE_URL`."
        )
        return

    provider = st.session_state.get("selected_provider", providers[0])
    if provider not in providers:
        provider = providers[0]
        st.session_state["selected_provider"] = provider

    api_key = provider_key(provider)
    model_options = provider_model_options(provider)
    model = st.session_state.get("selected_model", provider_default_model(provider))
    if model not in model_options:
        model = provider_default_model(provider)
        st.session_state["selected_model"] = model

    system = build_system_prompt(skill)
    scenario = st.session_state.get("scenario", "")

    st.caption(f"Provider: **{PROVIDERS[provider]['label']}** · Model: **{model}**")

    if skill["type"] == "component":
        render_component_session(skill, provider, api_key, model, system, scenario)
    elif skill["type"] == "interactive":
        render_interactive_session(skill, provider, api_key, model, system, scenario)
    elif skill["type"] == "workflow":
        render_workflow_session(skill, provider, api_key, model, system, scenario)


def render_component_session(
    skill: dict, provider: str, api_key: str, model: str, system: str, scenario: str
):
    st.subheader(f"🧱 {skill['name']}")
    st.caption(f"Scenario: {scenario[:120]}{'…' if len(scenario) > 120 else ''}")
    st.divider()

    if not st.session_state.get("messages"):
        with st.spinner("Running skill…"):
            try:
                messages = [{"role": "user", "content": scenario}]
                response = call_model(provider, api_key, model, system, messages)
                st.session_state.messages = messages + [
                    {"role": "assistant", "content": response}
                ]
            except Exception as e:
                if is_auth_error(e):
                    st.error(f"❌ Invalid {PROVIDERS[provider]['label']} API key. Check your environment configuration.")
                    return
                st.error(f"API error: {e}")
                return

    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.markdown(msg["content"])

    st.divider()
    if st.button("↩ Try a different scenario", use_container_width=True):
        nav("skill", skill=skill, theme=st.session_state.get("theme"))


def render_interactive_session(
    skill: dict, provider: str, api_key: str, model: str, system: str, scenario: str
):
    # Progress bar
    messages = st.session_state.get("messages", [])
    current_step, total_steps = detect_progress(messages)
    if current_step and total_steps:
        st.progress(
            current_step / total_steps,
            text=f"Question {current_step} of {total_steps}",
        )
    elif messages:
        user_turns = sum(1 for m in messages if m["role"] == "user")
        st.caption(f"Turn {user_turns}")

    st.subheader(f"🔄 {skill['name']}")

    # Kick off with first message if fresh
    if not messages:
        initial = f"My situation: {scenario}" if scenario else "Let's start."
        with st.spinner("Starting session…"):
            try:
                msgs = [{"role": "user", "content": initial}]
                response = call_model(provider, api_key, model, system, msgs)
                st.session_state.messages = msgs + [
                    {"role": "assistant", "content": response}
                ]
                messages = st.session_state.messages
            except Exception as e:
                if is_auth_error(e):
                    st.error(f"❌ Invalid {PROVIDERS[provider]['label']} API key. Check your environment configuration.")
                    return
                st.error(f"API error: {e}")
                return

    # Render conversation history
    for msg in messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Your response… (type 'done' to finish)")
    if user_input:
        if user_input.strip().lower() in ("done", "exit", "quit", "bail", "stop"):
            st.info(
                "Session ended.  \n"
                "Use **↩ Start over** in the sidebar to try a different scenario, "
                "or **← Different skill** to explore another skill."
            )
        else:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    try:
                        response = call_model(
                            provider, api_key, model, system, st.session_state.messages
                        )
                        st.markdown(response)
                        st.session_state.messages.append(
                            {"role": "assistant", "content": response}
                        )
                    except Exception as e:
                        if is_auth_error(e):
                            st.error(f"❌ Invalid {PROVIDERS[provider]['label']} API key. Check your environment configuration.")
                            return
                        st.error(f"API error: {e}")
                        return
            st.rerun()


def render_workflow_session(
    skill: dict, provider: str, api_key: str, model: str, system: str, scenario: str
):
    # Detect phases from parsed section keys first (handles skills that use ## Phase N),
    # then fall back to heading extraction from Application text.
    phase_defs = [
        {"name": section_name, "body": section_body}
        for section_name, section_body in skill["sections"].items()
        if re.match(r"^Phase\s+\d+", section_name)
    ]
    if not phase_defs:
        app_text = skill["sections"].get("Application", "")
        phase_defs = extract_workflow_phases(app_text)
    phases = [p["name"] for p in phase_defs]
    workflow_outputs: dict[str, str] = st.session_state.get("workflow_outputs", {})

    st.subheader(f"🎭 {skill['name']}")

    current_phase = st.session_state.get("phase", 0)
    if current_phase >= len(phases):
        current_phase = 0
        st.session_state.phase = 0

    completed_count = sum(1 for phase_name in phases if workflow_outputs.get(phase_name))
    st.progress(
        completed_count / max(len(phases), 1),
        text=f"Workflow progress: {completed_count}/{len(phases)} phases generated",
    )

    st.info(
        "How this works: choose a phase and run it for concrete output, or run all phases automatically. "
        "Each phase result is saved and shown when you come back."
    )

    fast_model = PROVIDERS[provider]["default_models"][0]
    if model == fast_model and len(phases) >= 4:
        st.warning(
            f"Fast model selected (`{model}`). Complex workflows may be thin or skip detail. "
            "Use the capable profile for higher-quality phase outputs."
        )

    if len(phases) > 1:
        selected = st.radio(
            "Jump to phase:",
            phases,
            index=current_phase,
            horizontal=True,
        )
        new_phase = phases.index(selected)
        if new_phase != current_phase:
            st.session_state.phase = new_phase
            st.rerun()

    st.divider()
    current_def = phase_defs[current_phase]
    phase_name = current_def["name"]
    st.markdown(f"**{phase_name}**")

    if current_def["body"]:
        with st.expander("Phase brief from the skill"):
            st.markdown(current_def["body"])

    c1, c2, c3 = st.columns(3)
    with c1:
        run_phase = st.button("▶ Run this phase", type="primary", use_container_width=True)
    with c2:
        run_all = st.button("⚡ Run all phases", use_container_width=True)
    with c3:
        clear_all = st.button("🧹 Clear workflow outputs", use_container_width=True)

    if clear_all:
        st.session_state.workflow_outputs = {}
        st.session_state.phase = 0
        st.rerun()

    if run_phase:
        with st.spinner(f"Running {phase_name}…"):
            try:
                prompt = build_phase_prompt(
                    scenario, phase_name, current_def["body"], current_phase + 1, len(phases)
                )
                msgs = [{"role": "user", "content": prompt}]
                response = call_model(provider, api_key, model, system, msgs)
                workflow_outputs[phase_name] = response
                st.session_state.workflow_outputs = workflow_outputs
                st.rerun()
            except Exception as e:
                if is_auth_error(e):
                    st.error(f"❌ Invalid {PROVIDERS[provider]['label']} API key. Check your environment configuration.")
                    return
                st.error(f"API error: {e}")
                return

    if run_all:
        with st.spinner(f"Running all {len(phases)} phases…"):
            try:
                for idx, phase_def in enumerate(phase_defs, start=1):
                    prompt = build_phase_prompt(
                        scenario, phase_def["name"], phase_def["body"], idx, len(phases)
                    )
                    msgs = [{"role": "user", "content": prompt}]
                    response = call_model(provider, api_key, model, system, msgs)
                    workflow_outputs[phase_def["name"]] = response
                st.session_state.workflow_outputs = workflow_outputs
                st.session_state.phase = len(phases) - 1
                st.rerun()
            except Exception as e:
                if is_auth_error(e):
                    st.error(f"❌ Invalid {PROVIDERS[provider]['label']} API key. Check your environment configuration.")
                    return
                st.error(f"API error while running full workflow: {e}")
                return

    st.divider()
    if workflow_outputs.get(phase_name):
        st.markdown(workflow_outputs[phase_name])
    else:
        st.caption("No output yet for this phase. Click **Run this phase**.")

    st.divider()
    n1, n2, n3 = st.columns(3)
    with n1:
        if st.button("← Previous phase", disabled=current_phase == 0, use_container_width=True):
            st.session_state.phase = max(0, current_phase - 1)
            st.rerun()
    with n2:
        can_advance = bool(workflow_outputs.get(phase_name))
        if st.button(
            "Continue to next phase →",
            type="primary",
            disabled=(current_phase >= len(phases) - 1) or (not can_advance),
            use_container_width=True,
        ):
            st.session_state.phase = current_phase + 1
            st.rerun()
    with n3:
        if st.button("↩ Start from phase 1", use_container_width=True):
            st.session_state.phase = 0
            st.rerun()

    if current_phase == len(phases) - 1:
        if completed_count == len(phases):
            st.success("✅ All workflow phases have generated outputs.")
        else:
            st.warning(
                f"Last phase reached, but only {completed_count}/{len(phases)} phases have outputs. "
                "Use **Run all phases** or run missing phases manually."
            )


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    st.set_page_config(
        page_title="PM Skills Playground (beta)",
        page_icon="🧰",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Initialise session state
    defaults = {
        "view": "home",
        "theme": None,
        "skill": None,
        "messages": [],
        "scenario": "",
        "scenario_input": "",
        "phase": 0,
        "workflow_outputs": {},
        "selected_provider": "anthropic",
        "selected_model": provider_default_model("anthropic"),
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    skills = load_skills()
    current_skill = st.session_state.get("skill")

    render_sidebar(current_skill)

    view = st.session_state.get("view", "home")
    if view == "home":
        render_home(skills)
    elif view == "theme":
        render_theme(skills, st.session_state.get("theme", ""))
    elif view == "skill":
        render_skill_detail(st.session_state.get("skill"), st.session_state.get("theme"))
    elif view == "session":
        render_session(st.session_state.get("skill"))


if __name__ == "__main__":
    main()
