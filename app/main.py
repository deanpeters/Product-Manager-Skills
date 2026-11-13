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
DOCS_DIR = Path(__file__).parent.parent / "docs"
ROOT_DIR = Path(__file__).parent.parent
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


# ─── Lifecycle bundles (from pm-skills.config.yaml) ───────────────────────────
# The browser groups skills by lifecycle bundle (Determine, Discover, Define,
# Develop, Deliver, Drive, plus Core). The old per-skill `theme` frontmatter is
# the fallback if the config is missing.
BUNDLE_ICONS = {
    "determine": "🧭", "discover": "🔍", "define": "🧪",
    "develop": "🛠️", "deliver": "🚚", "drive": "🪜", "core": "🧰",
}
SKILL_HOMES: dict[str, tuple[str, str]] = {}      # skill -> (bundle, motion)
BUNDLE_MOTIONS: dict[str, list[dict]] = {}        # bundle -> [{name, summary, skills, gap}]


def _load_lifecycle() -> None:
    global THEMES
    cfg_path = Path(__file__).parent.parent / "pm-skills.config.yaml"
    try:
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return
    bundles = cfg.get("bundles") or {}
    if not bundles:
        return
    themes: dict = {}
    for bname, bundle in bundles.items():
        motions = []
        for mname, motion in bundle["motions"].items():
            for sk in motion.get("skills") or []:
                SKILL_HOMES[sk] = (bname, mname)
            motions.append({"name": mname, "summary": motion.get("summary", ""),
                            "skills": motion.get("skills") or [], "gap": motion.get("gap")})
        BUNDLE_MOTIONS[bname] = motions
        themes[bname] = {"label": bname.capitalize(), "icon": BUNDLE_ICONS.get(bname, "📦"),
                         "description": f"{bundle['summary']} ({bundle['phase']})"}
    core = cfg.get("core") or []
    if core:
        for sk in core:
            SKILL_HOMES[sk] = ("core", "core")
        themes["core"] = {"label": "Core", "icon": BUNDLE_ICONS["core"],
                          "description": "Shared helpers the other skills lean on: facilitation, investigation, authoring"}
        BUNDLE_MOTIONS["core"] = [{"name": "core", "summary": "", "skills": core, "gap": None}]
    THEMES = themes


_load_lifecycle()

TYPE_BADGES = {
    "component": ("🧱", "Component"),
    "interactive": ("🔄", "Interactive"),
    "workflow": ("🎭", "Workflow"),
}

