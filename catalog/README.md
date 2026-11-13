# Catalog Artifacts

These files are generated navigation indexes for skills and commands.

- `skills-index.yaml` - machine-readable skill metadata index
- `commands-index.yaml` - machine-readable command metadata index
- `skills-by-type.md` - human-readable browse view by skill type
- `skills-by-bundle.md` - human-readable browse view by lifecycle bundle and motion
- `commands.md` - human-readable command catalog

Regenerate any time skills or commands change:

```bash
python3 scripts/generate-catalog.py
```
