# Frameworks and Official Docs

This page is a practical starting point for students who need to learn a tool quickly.

The idea is simple:

- choose one main direction
- choose one main model/framework stack
- start from the official docs
- build something small first

## Main AI Frameworks

### PyTorch

- Main role: general deep-learning framework
- Good for: almost everything
- Official site: <https://pytorch.org/>
- Why it matters: this is the most important base framework to know in this course

### torchvision

- Main role: PyTorch domain library for computer vision
- Official docs: <https://docs.pytorch.org/vision/main/index.html>
- Good for:
  - datasets
  - pretrained vision models
  - transforms
  - detection / segmentation / classification baselines

### torchaudio

- Main role: PyTorch domain library for audio
- Official docs: <https://docs.pytorch.org/audio/main/index.html>
- Good for:
  - audio preprocessing
  - speech pipelines
  - audio deep-learning experiments

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

### Fine-tuning and adaptation

- Transformers fine-tuning docs: <https://huggingface.co/docs/transformers/training>
- Transformers PEFT/adapters docs: <https://huggingface.co/docs/transformers/en/peft>
- Diffusers training overview: <https://huggingface.co/docs/diffusers/training/overview>
- Diffusers text-to-image fine-tuning example: <https://huggingface.co/docs/diffusers/training/text2image>
- Why it matters:
  - students can go beyond inference
  - fine-tuning or adaptation is a valid project category in this course

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

### RF-DETR

- Main role: practical object detection / segmentation with a strong fine-tuning story
- Official docs: <https://rfdetr.roboflow.com/develop/>
- Official repo: <https://github.com/roboflow/rf-detr>
- Good for:
  - modern detection projects
  - fine-tuning on custom data
  - comparing against YOLO-style workflows

### OpenCV

- Main role: classic computer vision and image/video preprocessing
- Official docs: <https://docs.opencv.org/>
- Good for:
  - image preprocessing
  - camera/video handling
  - classical CV pipelines
  - combining deep learning with engineering workflows

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

## Edge AI and Deployment

### ONNX Runtime

- Main role: optimized inference across CPU, GPU, NPU, edge, web, and mobile
- Official site: <https://onnxruntime.ai/>
- Good for:
  - deployment
  - performance comparison
  - edge inference
  - model export workflows

### NVIDIA JetPack / Jetson

- Main role: official software stack for NVIDIA Jetson edge devices
- Official overview: <https://developer.nvidia.com/embedded/jetpack>
- Install/setup docs: <https://docs.nvidia.com/jetson/jetpack/install-setup/index.html>
- Good for:
  - GPU-accelerated edge deployment
  - deploying AI on NVIDIA embedded hardware

### NVIDIA TensorRT

- Main role: optimized inference on NVIDIA GPUs
- Official docs: <https://docs.nvidia.com/deeplearning/tensorrt/10.11.0/_static/python-api/gettingStarted.html>
- Good for:
  - inference optimization
  - lower latency deployment
  - optimized GPU serving

## Optional Supporting Frameworks

These are useful, but they are not the main AI choice.
They support the application around the model.

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

## Suggested Simple Stacks

If you want to move fast, pick one of these:

### Vision app

- PyTorch
- Ultralytics YOLO or RF-DETR
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
- Jetson/JetPack if using NVIDIA edge hardware
- FastAPI or Gradio
