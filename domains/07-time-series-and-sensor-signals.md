# Domain 7: Time-Series and Sensor Signals

This domain is about data measured over time.

If you like sensors, devices, monitoring, forecasting, industrial systems, or signal-based problems, this is a very strong direction for a project.

It is less flashy than image, audio, or chatbot projects, but it can be extremely meaningful and technically strong, especially in an electronics-ICT context.

## What This Domain Is

A time series is a sequence of values measured over time.

That can include:

- temperatures
- voltages
- pressures
- machine signals
- wearable signals
- power measurements
- traffic or usage data
- any other changing signal over time

This domain is about building systems that can learn patterns in those signals.

Typical tasks include:

- forecasting
- anomaly detection
- sensor monitoring
- condition monitoring
- classification of signals over time
- predictive maintenance

A useful way to think about this domain is:

> What signal do I observe over time, and what useful decision or warning should the system produce?

That makes it a very practical domain, even if the result is not as visually dramatic as in computer vision.

## Why You Might Choose It

This is a strong domain for this course for several reasons:

- it is highly relevant to industrial AI
- it fits electronics-ICT very well
- it can be very meaningful even without flashy visuals
- it is a good choice if you already have an interesting dataset
- it connects naturally to monitoring, prediction, and real-world systems

This domain is especially good if you care about:

- engineering usefulness
- meaningful warnings or predictions
- systems that support decisions
- device and signal data

It is also a good domain if you already have access to:

- historical data
- sensor logs
- machine measurements
- wearable or device recordings

In this domain, the quality of the project usually comes from choosing a useful signal problem, not from adding a huge interface.

## Example Applications

Good project ideas include:

- an anomaly detector for sensor streams
- a predictive maintenance demo
- classification of signal patterns
- a forecast dashboard
- an industrial monitoring assistant
- wearable-signal or device-signal analysis
- a warning system for unusual patterns
- a simple process-monitoring app

You can shape this domain in different ways:

- prediction side: estimate future values
- anomaly side: detect unusual behavior
- classification side: label signal patterns
- monitoring side: build an application that watches a stream or dataset

The strongest student projects usually choose one signal type, one task, and one clear output.

## Which Technical Paths Fit Best

### Path 1: Train your own model on time-series data

This is the most natural route for many time-series projects.

It fits well if you want to:

- train or retrain a model directly on signal data
- understand the data -> model -> training workflow
- build a more classical deep-learning project

This is especially strong for:

- classification
- anomaly detection
- forecasting
- condition monitoring

### Path 2: Build around an existing forecasting or anomaly stack

This path is also possible if you want the main challenge to be the application and workflow.

It fits well if you want to:

- use an existing time-series library
- build a monitoring or prediction interface
- focus more on the product side than the model-training side

### Path 5: Deployment on real hardware

This domain can connect well to edge deployment or hardware-oriented work.

That is especially interesting if your project involves:

- a real sensor
- a device
- local monitoring
- low-latency inference

So this domain can become very strong if you want something closer to embedded or industrial systems.

## Recommended Starter Routes

You do not need to solve a huge industrial problem.
Pick one clear signal task and make it work well.

### Route A: Anomaly detection

This is one of the strongest starter routes in this domain.

Good fit for:

- machine signals
- device monitoring
- sensor streams
- unusual-pattern detection

Recommended tools:

- PyTorch
- pandas or polars
- Gradio or Streamlit for visualization

Why choose this route:

- very practical
- easy to explain
- naturally useful
- strong fit with electronics and industry

### Route B: Forecasting

This route is strong if you want a clear prediction task.

Good fit for:

- future value prediction
- trend forecasting
- demand or usage prediction
- signal forecasting

Recommended tools:

- NeuralForecast or another time-series library
- pandas or polars
- Streamlit or Gradio

Why choose this route:

- very standard task in time-series work
- easy to frame and evaluate
- good if you have historical data

### Route C: Signal classification

This route is good if you want a more model-centered project.

Good fit for:

- labeled signal windows
- device or activity classification
- pattern recognition in time-series data

Recommended tools:

- PyTorch
- tsai
- pandas or polars

Why choose this route:

- closer to standard supervised deep learning
- clearer training/evaluation story
- strong if you already have labeled data

### Route D: Monitoring dashboard or assistant

This route is a good fit if you want a more application-oriented project.

Good fit for:

- dashboards
- warnings
- anomaly alerts
- forecast visualization

Recommended tools:

- time-series model or library
- Streamlit, Gradio, or FastAPI
- data-processing tools

Why choose this route:

- strong product feel
- easy to connect model output to a useful interface
- very realistic engineering direction

## Which Frameworks to Start With

You do not need all of these.
Pick one main stack.

### PyTorch

Use PyTorch if:

- you want to train or retrain your own model
- you want flexibility
- you want a more classical deep-learning route

### tsai

Use tsai if:

- you want a time-series-focused deep-learning library
- you want help with signal classification or other time-series workflows
- you want a more domain-focused starting point than raw PyTorch alone

### NeuralForecast

Use NeuralForecast if:

- your project is about forecasting
- you want a dedicated forecasting ecosystem
- you want a more direct path for prediction tasks

### pandas or polars

Use pandas or polars if:

- you need preprocessing
- you need to clean or reshape time-series data
- you need to inspect the dataset carefully before modeling

In this domain, data preparation is often extremely important.

### Streamlit or Gradio

Use these if:

- you want a dashboard
- you want to visualize predictions or anomalies
- you want a simple user-facing interface

### FastAPI

Use FastAPI if:

- you want a backend API
- you want to separate the model and interface
- you want a service-oriented monitoring or prediction system

## Official Docs and Starting Points

Start from the official docs, not random short tutorials.

- PyTorch: <https://pytorch.org/>
- tsai: <https://timeseriesai.github.io/tsai/>
- NeuralForecast: <https://nixtlaverse.nixtla.io/neuralforecast/>
- pandas: <https://pandas.pydata.org/docs/>
- polars: <https://docs.pola.rs/>

If you want a training-focused route, start with PyTorch and tsai.

If you want a forecasting route, start with NeuralForecast.

If you want a dashboard-style project, plan the interface early so the output becomes visible and useful.

## How To Choose a Good Time-Series Project

Before you start building, answer these questions:

1. What signal are you working with?
   Sensor logs, machine data, wearable signals, measurements, or another time-based dataset?
2. What is the task?
   Forecasting, anomaly detection, classification, or monitoring?
3. What should the output be?
   Predicted values, alert, label, score, dashboard, or report?
4. Why is the output useful?
   What decision, warning, or insight does it support?

That last question matters a lot.

A time-series project becomes much stronger when the output has a clear meaning.

For example:

- "warn me when this machine signal looks abnormal"
- "predict the next values of this sensor"
- "classify what kind of activity or condition this signal represents"

## Good Advice Before You Begin

- use a manageable dataset
- define the task clearly
- make the output useful and explainable
- industrial applications are a strong option, but not the only option
- do not worry if the project is less flashy than vision or audio
- build a clear visualization so the result is easy to understand

This domain is probably less immediately attractive than images, text, or audio for some students, but it is still very valuable, especially if you want something more industrial, more engineering-oriented, or more connected to real devices.

For this course, this can be one of the strongest domains if you already have a meaningful dataset and you care more about usefulness than visual spectacle.