GUIDE_GROUPS = [
    {
        "label": "Start Here",
        "guides": [
            {
                "id": "start_here",
                "title": "Start Here",
                "path": ROOT_DIR / "START_HERE.md",
                "summary": "Fastest path from zero to first useful output.",
            },
            {
                "id": "pm_skills_101",
                "title": "Using PM Skills 101",
                "path": DOCS_DIR / "Using PM Skills 101.md",
                "summary": "Beginner-first orientation and platform install patterns.",
            },
            {
                "id": "platform_guides",
                "title": "Platform Guides for PMs",
                "path": DOCS_DIR / "Platform Guides for PMs.md",
                "summary": "Pick-your-tool index for all supported harnesses.",
            },
        ],
    },
    {
        "label": "Core Platforms",
        "guides": [
            {
                "id": "claude",
                "title": "Using PM Skills with Claude",
                "path": DOCS_DIR / "Using PM Skills with Claude.md",
                "summary": "Claude setup across Code, Desktop, and Cowork.",
            },
            {
                "id": "codex",
                "title": "Using PM Skills with Codex",
                "path": DOCS_DIR / "Using PM Skills with Codex.md",
                "summary": "Run skills via local paths or GitHub-connected Codex.",
            },
            {
                "id": "chatgpt",
                "title": "Using PM Skills with ChatGPT",
                "path": DOCS_DIR / "Using PM Skills with ChatGPT.md",
                "summary": "Projects, GPT Knowledge, and GitHub-connected usage.",
            },
        ],
    },
    {
        "label": "Claude + Chat Apps",
        "guides": [
            {
                "id": "claude_code",
                "title": "Using PM Skills with Claude Code",
                "path": DOCS_DIR / "Using PM Skills with Claude Code.md",
                "summary": "CLI-first usage with direct file path workflows.",
            },
            {
                "id": "claude_desktop",
                "title": "Using PM Skills with Claude Desktop",
                "path": DOCS_DIR / "Using PM Skills with Claude Desktop.md",
                "summary": "No-code upload flow and starter usage patterns.",
            },
            {
                "id": "claude_cowork",
                "title": "Using PM Skills with Claude Cowork",
                "path": DOCS_DIR / "Using PM Skills with Claude Cowork.md",
                "summary": "Knowledge-module style workspace usage.",
            },
            {
                "id": "claude_slash",
                "title": "Using PM Skills with Slash Commands 101",
                "path": DOCS_DIR / "Using PM Skills with Slash Commands 101.md",
                "summary": "Turn PM skills into reusable /commands.",
            },
            {
                "id": "chatgpt_desktop",
                "title": "Using PM Skills with ChatGPT Desktop",
                "path": DOCS_DIR / "Using PM Skills with ChatGPT Desktop.md",
                "summary": "Project-first setup in desktop chat workflows.",
            },
        ],
    },
    {
        "label": "Automation + Agent Harnesses",
        "guides": [
            {
                "id": "n8n",
                "title": "Using PM Skills with n8n",
                "path": DOCS_DIR / "Using PM Skills with n8n.md",
                "summary": "Repeatable AI workflows with skill injection patterns.",
            },
            {
                "id": "langflow",
                "title": "Using PM Skills with LangFlow",
                "path": DOCS_DIR / "Using PM Skills with LangFlow.md",
                "summary": "Visual prompt-chain setup with skill context.",
            },
            {
                "id": "python_agents",
                "title": "Using PM Skills with Python Agents",
                "path": DOCS_DIR / "Using PM Skills with Python Agents.md",
                "summary": "Embed skill files into custom agent pipelines.",
            },
            {
                "id": "openclaw",
                "title": "Using PM Skills with OpenClaw",
                "path": DOCS_DIR / "Using PM Skills with OpenClaw.md",
                "summary": "System prompt and router patterns for self-hosted agents.",
            },
            {
                "id": "cursor",
                "title": "Using PM Skills with Cursor",
                "path": DOCS_DIR / "Using PM Skills with Cursor.md",
                "summary": "Persistent rules plus @file invocation pattern.",
            },
            {
                "id": "windsurf",
                "title": "Using PM Skills with Windsurf",
                "path": DOCS_DIR / "Using PM Skills with Windsurf.md",
                "summary": "Cascade rules and context-aware multi-step usage.",
            },
            {
                "id": "bolt",
                "title": "Using PM Skills with Bolt",
                "path": DOCS_DIR / "Using PM Skills with Bolt.md",
                "summary": "Problem-first prompts before prototype generation.",
            },
            {
                "id": "replit",
                "title": "Using PM Skills with Replit Agent",
                "path": DOCS_DIR / "Using PM Skills with Replit Agent.md",
                "summary": "System prompt guardrails for iterative build loops.",
            },
            {
                "id": "make",
                "title": "Using PM Skills with Make.com",
                "path": DOCS_DIR / "Using PM Skills with Make.com.md",
                "summary": "No-code scenario design with skill-driven AI modules.",
            },
            {
                "id": "devin",
                "title": "Using PM Skills with Devin",
                "path": DOCS_DIR / "Using PM Skills with Devin.md",
                "summary": "Keep autonomous execution aligned with PM guardrails.",
            },
            {
                "id": "crewai",
                "title": "Using PM Skills with CrewAI",
                "path": DOCS_DIR / "Using PM Skills with CrewAI.md",
                "summary": "Map skills to multi-agent roles and orchestration.",
            },
            {
                "id": "gemini",
                "title": "Using PM Skills with Gemini",
                "path": DOCS_DIR / "Using PM Skills with Gemini.md",
                "summary": "Gemini CLI, AI Studio, and persistent context patterns.",
            },
        ],
    },
]

LEARN_TO_RUN_SKILLS = [
    ("prioritization-advisor", "Interactive"),
    ("user-story", "Component"),
    ("prd-development", "Workflow"),
]

FIND_MY_SKILL_PROMPTS = [
    "I need to figure out why activation is dropping for new users.",
    "Help me decide whether this feature is worth building.",
    "I need to turn discovery notes into a PRD my engineers can use.",
    "We need a clearer prioritization framework for roadmap decisions.",
]

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
                "intent": fm.get("intent", ""),
                "type": fm.get("type", "component"),
                "theme": SKILL_HOMES.get(fm.get("name", skill_dir.name), (fm.get("theme"),))[0],
                "motion": SKILL_HOMES.get(fm.get("name", skill_dir.name), (None, None))[1],
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


