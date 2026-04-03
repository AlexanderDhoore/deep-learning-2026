# Deep Learning: Broad Overview and Project Domains

Use this document as a practical overview before you start working on your project.

The goal of this talk is not to explain every deep-learning technique in depth.

The goal is to answer three practical questions:

1. What kinds of deep-learning systems exist?
2. Which tools and frameworks could I use?
3. Which domain could I choose for my own project?

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

- choose a domain
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

Because in practice, you may first choose a framework you want to explore, and then invent a project around it.

See also:

- [`01-strategic-project-paths.md`](01-strategic-project-paths.md)

### Quick explanation of the five paths

#### Path 1: Train or retrain your own model

This is the classical workflow:

- data
- model
- training
- evaluation
- deployment

You can still start from pretrained weights.
For example, you can take MobileNet or YOLO and continue training it on your own dataset.

Good fit if you want to understand how model training really works.

#### Path 2: Build with pretrained foundation models

Here, you mostly use a model that already exists and build an application around it.

That means:

- less focus on training
- more focus on system design
- more focus on integrating models into a useful tool

This is very close to what you already touched in the generative AI workshop.
If you need inspiration, Hugging Face is one of the best places to explore models and tasks.

#### Path 3: Fine-tune or adapt large models

This path sits between Path 1 and Path 2.

You are not training everything from scratch, but you are also doing more than simple inference.

For very large models, it is often too expensive to retrain the whole model.
So instead, you adapt part of it with methods such as:

- LoRA
- PEFT
- adapters

A concrete example is fine-tuning an image model on your own face or style.

#### Path 4: Reinforcement learning

This path is very different from normal supervised learning.

Instead of learning only from labeled examples, the model:

- interacts with an environment
- tries actions
- receives rewards
- improves over time

This is why reinforcement learning is strongly connected to games, simulations, robotics, and control.

#### Path 5: Edge AI and deployment

Many projects in this course will run on your GPU server.

This path is about running a model somewhere else:

- on your laptop
- on a Jetson
- on a Raspberry Pi
- on another embedded or edge device

Here the challenge is often export, optimization, latency, and runtime choice rather than training a brand-new model.

## 4. Then Choose an Application Domain

After that, choose the application domain where you want to apply that path.

Below is a practical map of application domains.

These domains help you imagine possible projects.

The key idea is simple:

- the technical path tells you **how** you work with models
- the application domain tells you **what kind of data or problem** you work on

One domain can combine with several technical paths.
For example:

- computer vision can use your own trained model, a pretrained model, or edge deployment
- language models usually fit Path 2 or Path 3
- audio can fit Path 1, Path 2, or Path 3

### Domain 1: Computer Vision

This is about using AI on images or video.

Typical tasks:

- image classification
- object detection
- segmentation
- depth estimation
- keypoint detection
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
- RF-DETR
- OpenCV

Why this is a good domain:

- visual output
- easy to demo
- many pretrained models exist
- easy to build a web app around it
- it is an established field, but still extremely powerful
- it solves many real industrial problems very well

### Domain 2: Language Models and Text Systems

This is about text-based AI systems.

Typical tasks:

- chatbots
- question answering
- summarization
- classification
- rewriting
- information extraction
- tool calling
- text ranking

Typical examples:

- a study assistant
- an email helper
- a chatbot for a specific topic
- a document question-answering app
- an AI assistant that uses external tools
- a tool-calling assistant that searches, summarizes, or automates steps for the user

Good tools:

- Ollama
- Hugging Face Transformers
- Sentence Transformers
- Gradio or FastAPI

Why this is a good domain:

- you already saw some of this in the generative AI workshop
- easy to prototype quickly
- easy to connect to a frontend

Important note:

- this domain usually uses pretrained models or fine-tuned models
- training your own language model from scratch is usually not realistic
- so this domain fits especially well with Path 2 and Path 3

Tool calling is especially powerful here:

- the model does not only generate text
- it can also decide when to call a tool
- for example: search, calculator, database lookup, or another API
- that can become a whole project by itself

### Domain 3: Multimodal and Document AI

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
- docTR
- Gradio

Why this is a good domain:

- feels modern
- shows that deep learning is broader than just chatbots
- often creates strong demos
- you already saw a small example of this in the generative AI workshop

### Domain 4: Semantic Search and Retrieval

This domain is based on embeddings.

An embedding is a vector representation of data such as:

- text
- image
- audio

The key idea is that items with similar meaning end up close together in vector space.

That makes it possible to:

- search by meaning, not only by exact words
- retrieve relevant context
- find similar items

Typical tasks:

- semantic search
- retrieval-augmented generation
- similarity matching
- nearest-neighbor search

Typical examples:

- search through notes or documents by meaning
- build a chatbot that first retrieves relevant context
- find similar images, texts, or items
- search through a knowledge base or course archive

Good tools:

- Sentence Transformers
- Transformers
- vector databases or plain vector search libraries
- Gradio / Streamlit / FastAPI

Why this is a good domain:

- very practical
- highly relevant in modern AI products
- easier to scope than many full fine-tuning projects

RAG is part of this domain:

- first retrieve relevant context from documents
- then pass that context to a language model
- then generate the answer with better grounding

### Domain 5: Recommendation Systems

