# Deep Learning 2026

This repository contains the course material for the deep-learning part of the 2026 course.

The course is short and strongly practice-oriented. The main goal is not to cover the whole field in mathematical depth, but to help you:

- get a broad overview of modern deep learning
- choose a project domain
- build a unique AI application
- understand and defend what you built

## Current Structure

- `01-strategic-project-paths.md`
  High-level map of the main technical paths you can choose.
- `02-overview-and-project-directions.md`
  Main kickoff text for the lesson: broad field overview plus project-domain framing.
- `03-assignment-brief.md`
  Assignment expectations and scope.
- `04-frameworks-and-official-docs.md`
  Curated list of useful frameworks plus official docs to start from.
- `05-edge-ai-and-deployment.md`
  Extra student-facing note for the edge deployment path, including ONNX Runtime, Jetson, TensorRT, and local model serving.
- `domains/`
  One short file per application domain. These notes help you choose a domain and find the best official docs to continue with.
- `slides/`
  Quarto-based slide deck source plus the generated PowerPoint for the kickoff presentation.

## Teaching Philosophy

- broad rather than deep
- practical rather than purely theoretical
- build something real
- use AI tools if useful, but understand your own code
- framework choice first, project idea second is a valid path

## Current High-Level Shape

The material is currently organized around:

1. strategic technical paths
2. application domains
3. frameworks and official docs

Generative AI is treated as a cross-cutting theme rather than one single modality next to vision or audio.
That idea is explained directly in the top-level notes instead of in a separate folder.
The technical paths are also explained directly in the top-level notes, especially in `01-strategic-project-paths.md`, instead of in a separate folder.

The slide deck is a shorter subset of the written notes. If you want more context after the presentation, start with the top-level Markdown files and then open the matching file in `domains/`.