@st.cache_data
def load_guide_markdown(path_str: str) -> str:
    path = Path(path_str)
    if not path.exists():
        return f"# Missing guide\n\nCould not find `{path}`."
    return path.read_text(encoding="utf-8")


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


FINDER_STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "at",
    "be",
    "by",
    "do",
    "for",
    "from",
    "help",
    "how",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "me",
    "my",
    "need",
    "new",
    "of",
    "on",
    "or",
    "our",
    "that",
    "the",
    "this",
    "to",
    "user",
    "users",
    "we",
    "what",
    "when",
    "with",
}


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def tokenize_text(value: str) -> list[str]:
    tokens: list[str] = []
    for token in re.findall(r"[a-z0-9]+", normalize_text(value)):
        if len(token) <= 1 or token in FINDER_STOP_WORDS:
            continue
        tokens.append(token)
    return tokens


def tokens_match(query_token: str, candidate_token: str) -> bool:
    if query_token == candidate_token:
        return True
    if len(query_token) >= 4 and candidate_token.startswith(query_token):
        return True
    if len(candidate_token) >= 4 and query_token.startswith(candidate_token):
        return True
    if len(query_token) >= 5 and len(candidate_token) >= 5:
        if query_token in candidate_token or candidate_token in query_token:
            return True
    return False


def matched_query_tokens(query_tokens: list[str], text: str) -> list[str]:
    text_tokens = tokenize_text(text)
    matched: list[str] = []
    for query_token in query_tokens:
        if any(tokens_match(query_token, candidate) for candidate in text_tokens):
            matched.append(query_token)
    return matched


def summarize_match_reasons(skill: dict, query_lc: str, query_tokens: list[str]) -> list[str]:
    reasons: list[str] = []
    fields = [
        ("description", skill.get("description", "")),
        ("best for", " ".join(skill.get("best_for") or [])),
        ("scenarios", " ".join(skill.get("scenarios") or [])),
        ("intent", skill.get("intent", "")),
        ("purpose", skill.get("purpose_short", "")),
    ]
    for label, raw_text in fields:
        normalized = normalize_text(raw_text)
        if query_lc and query_lc in normalized:
            reasons.append(label)
            continue
        if query_tokens and matched_query_tokens(query_tokens, raw_text):
            reasons.append(label)
    return reasons[:3]


def rank_skills_for_query(
    skills: list[dict],
    query: str,
    type_filter: str = "Any",
    theme_filter: str = "Any",
) -> list[dict]:
    query_lc = normalize_text(query)
    query_tokens = tokenize_text(query)
    results: list[dict] = []

    for skill in skills:
        if type_filter != "Any" and skill["type"] != type_filter:
            continue
        if theme_filter != "Any" and skill.get("theme") != theme_filter:
            continue

        name_lc = normalize_text(skill.get("name", ""))
        score = 0
        match = "browse"

        if not query_lc:
            score = 50
        elif name_lc == query_lc:
            score = 400
            match = "exact name"
        else:
            field_specs = [
                ("name", skill.get("name", ""), 320, 120),
                ("trigger metadata", skill.get("description", ""), 240, 45),
                ("best for", " ".join(skill.get("best_for") or []), 220, 55),
                ("scenarios", " ".join(skill.get("scenarios") or []), 220, 55),
                ("intent", skill.get("intent", ""), 180, 30),
                ("purpose", skill.get("purpose_short", ""), 140, 24),
                ("skill body", skill.get("body", ""), 80, 8),
            ]

            best_label = ""
            best_field_score = 0
            matched_token_set: set[str] = set()

            for label, text, phrase_bonus, token_weight in field_specs:
                normalized_text = normalize_text(text)
                field_score = 0
                if query_lc and query_lc in normalized_text:
                    field_score += phrase_bonus

                token_hits = matched_query_tokens(query_tokens, text)
                if token_hits:
                    unique_hits = len(set(token_hits))
                    field_score += unique_hits * token_weight
                    matched_token_set.update(token_hits)

                if field_score > best_field_score:
                    best_field_score = field_score
                    best_label = label

                score += field_score

            if not score:
                continue

            if best_label:
                match = best_label

            if query_tokens:
                coverage = len(matched_token_set) / max(len(query_tokens), 1)
                score += int(coverage * 100)

            if len(query_tokens) >= 3 and len(matched_token_set) < 2:
                continue

        results.append(
            {
                "skill": skill,
                "score": score,
                "match": match,
                "reasons": summarize_match_reasons(skill, query_lc, query_tokens),
            }
        )

    results.sort(key=lambda item: (-item["score"], item["skill"]["name"]))
    return results


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


