# Domain 9: Reinforcement Learning and Control

Reinforcement learning is a special case in this folder.

It is not a normal application domain like vision, language, or audio.
It is a project direction built around a different way of learning.

It is included here because, from a student point of view, it is still a clear path you might choose for your project.

## What This Direction Is

In reinforcement learning, the model does not mainly learn from labeled examples.

Instead, it:

- interacts with an environment
- tries actions
- receives rewards
- improves over time

So the system learns by experience and feedback.

That environment can be:

- a game
- a simulation
- a control problem
- in more advanced cases, a physical system

A useful way to think about reinforcement learning is:

> The model keeps making decisions, and the environment tells it how good those decisions were.

This makes reinforcement learning feel very different from normal supervised training.

## Why You Might Choose It

This is a strong project direction if you like:

- games
- simulation
- decision making
- control systems
- agents that learn behavior

It is also one of the clearest examples of AI learning through interaction rather than just pattern recognition.

This path is exciting because the model can discover strategies by itself.

At the same time, it is riskier than many other directions because:

- it can take more time
- it can take more compute
- environment design matters a lot
- debugging can be less straightforward

So it is a very interesting path, but it should be scoped carefully.

## Example Applications

Good project ideas include:

- train an agent in a simple game environment
- compare RL algorithms on one task
- build an interactive policy demo
- make an agent learn a control strategy in simulation
- create a custom small environment and train an agent on it

For this course, the safest and strongest RL projects are usually based on:

- games
- simple simulations
- toy control tasks

That is usually a better fit than trying to do real robotics hardware work immediately.

## Which Technical Path This Fits

This file is itself about `Path 4: Reinforcement Learning and Control`.

So unlike the other files in `domains/`, this is not mainly about a modality.
It is about a learning setup.

That means you should choose this direction if the central challenge of your project is:

- training an agent through reward
- designing an environment
- studying learned behavior

not mainly:

- image classification
- text generation
- retrieval
- deployment

## Recommended Starter Routes

### Route A: Simple game environment

This is the safest starter route.

Good fit for:

- CartPole-style tasks
- grid worlds
- simple game logic
- small custom environments

Recommended tools:

- Gymnasium
- Stable-Baselines3
- PyTorch

Why choose this route:

- easiest to understand
- easiest to debug
- easiest to demonstrate

### Route B: Compare algorithms on one task

This route is good if you want a clearer scientific or engineering comparison.

Good fit for:

- benchmarking PPO vs DQN or similar choices
- studying training behavior
- comparing reward design or environment settings

Recommended tools:

- Gymnasium
- Stable-Baselines3
- TensorBoard or another logging tool if useful

Why choose this route:

- very explainable
- good for oral defense
- focuses on clear experimental reasoning

### Route C: Small control simulation

This route is interesting if you care about control more than games.

Good fit for:

- simulated balancing tasks
- control-oriented toy environments
- simple system behavior problems

Recommended tools:

- Gymnasium
- Stable-Baselines3
- TorchRL if you want a more PyTorch-native route

Why choose this route:

- closer to control engineering
- still feasible if kept simple
- strong bridge toward real-world systems

## Which Tools to Start With

### Gymnasium

Use Gymnasium if:

- you need environments
- you want a standard RL interface
- you want to use common RL tooling

This is the main starting point for the environment side of RL.

### Stable-Baselines3

Use Stable-Baselines3 if:

- you want the safest student-friendly RL starting point
- you want reliable implementations of standard algorithms
- you want to focus more on the project than on implementing algorithms from scratch

For most students, this is the best first RL tool.

### TorchRL

Use TorchRL if:

- you want a more PyTorch-native RL workflow
- you want something a bit more advanced or modular
- you already know why you want it

It is a valid option, but Stable-Baselines3 is usually the safer default.

### PyTorch

Use PyTorch if:

- you want to understand the model side more deeply
- you want lower-level control
- you want to build on top of the broader PyTorch ecosystem

## Official Docs and Starting Points

Start from the official docs, not random short tutorials.

- Gymnasium: <https://gymnasium.farama.org/>
- Stable-Baselines3: <https://stable-baselines3.readthedocs.io/>
- TorchRL: <https://docs.pytorch.org/rl/main/index.html>
- PyTorch: <https://pytorch.org/>

If you want the safest path, start with Gymnasium and Stable-Baselines3 on a simple environment.

If you want a more advanced PyTorch-native route, look at TorchRL after you already understand the basics.

## How To Choose a Good RL Project

Before you start building, answer these questions:

1. What is the environment?
   A game, simulation, or control problem?
2. What action does the agent take?
   Move, choose, control, or optimize something?
3. What reward tells the agent it is doing well?
4. How will you demonstrate success?
   Score, survival time, reward curve, or visible learned behavior?

If those answers are not clear, the project is probably still too vague.

In RL, reward design and environment definition are often more important than fancy implementation details.

## Good Advice Before You Begin

- keep the environment simple
- do not overscope
- use Stable-Baselines3 as the default starting point unless you have a reason not to
- make the reward easy to explain
- make sure you have a clear success metric
- prefer a small working agent over a huge ambitious environment

This is one of the most interesting project directions in the course, but also one of the riskiest.

For this course, the strongest RL projects are usually simple, focused, and simulation-based.
