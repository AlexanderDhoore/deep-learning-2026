# Deep Learning: Broad Overview and Project Directions

This document is meant as the basis for the first 30-minute kickoff talk before students start working on their own project.

The goal of this talk is not to explain every deep-learning technique in depth.

The goal is to answer three practical questions:

1. What kinds of deep-learning systems exist?
2. Which tools and frameworks could I use?
3. Which direction could I choose for my own project?

---

## 1. Start With the Big Picture

Deep learning is not one single thing.

It is a large family of methods based on neural networks, and it appears in many forms:

- image recognition
- object detection
- speech recognition
- large language models
- image generation
- multimodal systems
- time-series prediction
- robotics and control

So when we say "deep learning", we are really talking about a **whole toolbox**.

For this course, the important question is:

> Which part of that toolbox do you want to use to build something interesting?

---

## 2. The Goal of the Project

You are not expected to become a deep-learning researcher in a few weeks.

You are expected to:

- choose a direction
- learn a framework or model stack
- build a working application
- understand the code, architecture, and choices you made

So the project is not only about "using AI".
It is about **learning how to build with AI**.

That means:

- frontend + backend is fine
- Python will probably be the easiest language
- using AI assistants is allowed
- but at the exam, you must be able to explain what your code does

---

## 3. First Choose a Technical Path

Before choosing a detailed project idea, it is often easier to choose a **technical path**.

For this course, the main paths are:

- train your own neural network
- build with pretrained foundation models
- fine-tune or adapt pretrained models
- reinforcement learning
- edge AI and deployment

That is often a better starting point than asking:

> "What app should I build?"

Because in practice, many students will first choose a framework they want to explore, and then invent a project around it.

See also:

- [`01-strategic-project-paths.md`](01-strategic-project-paths.md)

One important distinction:

- in classical deep learning, you may start from a pretrained model such as MobileNet and still retrain the model in the usual way
- in modern foundation-model work, "fine-tuning" often means adapting only part of a very large model with methods like LoRA or PEFT

So not every use of pretrained weights belongs in the same bucket.

## 4. Then Choose an Application Direction

After that, choose the application area where you want to apply that path.

Below is a practical map of application directions.

These are not rigid categories.
They overlap.
But they help you imagine possible projects.

### Direction 1: Computer Vision

This is about using AI on images or video.

Typical tasks:

- image classification
- object detection
- segmentation
- pose estimation
- visual inspection
- counting objects

Typical examples:

- detect items on a photo
- classify waste or products
- inspect defects
- count people or objects in a camera feed
- track movement in a video

Good tools:

- PyTorch
- torchvision / timm
- Ultralytics YOLO
- OpenCV

Why it is a good student direction:

- visual output
- easy to demo
- many pretrained models exist
- easy to build a web app around it

### Direction 2: Language Models, Text Apps, and Chat Systems

This is about text-based AI systems.

Typical tasks:

- chatbots
- question answering
- summarization
- classification
- rewriting
- information extraction
- tool calling

Typical examples:

- a study assistant
- an email helper
- a chatbot for a specific topic
- a document question-answering app
- an AI assistant that uses external tools

Good tools:

- Ollama
- Hugging Face Transformers
- Sentence Transformers
- Gradio or FastAPI

Why it is a good student direction:

- students already saw some of this in the generative AI workshop
- easy to prototype quickly
- easy to connect to a frontend

### Direction 3: Speech and Audio AI

This is about systems that listen to audio or generate audio.

Typical tasks:

- speech-to-text
- text-to-speech
- speaker recognition
- sound classification
- audio generation

Typical examples:

- a voice note transcriber
- a speech-based chatbot
- a sound-event detector
- a text-to-speech assistant

Good tools:

- Whisper
- Kokoro or another TTS library
- Hugging Face Transformers
- Gradio

Why it is a good student direction:

- very interactive
- easy to combine with LLMs
- good for multimodal demos

### Direction 4: Multimodal AI and Document AI

This is about combining multiple input or output types:

- text + image
- text + audio
- image + language
- video + language

Typical tasks:

- visual question answering
- image captioning
- document understanding
- OCR-enhanced document workflows
- audio-aware assistants
- systems that combine speech, vision, and text

Typical examples:

- upload an image and ask questions about it
- analyze a receipt or document
- combine voice input with image understanding
- build a document question-answering tool

Good tools:

- Hugging Face Transformers
- Ollama vision-capable models
- Gradio

Why it is a good student direction:

- feels modern
- shows that deep learning is broader than just chatbots
- often creates strong demos

### Direction 5: Time-Series and Sensor Signals

This is about signals measured over time.

Typical tasks:

- forecasting
- anomaly detection
- condition monitoring
- classification of sensor signals
- predictive maintenance

Typical examples:

- detect anomalies in machine data
- classify patterns in sensor measurements
- predict future values of a signal
- monitor process data from an industrial system

Good tools:

- PyTorch
- tsai, NeuralForecast, or other time-series libraries
- pandas / polars for preprocessing
- Gradio / Streamlit / FastAPI for interfaces

Why it is a good student direction:

- relevant to industrial applications, but not limited to industry
- good fit with electronics/ICT
- does not need flashy graphics to be meaningful

### Direction 6: Semantic Search, Retrieval, and Recommendation