def queue_finder_reset():
    """Request a finder reset on the next rerun."""
    st.session_state["finder_reset_requested"] = True


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

        view = st.session_state.get("view", "home")
        run_views = {"find_home", "run_home", "theme", "skill", "session"}

        nav_cols = st.columns(3)
        with nav_cols[0]:
            if st.button("📚 Learn", use_container_width=True):
                nav("learn_home")
        with nav_cols[1]:
            if st.button("🧭 Find", use_container_width=True):
                nav("find_home")
        with nav_cols[2]:
            if st.button("🧪 Run Skills", use_container_width=True):
                nav("run_home")
        if st.button("🏠 Start", use_container_width=True):
            nav("home")

        if view in run_views:
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
        else:
            st.info("Browse setup guides first, then jump into Run Skills when ready.")

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
                    nav("run_home")
            if st.button("🏠 Home", use_container_width=True):
                nav("run_home")
        else:
            if st.button("🏠 Home", use_container_width=True):
                nav("run_home" if view in run_views else "home")

        st.divider()
        st.caption("Streamlit (beta) · New feature in flight")
        st.caption(
            "[Feedback via GitHub ↗](https://github.com/deanpeters/Product-Manager-Skills/issues) · "
            "[Connect on LinkedIn ↗](https://linkedin.com/in/deanpeters)"
        )
        st.caption("47 PM skills · CC BY-NC-SA 4.0")
        st.caption("[GitHub ↗](https://github.com/deanpeters/product-manager-skills)")


def get_guide(guide_id: str) -> dict | None:
    for group in GUIDE_GROUPS:
        for guide in group["guides"]:
            if guide["id"] == guide_id:
                return guide
    return None


# ─── Screen: Home / Learn ────────────────────────────────────────────────────

def render_home():
    st.title("PM Skills Playground")
    st.markdown(
        "Choose your mode: **Learn** setup/integration, **Find My Skill** from your situation, or **Run Skills** directly."
    )
    st.caption("The docs stay the source of truth; the app helps you navigate and practice.")

    left, middle, right = st.columns(3)
    with left:
        with st.container(border=True):
            st.markdown("### 📚 Learn & Setup")
            st.caption(
                "Read platform guides, onboarding docs, and installation playbooks in one place."
            )
            if st.button("Open Learn Hub →", type="primary", use_container_width=True):
                nav("learn_home")
    with middle:
        with st.container(border=True):
            st.markdown("### 🧭 Find My Skill")
            st.caption(
                "Describe what you're trying to do and get ranked skill recommendations with why they fit."
            )
            if st.button("Open Skill Finder →", use_container_width=True):
                nav("find_home")
    with right:
        with st.container(border=True):
            st.markdown("### 🧪 Run Skills")
            st.caption(
                "Test-drive component, interactive, and workflow skills with your own scenario."
            )
            if st.button("Open Skill Runner →", use_container_width=True):
                nav("run_home")


def render_learn_home(skills: list):
    st.title("📚 Learn PM Skills")
    st.markdown(
        "Start with onboarding docs, then open a platform-specific guide. "
        "When ready, jump straight into a skill run from this page."
    )

    for group in GUIDE_GROUPS:
        st.markdown(f"### {group['label']}")
        for guide in group["guides"]:
            with st.container(border=True):
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.markdown(f"**{guide['title']}**")
                    st.caption(guide["summary"])
                with c2:
                    if st.button("Open", key=f"guide_{guide['id']}", use_container_width=True):
                        nav("learn_doc", guide_id=guide["id"])

    st.divider()
    st.markdown("### Practice While You Learn")
    st.caption(
        "Pick one starter skill and run it now. This keeps learning tied to real output."
    )
    run_cols = st.columns(3)
    skills_by_name = {s["name"]: s for s in skills}
    for i, (skill_name, label) in enumerate(LEARN_TO_RUN_SKILLS):
        skill = skills_by_name.get(skill_name)
        if not skill:
            continue
        with run_cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{skill_name}**")
                st.caption(f"{label} starter")
                if st.button("Run this skill →", key=f"learn_run_{skill_name}", use_container_width=True):
                    nav("skill", skill=skill, theme=skill.get("theme"))


