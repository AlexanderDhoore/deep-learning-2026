# Domain 1: Computer Vision

Computer vision is one of the clearest and most practical deep-learning domains.

If you like images, video, cameras, inspection, or visual demos, this is a very strong project domain for this course.

It is also one of the best domains if you want to build something that is easy to show and easy to explain during your final presentation.

## What This Domain Is

Computer vision is about using AI on images and video.

That can mean many different tasks:

- image classification
  You give the model one image and ask: what is in this image?
- object detection
  The model finds objects and draws boxes around them.
- segmentation
  The model labels pixels or regions, not just whole objects.
- depth estimation
  The model estimates how far parts of the scene are from the camera.
- keypoint detection or pose estimation
  The model finds important points, such as joints, corners, or landmarks.

So computer vision is not only "recognizing a cat in a photo".
It includes inspection, counting, tracking, measuring, understanding scenes, and building systems that can react to what a camera sees.

## Why You Might Choose It

This is a strong domain for this course for several reasons:

- it is visual and easy to demo
- many pretrained models already exist
- it works well on the GPU hardware you have
- it fits very well with the practical style of this course
- it is an established field, but still extremely powerful in practice
- it solves many real industrial problems very well

Computer vision is also a good choice if you want a project with a clear input and output:

- input: image or video
- model: classifier, detector, segmenter, depth model, or pose model
- output: labels, boxes, masks, scores, counts, or other visual results
- interface: web app, dashboard, API, or edge-device demo

That project structure is very natural and usually leads to a clean final demo.

## Example Applications

You do not need to invent a revolutionary idea.
A small, clear project is usually better than a vague, over-ambitious one.

Good examples include:

- an object detector for a chosen domain
- an image classifier for products, waste, plants, or materials
- a defect-detection demo
- a segmentation app
- a depth-estimation demo
- a keypoint or pose-estimation demo
- a people or object counter
- a simple visual-inspection tool
- a video analysis tool that tracks or counts objects over time

You can also make the project more personal or more industrial depending on your interests.

For example:

- hobby side: sports analysis, pets, collections, fashion, games, media
- practical side: inspection, counting, sorting, monitoring, defect detection
- deployment side: running the model on a local edge device

## Which Technical Paths Fit Best

Computer vision combines very well with several of the course paths.

### Path 1: Train or retrain your own model

This is the most classical computer-vision route.

It fits well if you want to:

- collect or choose a dataset
- train or retrain a model yourself
- understand the training workflow more directly

This path is especially good for:

- classification
- object detection
- segmentation
- simple anomaly-detection style workflows

You do not need to start from random weights.
In practice, you will often start from a pretrained model and continue training it on your own dataset.

### Path 2: Build with pretrained models

This path fits well if you do not want the main challenge to be model training.

Instead, you:

- choose a model that already works
- build an application around it
- focus on user interaction, workflow, and system design

This is a good route for:

- depth estimation
- image captioning style workflows
- quick demos with existing models
- combining vision with another modality or interface

### Path 5: Edge AI and deployment

Computer vision is one of the best domains for edge AI.

That is because vision models are often:

- compact enough to deploy
- easy to benchmark
- easy to visualize
- strongly connected to real-world use cases

So if you like deployment, systems engineering, or embedded hardware, vision is an excellent match.

### Path 3: Fine-tuning or adaptation

This path is possible in vision, but it is usually less central here than in large language models.

For this course, most vision projects will probably be:

- Path 1 if you want to train or retrain
- Path 2 if you want to build around a pretrained model
- Path 5 if you want to focus on deployment

## Recommended Starter Routes

You do not need to understand the entire computer-vision ecosystem before you start.
It is better to choose one route and go deep enough to build something real.

### Route A: Fast practical object detection

This is one of the best starter routes if you want visible results quickly.

Good fit for:

- object detection
- segmentation
- tracking
- pose estimation

Recommended tools:

- Ultralytics YOLO
- OpenCV

Why choose this route:

- very practical
- strong docs
- quick feedback
- good for demos

### Route B: More flexible PyTorch route

This route is good if you want to understand the training workflow more directly.

Good fit for:

- image classification
- transfer learning
- experiments with different architectures
- custom training loops if you want more control

Recommended tools:

- PyTorch
- torchvision
- timm
- OpenCV

Why choose this route:

- more educational
- more flexible
- closer to the general deep-learning workflow

### Route C: Modern detection project

If you specifically want a modern object-detection project, RF-DETR is also a strong option.

Good fit for:

- custom detection datasets
- comparing approaches
- detection-focused projects

Recommended tools:

- RF-DETR
- PyTorch
- OpenCV

Why choose this route:

- strong modern detection workflow
- interesting if you want something a bit different from YOLO

## Which Frameworks to Start With

You do not need all of these.
Pick one main stack.

### PyTorch

Use PyTorch if:

- you want to train or retrain your own model
- you want to understand the general training workflow
- you want flexibility

### torchvision

Use torchvision if:

- you want standard vision models and transforms
- you want a PyTorch-native starting point
- you want baselines for classification, detection, or segmentation

### timm

Use timm if:

- you want access to many pretrained vision architectures
- you want a strong model library on top of PyTorch

### Ultralytics YOLO

Use YOLO if:

- you want a practical path to detection, segmentation, pose, or tracking
- you want fast results
- you want a very demo-friendly workflow

### RF-DETR

Use RF-DETR if:

- you want to focus on modern object detection
- you want an alternative to YOLO
- you want a strong detection-specific project

### OpenCV

Use OpenCV as a support tool if you need:

- image loading
- video loading
- frame processing
- drawing boxes or overlays
- traditional preprocessing around the deep-learning model

OpenCV is usually not the main AI framework.
It is the engineering glue around your vision pipeline.

## Official Docs and Starting Points

Start from the official docs, not random tutorials.

- PyTorch: <https://pytorch.org/>
- torchvision: <https://docs.pytorch.org/vision/main/index.html>
- Ultralytics YOLO: <https://docs.ultralytics.com/>
- RF-DETR: <https://rfdetr.roboflow.com/develop/>
- OpenCV: <https://docs.opencv.org/>

If you choose the more PyTorch-oriented route, start with PyTorch and torchvision.

If you choose detection, start with YOLO or RF-DETR.

If you choose a project with images or video, OpenCV will often still be useful somewhere in the pipeline.

For generic interface or backend tooling, use the top-level support-tooling page instead of this domain note.

## How To Choose a Good Computer-Vision Project

Before you start building, make four decisions:

1. What is the input?
   One image, a folder of images, a webcam, a video file, or a live stream?
2. What is the task?
   Classification, detection, segmentation, counting, depth estimation, or something else?
3. What is the output?
   A label, boxes, masks, a count, a score, an alert, or a processed video?
4. What is the interface?
   A web app, dashboard, API, local script, or edge-device demo?

If you can answer those four questions clearly, your project is probably well scoped.

## Good Advice Before You Begin

- start from a pretrained model
- keep the dataset small and clear
- focus on one main task
- make the output visual
- get a first result working before trying to optimize everything
- do not combine too many hard problems at once

A simple detector with a clean demo is better than a huge project that never becomes stable.

For this course, computer vision is one of the safest and strongest domains if you want a project that feels concrete, technical, and easy to present well.
