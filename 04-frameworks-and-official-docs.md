# Frameworks and Official Docs

This page is intentionally short.

Use the files in `domains/` for domain-specific frameworks, project ideas, and next steps.

This page keeps only the things that are shared across several domains:

- broad AI ecosystems
- fine-tuning and adaptation docs
- generic support tooling for interfaces, APIs, and packaging

## How To Use This Page

The practical workflow is:

1. choose a project direction in `domains/`
2. use that file to find the domain-specific AI frameworks
3. come back to this page only if you need shared tooling or broad ecosystem links

So this page does not replace the domain notes.
It only supports them.

## Broad AI Ecosystems

These are useful across multiple domains.

### PyTorch

- Official site: <https://pytorch.org/>
- Use it when you want to train your own models, write custom model code, or work at a lower level.

### Hugging Face Hub

- Official site: <https://huggingface.co/models>
- Use it to browse models, tasks, datasets, and model cards before you decide what to build.

### Hugging Face Transformers

- Official docs: <https://huggingface.co/docs/transformers/en/index>
- Use it for pretrained workflows across text, multimodal, speech, and several other domains.

## Generative AI and Adaptation

Generative AI is not treated as one separate application domain in this repository.

Instead, it appears across several directions:

- text generation in language-model projects
- image generation in visual workflows
- speech or music generation in audio workflows
- multimodal generation in richer assistant-style systems

Use the matching domain note first, then use the links below if you need shared generative tooling.

### Hugging Face Diffusers

- Official docs: <https://huggingface.co/docs/diffusers/en/index>
- Use it for diffusion-based image, video, and audio workflows.

### Fine-tuning and adaptation docs

- Transformers fine-tuning docs: <https://huggingface.co/docs/transformers/training>
- Transformers PEFT/adapters docs: <https://huggingface.co/docs/transformers/en/peft>
- TRL docs for LLM fine-tuning workflows: <https://huggingface.co/docs/trl/index>
- Diffusers training overview: <https://huggingface.co/docs/diffusers/training/overview>
- Diffusers text-to-image fine-tuning example: <https://huggingface.co/docs/diffusers/training/text2image>

## Generic Support Tooling

These are useful, but they are not the main AI choice.
They support the application around the model.
That is why they are kept here at the top level instead of being repeated in every domain note.

### Gradio

- Official docs: <https://www.gradio.app/docs>
- Good for fast demos and simple web interfaces.

### Streamlit

- Official docs: <https://docs.streamlit.io/>
- Good for dashboards and simple Python web apps.

### React

- Official docs: <https://react.dev/>
- Good if you want more frontend control and do not mind more complexity.

### FastAPI

- Official docs: <https://fastapi.tiangolo.com/>
- Good for Python backend APIs.

### Docker

- Official docs: <https://docs.docker.com/>
- Good for packaging and reproducible deployment.

## Final Advice

- If you want AI-specific guidance, go to the matching file in `domains/`.
- If you want shared ecosystems, adaptation docs, or generic support tooling, use this page.
- Start from official docs before looking for random tutorials.