This is about turning data into embeddings and then using those embeddings to search, retrieve, rank, or recommend.

Typical tasks:

- semantic search
- retrieval-augmented generation
- recommendation
- similarity matching
- nearest-neighbor search

Typical examples:

- search through notes or documents by meaning
- recommend songs, products, or media
- build a chatbot that first retrieves relevant context
- find similar images, texts, or items

Good tools:

- Sentence Transformers
- Transformers
- vector databases or plain vector search libraries
- Gradio / Streamlit / FastAPI

Why it is a good student direction:

- very practical
- highly relevant in modern AI products
- easier to scope than many full fine-tuning projects

### Direction 7: Reinforcement Learning and Control

This is about learning by interaction and reward.

Typical tasks:

- game playing
- robot control
- decision making
- control policies

Typical examples:

- train an agent in a simulation
- compare policies on a small control task
- build an interactive RL demo

Good tools:

- Gymnasium
- Stable-Baselines3
- TorchRL
- PyTorch

Why it is a possible student direction:

- conceptually interesting
- good for students who like control or simulation

Why it is riskier:

- harder to explain well in a short time
- can be less predictable than other directions
- often more difficult to finish cleanly

### Direction 8: Edge AI and Deployment

This is about making models run efficiently on real hardware.

Typical tasks:

- exporting models
- optimizing inference
- quantization
- ONNX deployment
- deploying on embedded or edge hardware

Typical examples:

- deploy a small model on an edge device
- compare CPU vs GPU vs optimized runtime
- build a small web service around an optimized model
- run a small local LLM on an edge-oriented machine

Good tools:

- ONNX Runtime
- Ollama or llama.cpp
- JetPack / TensorRT on NVIDIA edge hardware
- PyTorch export flows
- Ultralytics export tools
- Docker

Why it is a good student direction:

- very relevant for electronics/ICT students
- strong engineering value
- good fit with real systems thinking

## 5. Cross-Cutting Theme: Generative Systems

Generative AI is important, but it does not fit neatly as one single application domain next to vision or audio.

It cuts across several areas:

- language generation
- image generation
- speech generation
- music generation
- multimodal generation

So instead of treating it as one separate modality, it is better to explain it as a **style of model behavior** that can appear in several domains.

---

## 6. Which Frameworks Matter Most?

Students do not need to learn every framework.

For this course, the main **AI frameworks** worth pointing students toward are:

- **PyTorch** as the core deep-learning framework
- **torchvision** and **torchaudio** for domain-specific PyTorch work
- **Ultralytics YOLO** and **RF-DETR** for practical vision projects
- **Hugging Face Transformers** for text, multimodal, and pretrained model work
- **Diffusers** for image generation and adaptation
- **Sentence Transformers** for embeddings and semantic search
- **Stable-Baselines3** as the most student-friendly RL default
- **TorchRL** as an optional PyTorch-native RL stack
- **ONNX Runtime**, **Jetson/JetPack**, **TensorRT**, and optionally **Ollama / llama.cpp** for deployment

Supporting tools such as **Gradio**, **Streamlit**, and **FastAPI** are useful, but they are not the main AI frameworks.
They are optional support layers around the AI system.

For the students, a good mental model is:

- `PyTorch` when you want to train or retrain a model more directly
- `Transformers` / `Diffusers` when you want to build with or adapt large pretrained foundation models
- `Sentence Transformers` when you want embeddings, retrieval, or recommendation
- `Stable-Baselines3` when you want the easiest RL starting point

---

## 7. Advice for Choosing a Project

Choose a project that is:

- interesting to you
- small enough to finish
- large enough to show real work
- easy to demo
- understandable by you

Good choices usually have:

- one clear user problem
- one clear AI component
- one interface
- one or two strong technical challenges

Bad choices are often:

- too big
- too vague
- too research-heavy
- too dependent on collecting a huge custom dataset
- too ambitious in both model complexity and deployment complexity at the same time

---

## 8. Good Project Formula

A strong student project often looks like this:

> Input -> AI model -> useful output -> user interface

Examples:

- image -> detector -> labels/boxes -> web app
- speech -> transcription -> text summary -> web app
- prompt -> image generator -> generated images -> gallery UI
- sensor data -> anomaly detector -> warning/dashboard -> web interface
- user question + document -> LLM/retrieval -> answer -> chat UI
- item embeddings -> similarity ranking -> recommendation UI

---

## 9. What I Expect at the Exam

At the exam, I do not only care whether your project "works".

I care whether you understand:

- what problem you chose
- which model or framework you used
- how your code is structured
- what your inputs and outputs are
- what your main design choices were
- what limitations your system has

You may use AI tools while building.
But at the exam, **you** must understand the result.

---

## 10. Simple Recommendation to Students

If you are unsure, start with one of these:

- a computer vision app based on YOLO or RF-DETR
- an LLM tool app based on Transformers or Ollama
- a speech-to-text or text-to-speech app
- a multimodal app
- a semantic search or recommendation app based on embeddings
- an edge/deployment project using ONNX Runtime or Jetson

These directions are usually easier to scope and demo than reinforcement learning.

---

## 11. Final Message

Deep learning is a wide field.

You do not need to master all of it in this course.
But you should leave this course with:

- a better overview of the landscape
- experience building one real system
- confidence that you can learn new AI tools on your own

That is the real goal.
