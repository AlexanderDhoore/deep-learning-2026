# Strategic Project Paths

This file defines the most important high-level categories for the course.

The key idea is:

students will probably choose a **framework stack first**, and then grow an application idea around it.

So these categories are not only based on application domain.
They are also based on the kind of technical path a student chooses.

## Path 1: Train Your Own Neural Network

This path is for students who want to train or retrain a model in a relatively classical deep-learning workflow.

Important note:

this path can still start from a pretrained model.

For example:

- start from a pretrained MobileNet
- replace the last layer if needed
- continue training the model on your own dataset
- update the normal model weights through standard training

So this path is **not** limited to training from random initialization.
It also includes the common practical workflow of transfer learning where you start from pretrained weights and then retrain the model normally.

Typical areas:

- computer vision
- audio classification
- time-series analysis
- simple custom classifiers

Typical framework stack:

- PyTorch
- torchvision / torchaudio
- timm
- Ultralytics YOLO
- RF-DETR

Good examples:

- train a visual classifier
- fine-tune an object detector
- classify sounds
- detect anomalies in sensor data

Why this path matters:

- it teaches the basic deep-learning workflow directly
- dataset -> model -> training -> evaluation -> deployment

Typical wording to use in class:

- transfer learning
- retraining
- training from pretrained weights
- updating the normal model weights

## Path 2: Build With Pretrained Foundation Models

This path is for students who want to use existing pretrained models instead of training from scratch.

Typical areas:

- LLM applications
- vision-language models
- speech models
- image generation
- multimodal demos

Typical framework stack:

- Hugging Face Transformers
- Diffusers
- Ollama
- Sentence Transformers

Good examples:

- chatbot
- image-question answering app
- speech-to-text tool
- text-to-image tool
- semantic search assistant
- document understanding tool
- recommendation prototype based on embeddings

Why this path matters:

- this is how much modern AI development actually works
- many useful systems are built on top of pretrained models

## Path 3: Fine-Tune or Adapt Pretrained Models

This path sits between Path 1 and Path 2.

The student does not build a model from scratch, but also does more than just call an existing model.

This path is especially important for large foundation models such as:

- large language models
- image generation models
- other very large pretrained systems

In these cases, it is often not practical to retrain the whole model.
Instead, the student adapts only part of it, or adds trainable adapters.

That is the key difference with Path 1.

### Difference between Path 1 and Path 3

Path 1:

- normal training workflow
- often updates the model weights in the usual way
- may start from pretrained weights
- common for CNNs, detectors, audio models, and smaller custom models

Path 3:

- adaptation of a large pretrained foundation model
- often does **not** update the whole model
- usually uses parameter-efficient methods
- common for LLMs and diffusion models

Typical parameter-efficient methods:

- LoRA
- PEFT
- adapters
- DreamBooth-style adaptation

Typical areas:

- LLM fine-tuning
- PEFT / LoRA adaptation
- DreamBooth / LoRA for image models
- domain-specific adaptation

Typical framework stack:

- Transformers training stack
- PEFT / LoRA-style methods
- Diffusers training scripts
- PyTorch

Good examples:

- adapt a small LLM to a narrow task
- fine-tune an image generation model on a style
- adapt a model to a domain-specific dataset

Why this path matters:

- it is one of the most interesting modern engineering paths
- it helps students understand the difference between prompting, inference, and actual model adaptation
- it teaches that "fine-tuning" can mean very different things depending on model scale

## Path 4: Reinforcement Learning and Control

This path is for students who want to build agents that learn through reward and interaction.

Typical framework stack:

- Gymnasium
- Stable-Baselines3
- PyTorch
- TorchRL as an optional PyTorch-native stack

Good examples:

- game-playing agent
- control simulation
- simple RL benchmark comparison

Why this path matters:

- it is a major deep-learning area
- it strongly appeals to students interested in games, robotics, or control

Risk note:

- this path is interesting, but harder to scope well in a short course

## Path 5: Edge AI and Deployment

This path is for students who care most about getting a model to run efficiently on real hardware.

Typical framework stack:

- ONNX Runtime
- NVIDIA Jetson / JetPack
- TensorRT
- Ollama or llama.cpp for local LLM deployment
- PyTorch export workflows

Good examples:

- export and deploy a model on edge hardware
- compare runtimes
- optimize latency
- build an application around an embedded AI model
- deploy a small local LLM on an edge-oriented machine

Why this path matters:

- it fits electronics-ICT very well
- it connects deep learning to real systems engineering
- it teaches that deployment is part of AI, not an afterthought

## Secondary Project Dimensions

After choosing a strategic path, the student can choose an application area:

- computer vision
- language models, text apps, and chat systems
- speech and audio
- multimodal and document AI
- time-series and sensor signals
- semantic search, retrieval, and recommendation

Generative systems are best treated as a cross-cutting theme:

- text generation
- image generation
- audio generation
- multimodal generation

This two-level model is probably the best way to explain the field:

1. choose a technical path
2. choose an application domain

So "generative AI" is not one separate modality next to vision or audio.
It is something that can happen inside several modalities.

## Recommended Default Paths For Most Students

If a student is unsure, these are probably the best default choices:

- Train Your Own Neural Network
- Build With Pretrained Foundation Models
- Edge AI and Deployment

These usually balance feasibility, learning value, and demo quality best.

The "Fine-Tune or Adapt Pretrained Models" path is exciting, but probably best for students who are especially motivated and willing to work with more demanding tooling.
