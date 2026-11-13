# Install PM Skills in Claude Desktop or Claude Web

Claude Desktop and Claude Web are the easiest path for nontechnical PMs: download one pack, unzip it, upload the skill ZIPs inside, and start working.

## Quick Setup (about 5 minutes)

1. Open the [Product Manager Skills Releases page](https://github.com/deanpeters/Product-Manager-Skills/releases/latest).
2. Download [`pm-skills-starter-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-skills-starter-pack.zip), or choose the pack for your lifecycle phase from the table below. The six `pm-` packs follow the product lifecycle (Determine, Discover, Define, Develop, Deliver), and Drive runs underneath all of them.
3. Unzip the pack on your computer. You now have a folder of smaller ZIP files, one per skill.
4. Open Claude and go to **Settings → Capabilities → Skills**.
5. Upload the individual skill ZIPs from inside that folder. Start with two or three; you can add more later.
6. Start a new chat and ask Claude to use the Product Manager Skills.

Try:

```text
Use the Product Manager Skills to help me frame this product problem.
```

**You'll know it worked when** the skills appear in your Skills list and Claude names the skill it is using, then starts asking you questions. If the list stays empty, see the first note below.

## Which Pack Should I Choose?

| Pack | Best for | Use when |
|---|---|---|
| [`pm-skills-starter-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-skills-starter-pack.zip) | Most PMs | You want a small, practical starter set. |
| [`pm-determine-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-determine-pack.zip) | Setting direction | You need strategy, finance, market intelligence, or to understand your customer. |
| [`pm-discover-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-discover-pack.zip) | Finding the real problem | You need interviews, problem framing, opportunity trees, or journey maps. |
| [`pm-define-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-define-pack.zip) | Shaping and testing a solution | You need hypotheses, probes, experiments, or positioning. |
| [`pm-develop-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-develop-pack.zip) | Building work | You need PRDs, stories, prioritization, roadmaps, or AI-agent work. |
| [`pm-deliver-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-deliver-pack.zip) | Going to market and sunsetting | You need pricing, channels, or the lifecycle and end-of-life process. |
| [`pm-drive-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/pm-drive-pack.zip) | People and career | You need stakeholder work, influence, or help stepping up a level. |
| [`99-all-skills-pack.zip`](https://github.com/deanpeters/Product-Manager-Skills/releases/latest/download/99-all-skills-pack.zip) | Advanced users | You want everything and can tolerate a larger skill list. |

## A Good First Prompt

```text
Use the Product Manager Skills. Ask me the minimum useful questions, then help me turn this rough idea into a clear problem statement.
```

## Notes

- Start with the starter pack unless you know you need a specific pack. Each lifecycle pack also includes a few shared helper skills, so it works on its own.
- The older themed packs (`02-discovery` through `07-lifecycle-eol`) were retired in v0.86. Every skill in them lives in a lifecycle pack above.
- Do not upload the outer pack ZIP to Claude. Unzip the pack first, then upload the skill ZIPs inside it. If Claude rejects an upload or the Skills list stays empty, this is the usual cause.
- Arriving empty-handed is fine. The skills ask for what they need, so you can start with a one-line description of your situation.
- Use one practical problem from your work. These skills are strongest with real context.
- Claude Code users should usually use the plugin marketplace instead of these ZIPs. See [`INSTALL-CLAUDE-CODE.md`](INSTALL-CLAUDE-CODE.md).
- Codex users should use the Codex ZIP or download the full library from GitHub (green **Code** button, then **Download ZIP**). See [`INSTALL-CODEX.md`](INSTALL-CODEX.md).
