# Slides

This folder contains Quarto-based slides that can be rendered to PowerPoint using the same general workflow as the historical `mlops4ecm-website/slides` setup.

## Files

- `deep-learning-project-directions.qmd`
  The current 30-minute kickoff presentation.
- `template-mlops.pptx`
  Reference PowerPoint template copied from the earlier MLOps slide workflow.
- `Dockerfile`
  Builds a small Quarto container for previewing and rendering.
- `compose.yaml`
  Starts live preview for the current `.qmd` file.

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