def render_learn_doc():
    guide_id = st.session_state.get("guide_id")
    guide = get_guide(guide_id or "")
    if not guide:
        st.error("Guide not found.")
        nav("learn_home")
        return

    top = st.columns([1, 6])
    with top[0]:
        if st.button("← Back"):
            nav("learn_home")
    with top[1]:
        st.title(guide["title"])
        st.caption(str(guide["path"].relative_to(ROOT_DIR)))

    content = load_guide_markdown(str(guide["path"]))
    st.markdown(content)

    st.divider()
    if st.button("🧪 Try a skill now", use_container_width=True):
        nav("run_home")


def render_find_home(skills: list):
    if st.session_state.get("finder_reset_requested"):
        st.session_state["finder_query_input"] = ""
        st.session_state["finder_last_query"] = ""
        st.session_state["finder_type_filter"] = "Any"
        st.session_state["finder_theme_filter"] = "Any"
        st.session_state["finder_reset_requested"] = False

    st.title("🧭 Find My Skill")
    st.markdown(
        "Describe the job you need done, click **Find Skills**, and the app will recommend the best-fit PM skills."
    )
    st.caption("You do not need to know the skill name. Start with plain English like “Help me create a PRD” or “I need to prioritize roadmap bets.”")
    st.info(
        "Finder results are local and instant. The app only calls an API after you choose **Run This Skill** or start a skill session."
    )

    steps = st.columns(3)
    step_copy = [
        ("1", "Describe your situation"),
        ("2", "Click Find Skills"),
        ("3", "Preview or run the best match"),
    ]
    for col, (step_num, step_text) in zip(steps, step_copy):
        with col:
            with st.container(border=True):
                st.markdown(f"**Step {step_num}**")
                st.caption(step_text)

    if not st.session_state.get("finder_query_input"):
        chips = st.columns(len(FIND_MY_SKILL_PROMPTS))
        for i, prompt in enumerate(FIND_MY_SKILL_PROMPTS):
            with chips[i]:
                if st.button(prompt, key=f"finder_prompt_{i}", use_container_width=True):
                    st.session_state["finder_query_input"] = prompt
                    st.session_state["finder_last_query"] = prompt
                    st.rerun()

    st.divider()
    with st.form("finder_form", clear_on_submit=False):
        form_col, filter_col = st.columns([3, 2])
        with form_col:
            query = st.text_area(
                "What are you trying to do?",
                placeholder=(
                    "Example: Help me create a PRD from discovery notes for a new onboarding improvement."
                ),
                height=120,
                key="finder_query_input",
            ).strip()
            st.caption("Tip: write the situation the way you would ask a teammate.")
        with filter_col:
            type_filter = st.selectbox(
                "Skill type",
                options=["Any", "component", "interactive", "workflow"],
                key="finder_type_filter",
            )
            theme_options = ["Any"] + [
                slug for slug in THEMES if any(s.get("theme") == slug for s in skills)
            ]
            theme_filter = st.selectbox(
                "Theme",
                options=theme_options,
                format_func=lambda value: "Any" if value == "Any" else THEMES[value]["label"],
                key="finder_theme_filter",
            )

        action_cols = st.columns([1, 1, 4])
        with action_cols[0]:
            submitted = st.form_submit_button("Find Skills", type="primary", use_container_width=True)
        with action_cols[1]:
            cleared = st.form_submit_button(
                "Clear",
                use_container_width=True,
            )

    if cleared:
        queue_finder_reset()
        st.rerun()

    if submitted:
        st.session_state["finder_last_query"] = st.session_state.get("finder_query_input", "").strip()

    query = st.session_state.get("finder_query_input", "").strip()
    active_query = st.session_state.get("finder_last_query", "").strip()
    if query != active_query and query:
        st.info("Click **Find Skills** to refresh the recommendations for your latest wording.")

    if not active_query:
        st.info("Enter your situation above, then click **Find Skills**.")
        return

    results = rank_skills_for_query(skills, active_query, type_filter, theme_filter)
    st.markdown(f"### Best Matches for “{active_query}”")
    st.caption(f"{len(results)} matching skills")

    if not results:
        st.warning("No matching skills found yet. Try simpler phrasing or remove a filter.")
        return

    top = results[0]
    top_skill = top["skill"]
    top_icon, top_type_label = TYPE_BADGES.get(top_skill["type"], ("", "Skill"))
    with st.container(border=True):
        st.markdown("#### Recommended First")
        st.markdown(f"**{top_icon} {top_skill['name']}**")
        st.caption(f"{top_type_label} skill")
        st.markdown(top_skill["description"])
        why_text = ", ".join(top["reasons"]) if top["reasons"] else top["match"]
        st.caption(f"Why this is a good fit: matched on {why_text}.")
        if top_skill.get("best_for"):
            st.markdown("**Best for**")
            for bf in top_skill["best_for"][:3]:
                st.markdown(f"- {bf}")
        top_actions = st.columns(2)
        with top_actions[0]:
            if st.button("Preview This Skill", key=f"finder_top_preview_{top_skill['name']}", type="primary", use_container_width=True):
                nav("skill", skill=top_skill, theme=top_skill.get("theme"))
        with top_actions[1]:
            if st.button("Run This Skill", key=f"finder_top_run_{top_skill['name']}", use_container_width=True):
                seed_scenario = active_query or (top_skill.get("scenarios") or [""])[0]
                nav("session", skill=top_skill, theme=top_skill.get("theme"), scenario=seed_scenario)
        st.caption("Running a skill sends your scenario to the selected model and will show a spinner on the next screen.")

    if len(results) > 1:
        st.markdown("### Other Good Options")

    for item in results[1:10]:
        skill = item["skill"]
        icon, type_label = TYPE_BADGES.get(skill["type"], ("", "Skill"))
        with st.container(border=True):
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"**{icon} {skill['name']}**")
                st.caption(skill["description"])
                if item["reasons"]:
                    st.caption(
                        "Why this matches: " + ", ".join(item["reasons"]) + "."
                    )
                else:
                    st.caption(f"Why this matches: {item['match']}.")
                if skill.get("best_for"):
                    for bf in skill["best_for"][:3]:
                        st.markdown(f"- {bf}")
                elif skill.get("purpose_short"):
                    st.caption(skill["purpose_short"][:220])
            with c2:
                st.caption(f"{type_label} skill")
                if st.button("Preview →", key=f"finder_preview_{skill['name']}", use_container_width=True):
                    nav("skill", skill=skill, theme=skill.get("theme"))
                if st.button("Run →", key=f"finder_run_{skill['name']}", use_container_width=True):
                    seed_scenario = query or (skill.get("scenarios") or [""])[0]
                    nav("session", skill=skill, theme=skill.get("theme"), scenario=seed_scenario)


