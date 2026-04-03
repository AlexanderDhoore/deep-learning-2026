# Domain 8: 3D, Depth, and Geometry

This is a more niche domain, but it is real and worth mentioning.

If you like spatial reasoning, 3D content, geometry, reconstruction, or unusual AI demos, this can be a very interesting project direction.

It is not the safest default for this course, but it can become a memorable and technically interesting project if you keep the scope small.

## What This Domain Is

This domain is about systems that do more than recognize what is in an image.

Instead, they try to understand something about:

- depth
- geometry
- 3D structure
- spatial layout

That can include tasks such as:

- depth estimation
- image-to-3D workflows
- text-to-3D workflows
- geometry-aware models
- point-cloud style outputs

So instead of asking:

> What object is this?

you may ask:

> How far away is it?
> What is the 3D structure?
> Can I turn this image or prompt into a 3D object?

This is why the domain feels different from normal computer vision.
It is more about spatial understanding and 3D representation than about classification or detection.

## Why You Might Choose It

This can be a strong domain for the course if:

- you want something more unusual
- you want a project that stands out
- you are interested in geometry, 3D assets, or spatial understanding
- you like exploring newer pretrained-model workflows

It is also interesting because it shows that deep learning is broader than the most common demos.

At the same time, this domain is more niche and often more experimental.
That means it is usually strongest when you:

- use pretrained models
- choose one narrow workflow
- focus on a clean demo instead of a huge system

## Example Applications

Good project ideas include:

- estimate scene depth from an image
- generate a 3D object from an image
- generate a 3D object from a text prompt
- build a small workflow around 3D model generation
- compare a few depth-estimation models
- build an interface that turns images into spatial outputs

You can shape the domain in different ways:

- depth-first route
  Start from images and estimate depth maps.
- image-to-3D route
  Turn an image into a 3D output or asset.
- text-to-3D route
  Start from prompts and generate 3D content.

The strongest student projects here usually choose one of those three and keep the workflow simple.

## Which Technical Paths Fit Best

### Path 2: Build with pretrained models

This is the most natural route for this domain.

It fits well if you want to:

- use existing models
- build a demo or workflow around them
- focus on the application and interface

This is especially strong for:

- depth estimation
- image-to-3D
- text-to-3D

### Path 3: Adapt a model or workflow

This path is possible, but it is more ambitious.

It fits if you want to:

- adapt part of a workflow
- experiment with a more specialized model setup
- go beyond plain inference

For this course, that is possible, but it should be treated as an advanced option.

### Path 1: Train your own model

This is usually not the best starting point here in a short course.

The field is broad, the data can become complicated, and the workflows are often already quite specialized.

So for most projects in this domain, the strongest route is:

- pick a pretrained model
- build a clean demo
- explain the workflow well

## Recommended Starter Routes

You do not need to solve full 3D reconstruction.
Pick one narrow workflow and make it work clearly.

### Route A: Depth estimation demo

This is the safest and strongest starter route in this domain.

Good fit for:

- image depth estimation
- scene understanding
- comparing depth outputs
- building an interface around depth maps

Recommended tools:

- Hugging Face Transformers
- a depth-estimation model

Why choose this route:

- easiest to understand
- easiest to demo
- clearly connected to a real task

This is probably the best first route if you want to explore the domain without making the project too risky.

### Route B: Image-to-3D workflow

This route is interesting if you want a more creative or visual project.

Good fit for:

- turning an image into a 3D asset
- visual experimentation
- unusual demos

Recommended tools:

- Hugging Face model ecosystem
- a model or workflow that supports image-to-3D

Why choose this route:

- memorable demo
- visually interesting
- feels more unusual than standard AI projects

### Route C: Text-to-3D workflow

This route is the most experimental of the three.

Good fit for:

- prompt-to-3D exploration
- creative AI experiments
- projects that produce 3D output assets

Recommended tools:

- Hugging Face task ecosystem
- a pretrained text-to-3D workflow

Why choose this route:

- very novel
- very creative
- can become a striking final demo

It is also riskier, so it is best if you keep the project small and focused.

## Which Frameworks to Start With

You do not need many tools here.
Pick one clear workflow.

### Hugging Face model ecosystem

Use the Hugging Face model ecosystem if:

- you want to explore available models
- you want to try depth or 3D tasks with pretrained systems
- you want an easy place to look for supported workflows

This is the most practical starting point for this domain.

### Hugging Face Transformers

Use Transformers if:

- your project focuses on depth estimation
- you want an official inference path for supported models
- you want a more standard Python workflow

Depth estimation is one of the clearest supported tasks here.

### PyTorch

Use PyTorch if:

- you need lower-level control
- you want to integrate a model into a custom pipeline
- you want to do more than a basic interface

For many student projects in this domain, PyTorch is supportive rather than the main story.

## Official Docs and Starting Points

Start from the official docs and task pages, not random short tutorials.

- Hugging Face models: <https://huggingface.co/models>
- Hugging Face tasks: <https://huggingface.co/tasks>
- Hugging Face depth estimation task: <https://huggingface.co/tasks/depth-estimation>
- Hugging Face text-to-3D task: <https://huggingface.co/tasks/text-to-3d>
- Hugging Face monocular depth estimation guide: <https://huggingface.co/docs/transformers/main/tasks/monocular_depth_estimation>
- PyTorch: <https://pytorch.org/>

If you want the safest route, start with depth estimation.

If you want a more experimental route, explore image-to-3D or text-to-3D models on Hugging Face first and make sure you can run one example before designing the rest of the application.

For generic interface or visualization tooling, use the top-level frameworks page instead of this domain note.

## How To Choose a Good 3D or Geometry Project

Before you start building, answer these questions:

1. What is the input?
   Image, prompt, or another visual source?
2. What is the output?
   Depth map, 3D asset, geometry representation, or visualization?
3. What is the user interaction?
   Upload image, enter prompt, compare outputs, or inspect generated results?
4. Is the project really about geometry, or would a vision project be simpler?

That last question is important.

Sometimes a student wants this domain because it sounds exciting, but the real project idea might fit computer vision better.

That is okay.
Choose this domain only if the spatial or 3D part is truly central to the idea.

## Good Advice Before You Begin

- keep the scope small
- focus on one clear input/output workflow
- prefer pretrained models over ambitious custom training
- make sure the output can be visualized clearly
- test one model end-to-end before building extra features
- treat this as a niche direction, not the default safe option

This domain can lead to one of the most unusual and memorable projects in the course, but only if you keep it narrow enough to stay stable.

For this course, depth estimation is probably the safest entry point, while text-to-3D and image-to-3D are more experimental but potentially more striking.
