# Edge AI and Deployment

This note is for students who are interested in the deployment path rather than mainly the model-training path.

Edge AI is not really a separate application domain like vision, language, or audio.
It is a technical path.

That means the central question is not:

> What kind of data do I work on?

but:

> Where does the model run, and how do I make it run well there?

## What This Path Is

Many projects in this course will run on your GPU server.

The edge deployment path is about running a model somewhere else, such as:

- on your laptop
- on a Jetson
- on a Raspberry Pi
- on another embedded or edge device
- on a smaller local machine instead of a large server

In this path, the challenge is often not training a brand-new model.
The challenge is:

- exporting the model
- choosing the runtime
- measuring latency
- fitting within hardware limits
- building a useful demo around the deployed system

So this path is often more about systems engineering than about training theory.

## Why You Might Choose It

This is a strong path for the course if you like:

- embedded systems
- optimization
- real hardware
- performance engineering
- deployment more than model training

It is also a very good fit with electronics-ICT.

This path is especially strong if you want your project to answer questions like:

- Can I run this model locally?
- Can I make it faster?
- Can I deploy it on edge hardware?
- What runtime works best?
- What tradeoffs appear on smaller devices?

That makes it a very realistic engineering direction.

## What Kinds of Projects Fit Here

Good project ideas include:

- deploy a pretrained model with ONNX Runtime
- compare inference on different runtimes
- optimize a model for edge deployment
- build a small app around an optimized model
- deploy a small local LLM with Ollama
- export a vision model and test it on edge hardware
- compare server inference and local inference

This path fits especially well with:

- computer vision
- local LLM serving
- smaller multimodal workflows
- signal-processing or monitoring systems on hardware

The strongest projects usually choose one model that already works and treat deployment itself as the main technical challenge.

## Typical Technical Workflow

A typical project in this path may look like:

1. choose a model that already works
2. run it normally first
3. export or convert it if needed
4. choose a runtime
5. deploy it on the target device
6. measure latency, memory use, and usability
7. build a small interface or demo around it

That is already a very valid project.

You do not need to both:

- train the hardest possible model
- and do the hardest possible deployment

at the same time.

In fact, for this course, that is usually a bad idea.

## Which Domains Combine Well With This Path

Edge deployment is not its own application domain.
It combines with other domains.

Strong combinations include:

- computer vision + edge deployment
- language models + local deployment
- speech/audio + local inference
- time-series monitoring + device deployment

The simplest and strongest combination is often:

- pick a model from another domain
- make it run well on smaller or local hardware

## Recommended Starter Routes

### Route A: Vision model on edge hardware

This is one of the safest and strongest edge routes.

Good fit for:

- object detection
- segmentation
- small vision workflows

Recommended tools:

- PyTorch export workflow
- ONNX Runtime
- Ultralytics export tools
- Jetson / JetPack if using NVIDIA hardware

Why choose this route:

- very visual
- easy to benchmark
- easy to demonstrate
- strong real-world relevance

### Route B: Local LLM deployment

This route is good if you care more about serving and runtime than training.

Good fit for:

- local assistant apps
- comparing model sizes
- testing local inference performance

Recommended tools:

- Ollama
- llama.cpp
- FastAPI or Gradio

Why choose this route:

- practical
- modern
- easy to connect to a frontend

### Route C: Runtime comparison project

This route is strong if you want a more engineering-focused project.

Good fit for:

- comparing ONNX Runtime and other runtimes
- measuring latency
- studying deployment tradeoffs

Recommended tools:

- ONNX Runtime
- TensorRT if using NVIDIA hardware
- simple benchmark scripts
- FastAPI or Gradio for the demo layer

Why choose this route:

- very systems-oriented
- easy to explain in terms of tradeoffs
- strong if you like optimization

## Which Tools to Start With

### ONNX Runtime

Use ONNX Runtime if:

- you want a common deployment runtime
- you want cross-platform inference
- you want to compare deployment behavior

This is one of the most important tools in this path.

### NVIDIA Jetson / JetPack

Use Jetson and JetPack if:

- you want GPU-accelerated edge deployment on NVIDIA hardware
- you want a real embedded AI workflow
- your project focuses on deployment to Jetson devices

### TensorRT

Use TensorRT if:

- you want optimized inference on NVIDIA GPUs
- you care about latency and performance
- you want to study deployment optimization more deeply

### Ollama

Use Ollama if:

- you want a very practical route for local LLM deployment
- you want model serving to be simple
- you want to focus on the deployed application rather than model internals

### llama.cpp

Use llama.cpp if:

- you want another local LLM inference path
- you care about efficient local serving
- you want to explore runtime tradeoffs

### Docker

Use Docker if:

- you want a cleaner deployment workflow
- you want reproducible serving
- you want to package the application around the model

## Official Docs and Starting Points

Start from the official docs, not random short tutorials.

- ONNX Runtime: <https://onnxruntime.ai/>
- NVIDIA JetPack overview: <https://developer.nvidia.com/embedded/jetpack>
- NVIDIA JetPack install and setup: <https://docs.nvidia.com/jetson/jetpack/install-setup/index.html>
- NVIDIA TensorRT docs: <https://docs.nvidia.com/deeplearning/tensorrt/10.11.0/_static/python-api/gettingStarted.html>
- Ollama: <https://ollama.com/>
- llama.cpp: <https://github.com/ggml-org/llama.cpp>
- Docker docs: <https://docs.docker.com/>

If you want the safest edge project, start with a vision model or a small local LLM that already works.

If you want the strongest systems story, measure performance clearly and explain the deployment tradeoffs well.

## How To Choose a Good Edge Deployment Project

Before you start building, answer these questions:

1. What model are you deploying?
   Vision, language, audio, time-series, or something else?
2. Where will it run?
   GPU server, laptop, Jetson, Raspberry Pi, or another device?
3. What is the technical challenge?
   Export, runtime choice, latency, memory use, packaging, or hardware integration?
4. What will the final demo show?
   A benchmark, an application, a local assistant, a vision demo, or a device workflow?

If those answers are clear, the project is probably well scoped.

## Good Advice Before You Begin

- start with a model that already works
- treat export and deployment as the technical challenge
- keep the demo simple and measurable
- do not combine this with the hardest possible training path
- benchmark something concrete
- make the deployment tradeoff easy to explain

A clean deployment demo with good measurements is usually stronger than a very ambitious project that tries to redesign the whole model as well.

For this course, this is one of the strongest paths if you like systems engineering and want a project that connects AI to real hardware and real deployment constraints.