# ─── Screen: Run Home ─────────────────────────────────────────────────────────

GLOBAL_CONTEXT_PRESETS = [
    "I am a PM at a B2B SaaS startup. Activation dropped from 42% to 31% in two months.",
    "I own onboarding for a fintech mobile app. Week-1 retention is flat and leadership wants a plan.",
    "I am preparing a roadmap for an AI assistant feature and need to prioritize bets with limited engineering capacity.",
    "I need to turn a rough feature idea into clear user stories and acceptance criteria for sprint planning.",
]


def build_learning_simulator_system_prompt(skill: dict) -> str:
    return (
        "You are a PM Skills learning simulator.\n"
        "Run the skill end-to-end internally using the provided context.\n"
        "Do not ask follow-up questions.\n"
        "Make explicit assumptions when needed.\n\n"
        f"Skill definition:\n\n{skill['body']}"
    )


def build_learning_simulator_user_prompt(skill: dict, context: str) -> str:
    return (
        f"Skill: {skill['name']} ({skill['type']})\n\n"
        f"Context:\n{context}\n\n"
        "Run through the skill steps as a worked example and return markdown with exactly these H2 sections in this order:\n"
        "## Filled Template / Form\n"
        "Provide the completed artifact/output as if the skill were fully run for this context.\n\n"
        "## Steps and Transformations\n"
        "Number each step. For each step include:\n"
        "- what input was used\n"
        "- what processing or reasoning happened\n"
        "- what output was produced and carried forward\n\n"
        "## Assumptions Made\n"
        "List assumptions you introduced to complete missing details.\n"
    )


