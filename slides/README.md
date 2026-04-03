# Slides

This folder contains Quarto-based slides that can be rendered to PowerPoint using the same general workflow as the historical `mlops4ecm-website/slides` setup.

## Files

- `deep-learning-project-directions.qmd`
  The current 30-minute kickoff presentation.
- `template-mlops.pptx`
  Original reference PowerPoint template copied from the earlier MLOps slide workflow.
- `template-mlops-clean.pptx`
  Sanitized reference template used for Quarto rendering.
- `scripts/sanitize_reference_template.py`
  Helper script that removes Office metadata parts Quarto leaves dangling in new `.pptx` files.
- `Dockerfile`
  Builds a small Quarto container for previewing and rendering.
- `compose.yaml`
  Starts live preview for the current `.qmd` file.

## Why The Clean Template Exists

The original PowerPoint template contains `customXml`, `revisionInfo`, and
`changesInfo` package parts. Quarto preserves the relationships for those parts
when rendering a new deck, but does not copy the parts themselves. Windows
PowerPoint may then reject the generated file because the internal package
relationships are broken.

The cleaned template keeps the layout and styling, but removes those metadata
parts so generated decks stay compatible.

If the original template is updated, regenerate the clean template with:

```bash
cd /root/deep-learning-2026/slides
python3 scripts/sanitize_reference_template.py template-mlops.pptx template-mlops-clean.pptx
```

## Preview

```bash
cd /root/deep-learning-2026/slides
docker compose up --build
```

Then open:

```text
http://localhost:8080
```

## Render PowerPoint

```bash
cd /root/deep-learning-2026/slides
docker build -t deep-learning-slides .
docker run --rm -v "$(pwd)":/data -w /data deep-learning-slides \
  quarto render deep-learning-project-directions.qmd
```

The rendered file will be written next to the `.qmd`.