This is about using embeddings, ranking, or preference signals to suggest useful items to a user.

Typical tasks:

- content-based recommendation
- similarity-based recommendation
- ranking
- personalized suggestions

Typical examples:

- recommend songs, products, or media
- build a movie or music recommender
- suggest similar articles, images, or products
- create a recommendation tool around a small curated dataset

Good tools:

- Sentence Transformers
- PyTorch for custom ranking experiments
- vector databases or plain vector search libraries
- Gradio / Streamlit / FastAPI

Why this is a good domain:

- it is different from search, even if both often use embeddings
- it is a very realistic product-oriented AI domain
- it can lead to a strong demo with a clear user experience

### Domain 6: Speech and Audio

This is about systems that listen to audio or generate audio.

Typical tasks:

- speech-to-text
- text-to-speech
- speaker recognition
- sound classification
- audio generation
- music generation
- audio-to-audio transformation

Typical examples:

- a voice note transcriber
- a speech-based chatbot
- a sound-event detector
- a text-to-speech assistant
- a music generation demo
- a system that speaks in a customized voice

Good tools:

- Whisper
- Kokoro or another TTS library
- Hugging Face Transformers
- torchaudio
- Gradio

Why this is a good domain:

- very interactive
- easy to combine with LLMs
- good for multimodal demos

This domain can use several technical paths:

- Path 1 if you want to train or retrain your own audio model
- Path 2 if you want to use pretrained speech or music models
- Path 3 if you want to adapt a model to a specific voice or style

### Domain 7: Time-Series and Sensor Signals

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

Why this is a possible domain:

- relevant to industrial applications, but not limited to industry
- good fit with electronics/ICT
- does not need flashy graphics to be meaningful
- it can be strong if you already have an interesting dataset

This domain is probably less immediately attractive than images, text, or audio for this course, but it is still valuable, especially if you want something more industrial.

### Domain 8: 3D, Depth, and Geometry

This is a more niche domain, but it is worth mentioning.

Typical tasks:

- depth estimation
- image-to-3D
- text-to-3D
- 3D representation learning
- point-cloud or geometry-related workflows

Typical examples:

- estimate scene depth from an image
- generate a 3D object from an image or prompt
- build a workflow around 3D model generation
- explore point-cloud style outputs

Good tools:

- Hugging Face models for depth or 3D tasks
- PyTorch
- Gradio or a custom visualization frontend

Why this is interesting:

- it shows that the field is broader than the most common demos
- some very interesting pretrained models already exist here

## 5. Technical Paths and Application Domains Work Together

The paths and the domains are not competing systems.
They combine.

Examples:

- computer vision + Path 1: train a detector on your own dataset
- computer vision + Path 5: deploy a vision model to edge hardware
- language models + Path 2: build a chatbot with a pretrained model
- language models + Path 3: adapt a model with LoRA
- speech + Path 3: adapt a model to a specific voice
- multimodal + Path 2: use a vision-language model

If you want a generative project, choose the domain that best matches what you want to build:

- language models for text generation and assistants
- computer vision or multimodal systems for image workflows
- speech and audio for voice or music workflows

Then use the frameworks page to find the right tooling.

---

## 6. Which Frameworks Matter Most?

You do not need to learn every framework.

The exact framework depends strongly on the domain you choose.

For the whole course, the most important big names to remember are:

- **PyTorch** for training or retraining models
- **Transformers** for pretrained language, multimodal, and speech models
- **Sentence Transformers** for embeddings, search, retrieval, and recommendation

Then the domain-specific notes can guide you further:

- vision may lead you to YOLO or RF-DETR
- image generation may lead you to Diffusers
- reinforcement learning may lead you to Stable-Baselines3
- deployment may lead you to ONNX Runtime or Jetson tools

So you do not need to memorize the whole framework landscape from this talk.
Choose your domain first, then study the matching tools in more detail.

Supporting tools such as **Gradio**, **Streamlit**, **FastAPI**, and even a custom **React** frontend are useful, but they are not the main AI frameworks.
They are optional support layers around the AI system.

A good mental model is:

- `PyTorch` when you want to train or retrain a model more directly
- `Transformers` / `Diffusers` when you want to build with or adapt large pretrained foundation models
- `Sentence Transformers` when you want embeddings, search, retrieval, or recommendation
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

A strong project often looks like this:

> Input -> AI model -> useful output -> user interface

Examples:

- image -> detector -> labels/boxes -> web app
- speech -> transcription -> text summary -> web app
- prompt -> image generator -> generated images -> gallery UI
- sensor data -> anomaly detector -> warning/dashboard -> web interface
- user question + document -> LLM/retrieval -> answer -> chat UI
- item embeddings -> similarity ranking -> recommendation UI

---

## 9. What You Should Be Ready to Explain at the Exam

At the exam, you should be ready to explain:

- what problem you chose
- which model or framework you used
- how your code is structured
- what your inputs and outputs are
- what your main design choices were
- what limitations your system has

You may use AI tools while building.
But at the exam, **you** must understand the result.

---

## 10. Final Message

Deep learning is a wide field.

You do not need to master all of it in this course.
But you should leave this course with:

- a better overview of the landscape
- experience building one real system
- confidence that you can learn new AI tools on your own

That is the real goal.
