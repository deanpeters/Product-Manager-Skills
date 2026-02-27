# Using PM Skills with ChatGPT

You can use this skills repo with ChatGPT in three ways, depending on how repeatable you want the setup.

If you want to test a skill locally first, use the Streamlit (beta) playground:

```bash
pip install -r app/requirements.txt
streamlit run app/main.py
```

---

## Option 1: Connect GitHub in ChatGPT Apps (Best for Active Repos)

Use this when you want ChatGPT to read current files from GitHub.

Availability can vary by plan and rollout region.

1. In ChatGPT, open **Settings**.
2. Go to **Apps** (or **Connected Apps**, depending on UI version).
3. Connect **GitHub** and authorize access.
4. In a chat, ask ChatGPT to use a skill file from this repo by path.

Example:

```text
Use skills/prioritization-advisor/SKILL.md from deanpeters/Product-Manager-Skills and guide me through choosing a framework for a B2B roadmap.
```

---

## Option 2: Build a Custom GPT with Skill Knowledge (Best for Reuse)

Use this when you want a reusable PM assistant that always carries selected skills.

1. In ChatGPT, create a new GPT.
2. Upload skill files as Knowledge.
3. Add instructions telling the GPT to follow the skill structure exactly.
4. Save and test.

Important for this repo:
- ChatGPT GPT Knowledge expects uploaded files; no GitHub auto-sync for these uploaded files.
- This repo stores source files as `SKILL.md`. For Claude-style compatibility packaging, run:

```bash
bash scripts/package-claude-skills.sh
```

Then upload the generated files from `dist/claude-skills/<skill-name>/Skill.md` (or upload the original `SKILL.md` files directly if you are only using ChatGPT).

---

## Option 3: Use ChatGPT Projects with Files (Best for One Initiative)

Use this for project-scoped work where you want files, chats, and instructions grouped together.

1. Create a Project in ChatGPT.
2. Upload one or more skill files (or a small curated set).
3. Add project instructions that require skill-conformant output.
4. Run your PM tasks inside that project.

---

## Recommended Project/GPT Instruction Snippet

```text
When solving PM tasks, use the uploaded skill files as the operating standard.
Follow each skill's sections in order: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References.
If context is missing, ask up to 3 clarifying questions before drafting.
```

---

## Official References

- [Apps in ChatGPT (includes GitHub)](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt/)
- [Creating a GPT](https://help.openai.com/en/articles/8554397-creating-a-gpt)
- [Knowledge in GPTs](https://help.openai.com/en/articles/8843948)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)
