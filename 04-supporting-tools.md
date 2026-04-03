# Supporting Tools

Use the files in `domains/` for AI frameworks, model choices, and official domain-specific docs.

This page is about the generic tooling that helps you turn a model into a usable application.
These are not the main AI choices in your project. They are the tools around the model: how users interact with it, how you expose it through an API, how you package it, and how you structure the application around it.

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

Gradio is usually the fastest way to turn an AI model into something people can actually use. If your project needs a simple interface for text, images, audio, or chat, Gradio is often the best default because you can get a working demo online very quickly without building a full frontend from scratch. For many student projects, that is exactly the right tradeoff: less frontend work, more focus on the AI system itself.

Official docs: <https://www.gradio.app/docs>

## Streamlit

Streamlit is a good choice when your project feels more like a dashboard, data app, or interactive report than a classic product interface. It works especially well if you want to combine model output with plots, tables, controls, and quick exploratory views. If your application is strongly data-oriented, Streamlit can feel more natural than Gradio.

Official docs: <https://docs.streamlit.io/>

## React

React makes sense if the interface itself is an important part of the project and you want much more control over the user experience. It is the most flexible option on this page, but also the one that usually brings the most frontend complexity. Choose React if you already know some frontend development or if the project really needs a custom interface that Gradio or Streamlit would make awkward.

Official docs: <https://react.dev/>

## FastAPI

FastAPI is a strong choice when you want to build a Python backend around your model. It is useful if you want to separate frontend and backend, expose clean API endpoints, or serve inference in a more structured way than a quick demo tool would allow. If you are building a React frontend or a larger application architecture, FastAPI is often the natural backend choice.

Official docs: <https://fastapi.tiangolo.com/>

## Docker

Docker is about packaging and reproducibility. It is useful when your project has several dependencies, when you want your setup to be easier to rerun later, or when you want to deploy the same application in a more controlled way. Not every project needs Docker immediately, but it becomes valuable as soon as the environment starts getting messy or you want to move your app to another machine cleanly.

Official docs: <https://docs.docker.com/>

## Final Advice

- Choose your AI framework from the matching file in `domains/`.
- Use this page for interface, API, frontend, and packaging choices around your project.
- Start simple. A small working demo is better than an overengineered stack.
