# Frameworks and Official Docs

This page is a practical starting point for students who need to learn a tool quickly.

The idea is simple:

- choose one main direction
- choose one main model/framework stack
- start from the official docs
- build something small first

## Core Framework

### PyTorch

- Main role: general deep-learning framework
- Good for: almost everything
- Official site: <https://pytorch.org/>
- Why it matters: this is the most important base framework to know in this course

## Text, Language Models, and Multimodal Models

### Hugging Face Transformers

- Main role: pretrained models for text, vision, audio, video, and multimodal use cases
- Official docs: <https://huggingface.co/docs/transformers/en/index>
- Good for:
  - text generation
  - text classification
  - question answering
  - image + text models
  - speech models

### Sentence Transformers

- Main role: embeddings, semantic search, retrieval, similarity
- Official docs: <https://www.sbert.net/>
- Good for:
  - semantic search
  - retrieval
  - document similarity
  - lightweight RAG-style apps

## Generative AI

### Hugging Face Diffusers

- Main role: diffusion models for images, video, and audio
- Official docs: <https://huggingface.co/docs/diffusers/en/index>
- Good for:
  - text-to-image
  - image-to-image
  - inpainting
  - other diffusion workflows

## Computer Vision

### Ultralytics YOLO

- Main role: fast practical computer vision
- Official docs: <https://docs.ultralytics.com/>
- Good for:
  - object detection
  - segmentation
  - pose estimation
  - tracking
  - classification

### OpenCV

- Main role: classic computer vision and image/video preprocessing
- Official docs: <https://docs.opencv.org/>
- Good for:
  - image preprocessing
  - camera/video handling
  - classical CV pipelines
  - combining deep learning with engineering workflows

## Fast UI Prototyping

### Gradio

- Main role: fastest way to build and share ML demos
- Official docs: <https://www.gradio.app/docs>
- Good for:
  - simple web apps
  - demos
  - class projects
  - fast prototypes

### Streamlit

- Main role: dashboards and simple Python web apps
- Official docs: <https://docs.streamlit.io/>
- Good for:
  - dashboards
  - data apps
  - quick interfaces

## Backend APIs

### FastAPI

- Main role: Python backend APIs
- Official docs: <https://fastapi.tiangolo.com/>
- Good for:
  - clean backend services
  - AI inference APIs
  - frontend/backend separation

## Reinforcement Learning

### Stable-Baselines3

- Main role: reliable RL algorithm implementations in PyTorch
- Official docs: <https://stable-baselines3.readthedocs.io/en/master/>
- Good for:
  - PPO
  - DQN
  - SAC
  - simple RL experiments

### Gymnasium

- Main role: RL environments and simulation interface
- Docs: <https://gymnasium.farama.org/>
- Good for:
  - creating or using RL environments
  - running control experiments

## Deployment and Optimization

### ONNX Runtime

- Main role: optimized inference across CPU, GPU, NPU, edge, web, and mobile
- Official site: <https://onnxruntime.ai/>
- Good for:
  - deployment
  - performance comparison
  - edge inference
  - model export workflows

## Suggested Simple Stacks

If you want to move fast, pick one of these:

### Vision app

- PyTorch
- Ultralytics YOLO
- OpenCV
- Gradio

### LLM app

- Ollama or Transformers
- Sentence Transformers if search/retrieval is needed
- Gradio or FastAPI

### Audio app

- Transformers or Whisper
- Gradio

### Generative image app

- Diffusers
- Gradio

### RL demo

- Gymnasium
- Stable-Baselines3
- Gradio or a simple script/demo

### Deployment project

- PyTorch
- ONNX Runtime
- FastAPI or Gradio