def parse_h2_sections(markdown_text: str) -> dict[str, str]:
    lines = markdown_text.splitlines()
    sections: dict[str, list[str]] = {}
    current = "__full__"
    sections[current] = []

    for line in lines:
        if line.startswith("## "):
            current = line[3:].strip().lower()
            sections[current] = []
            continue
        sections.setdefault(current, []).append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}


def render_run_theme_browser(skills: list):
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


def render_run_home(skills: list):
    st.title("🧪 Run Skills (Learning Simulator)")
    st.markdown(
        "Paste your context, click **Run the Skill Steps**, and get a worked example with a filled output and a step-by-step transformation walkthrough."
    )

    providers = available_providers()
    if not providers:
        st.warning(
            "Configure at least one provider to run simulations: "
            "`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `OLLAMA_ENABLED=1` with `OLLAMA_BASE_URL`."
        )

    skills_sorted = sorted(skills, key=lambda s: s["name"])
    skills_by_name = {s["name"]: s for s in skills_sorted}
    skill_names = list(skills_by_name.keys())

    if not skill_names:
        st.error("No skills were loaded from `skills/*/SKILL.md`.")
        return

    default_skill = st.session_state.get("runner_skill_name", skill_names[0])
    if default_skill not in skills_by_name:
        default_skill = skill_names[0]
        st.session_state["runner_skill_name"] = default_skill

    selected_skill_name = st.selectbox(
        "1) Choose a skill",
        options=skill_names,
        index=skill_names.index(default_skill),
        key="runner_skill_name",
    )
    selected_skill = skills_by_name[selected_skill_name]
    type_icon, type_label = TYPE_BADGES.get(selected_skill["type"], ("", "Skill"))
    st.caption(f"{type_icon} {type_label} · {selected_skill['description']}")

    context_mode = st.radio(
        "2) Pick context source",
        options=["Choose a quick context", "Write my own context"],
        horizontal=True,
        key="runner_context_mode",
    )

    quick_contexts = list(dict.fromkeys((selected_skill.get("scenarios") or []) + GLOBAL_CONTEXT_PRESETS))
    if context_mode == "Choose a quick context":
        if st.session_state.get("runner_context_preset") not in quick_contexts:
            st.session_state["runner_context_preset"] = quick_contexts[0]
        selected_context = st.selectbox(
            "Context",
            options=quick_contexts,
            key="runner_context_preset",
        )
    else:
        selected_context = st.text_area(
            "Context",
            value=st.session_state.get("runner_context_custom", ""),
            placeholder=(
                "Example: I am a PM at a 25-person B2B SaaS company. "
                "New trial users are not reaching first value within 7 days..."
            ),
            height=140,
            key="runner_context_custom",
        ).strip()

    run_disabled = not selected_context or not providers
    run_label = f"Run the Skill Steps ({selected_skill_name})"
    if st.button(run_label, type="primary", use_container_width=True, disabled=run_disabled):
        provider = st.session_state.get("selected_provider", providers[0])
        if provider not in providers:
            provider = providers[0]
            st.session_state["selected_provider"] = provider

        model_options = provider_model_options(provider)
        model = st.session_state.get("selected_model", provider_default_model(provider))
        if model not in model_options:
            model = provider_default_model(provider)
            st.session_state["selected_model"] = model

        api_key = provider_key(provider)
        system = build_learning_simulator_system_prompt(selected_skill)
        prompt = build_learning_simulator_user_prompt(selected_skill, selected_context)

        with st.spinner("Running skill steps..."):
            try:
                response = call_model(
                    provider,
                    api_key,
                    model,
                    system,
                    [{"role": "user", "content": prompt}],
                )
                st.session_state["runner_result"] = {
                    "skill_name": selected_skill_name,
                    "skill_type": selected_skill["type"],
                    "provider": PROVIDERS[provider]["label"],
                    "model": model,
                    "context": selected_context,
                    "response": response,
                }
                st.rerun()
            except Exception as e:
                if is_auth_error(e):
                    st.error(f"Invalid {PROVIDERS[provider]['label']} API key. Check your environment configuration.")
                    return
                st.error(f"API error: {e}")
                return

    result = st.session_state.get("runner_result")
    if result:
        st.divider()
        st.markdown(f"### Worked Example: `{result['skill_name']}`")
        st.caption(
            f"Provider: {result['provider']} · Model: {result['model']} · Skill type: {result['skill_type']}"
        )
        if st.button("Clear worked example", use_container_width=False):
            st.session_state["runner_result"] = None
            st.rerun()
        with st.expander("Context used", expanded=False):
            st.markdown(result["context"])

        sections = parse_h2_sections(result["response"])
        filled = sections.get("filled template / form", "")
        transformed = sections.get("steps and transformations", "")
        assumptions = sections.get("assumptions made", "")

        st.markdown("#### Filled Template / Form")
        with st.container(border=True):
            if filled:
                st.markdown(filled)
            else:
                st.markdown(result["response"])

        st.markdown("#### Steps and Transformations")
        with st.container(border=True):
            if transformed:
                st.markdown(transformed)
            else:
                st.info("The model did not return a dedicated steps section for this run.")

        if assumptions:
            st.markdown("#### Assumptions Made")
            with st.container(border=True):
                st.markdown(assumptions)

    st.divider()
    with st.expander("Need the older advanced browser? Open themes and manual sessions.", expanded=False):
        render_run_theme_browser(skills)


