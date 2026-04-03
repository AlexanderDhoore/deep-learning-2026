# Generic Support Tooling

Use the files in `domains/` for AI frameworks, model choices, and official domain-specific docs.

This page is only about the generic tooling that helps you turn a model into a usable application.

Typical examples are:

- a quick web interface
- a backend API
- a custom frontend
- containerized packaging

## How To Use This Page

The practical workflow is:

1. choose a project domain in `domains/`
2. choose your main AI framework from that domain note
3. use this page for generic application tooling around the model

## Gradio

- Official docs: <https://www.gradio.app/docs>
- Best for:
  - fast demos
  - simple web interfaces
  - course projects that need a usable UI quickly

## Streamlit

- Official docs: <https://docs.streamlit.io/>
- Best for:
  - dashboards
  - quick Python apps
  - data-heavy interfaces

## React

- Official docs: <https://react.dev/>
- Best for:
  - richer custom frontends
  - students who want more control over the interface
- Tradeoff:
  - more flexibility
  - more frontend complexity

## FastAPI

- Official docs: <https://fastapi.tiangolo.com/>
- Best for:
  - Python backend APIs
  - separating frontend and backend
  - serving model inference behind a clean interface

## Docker

- Official docs: <https://docs.docker.com/>
- Best for:
  - packaging your application
  - reproducible deployment
  - keeping environments more predictable

## Final Advice

- Choose your AI framework from the matching file in `domains/`.
- Use this page for interface, API, frontend, and packaging choices around your project.
- Start simple. A small working demo is better than an overengineered stack.