# ─── Screen: Theme ────────────────────────────────────────────────────────────

def render_theme(skills: list, theme_slug: str):
    meta = THEMES.get(theme_slug, {"label": theme_slug, "icon": "📦", "description": ""})

    if st.button("← Back to the lifecycle"):
        nav("run_home")

    st.title(f"{meta['icon']} {meta['label']}")
    st.markdown(meta["description"])
    st.divider()

    theme_skills = [s for s in skills if s.get("theme") == theme_slug]

    if not theme_skills:
        st.info("No skills tagged with this theme yet — check back soon.")
        return

    def _skill_card(s):
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

    motions = BUNDLE_MOTIONS.get(theme_slug)
    if not motions:
        for s in sorted(theme_skills, key=lambda x: x["name"]):
            _skill_card(s)
        return

    by_name = {s["name"]: s for s in theme_skills}
    for motion in motions:
        if theme_slug != "core":
            st.subheader(motion["name"].capitalize())
            if motion["summary"]:
                st.caption(motion["summary"])
        for sk in sorted(motion["skills"]):
            if sk in by_name:
                _skill_card(by_name[sk])
        if not motion["skills"]:
            st.info(f"Coming: {motion['gap'] or 'in progress'}")


# ─── Screen: Skill Detail ─────────────────────────────────────────────────────

def render_skill_detail(skill: dict, theme_slug: str | None):
    if skill is None:
        st.error("No skill selected.")
        nav("run_home")
        return

    meta = THEMES.get(theme_slug or "", {"label": "All Skills"})
    icon, type_label = TYPE_BADGES.get(skill["type"], ("", "Skill"))

    # Breadcrumb nav
    bc = st.columns([1, 1, 6])
    with bc[0]:
        if st.button("🏠 Home"):
            nav("run_home")
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

    # What to bring — the skill's own Input section. Optional by design:
    # arriving empty-handed is fine, the guided flow covers the gaps.
    if skill["sections"].get("Input"):
        with st.expander("🎒 What to bring (all optional — the skill walks you through the rest)"):
            st.markdown(skill["sections"]["Input"])

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
    else:
        st.caption("Starting this skill will call the selected model. A spinner will appear on the next screen while it runs.")


# ─── Screen: Session ──────────────────────────────────────────────────────────

def render_session(skill: dict | None):
    if skill is None:
        st.error("No skill selected.")
        nav("run_home")
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
        "guide_id": None,
        "theme": None,
        "skill": None,
        "finder_query_input": "",
        "finder_last_query": "",
        "finder_reset_requested": False,
        "finder_type_filter": "Any",
        "finder_theme_filter": "Any",
        "messages": [],
        "scenario": "",
        "scenario_input": "",
        "phase": 0,
        "workflow_outputs": {},
        "runner_skill_name": "",
        "runner_context_mode": "Choose a quick context",
        "runner_context_preset": "",
        "runner_context_custom": "",
        "runner_result": None,
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
        render_home()
    elif view == "learn_home":
        render_learn_home(skills)
    elif view == "learn_doc":
        render_learn_doc()
    elif view == "find_home":
        render_find_home(skills)
    elif view == "run_home":
        render_run_home(skills)
    elif view == "theme":
        render_theme(skills, st.session_state.get("theme", ""))
    elif view == "skill":
        render_skill_detail(st.session_state.get("skill"), st.session_state.get("theme"))
    elif view == "session":
        render_session(st.session_state.get("skill"))


if __name__ == "__main__":
    main()
