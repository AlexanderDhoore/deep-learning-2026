# Domain 2: Language Models and Text Systems

This domain is about building AI systems that work mainly with text.

If you like chat interfaces, assistants, writing tools, document workflows, or automation, this is one of the most accessible and flexible domains in the course.

It is also one of the most dangerous domains to scope badly.
A small, focused text application is usually a strong project.
A vague "AI assistant that does everything" is usually a weak one.

## What This Domain Is

Language models are systems that work with text.

Depending on the project, that can mean:

- generating text
- answering questions
- summarizing documents
- classifying messages or documents
- extracting information
- rewriting text
- ranking or comparing texts
- calling external tools from inside an AI workflow

In practice, this domain often looks like:

- user writes something
- the model interprets it
- the model produces an answer, action, or transformation

So the project is often not only "ask a model a question".
The interesting part is usually the application around the model:

- what text comes in
- what the system does with it
- what extra tools or data it can use
- how the result is shown to the user

## Why You Might Choose It

This is a strong domain for this course for several reasons:

- you already touched this domain in the generative AI workshop
- it is easy to prototype quickly
- it is easy to combine with a frontend
- many modern AI products are built in this space
- you can create something useful without training a model from scratch

It is also a good fit if you want a project with:

- clear user interaction
- a web-based interface
- a workflow that feels modern
- lots of room for creative product ideas

If you like building assistants, productivity tools, study tools, or text-processing applications, this domain gives you many options.

## Important Reality Check

For this course, this domain is usually about:

- Path 2: build with pretrained models
- Path 3: adapt or fine-tune large models

It is usually **not** about training your own large language model from scratch.

Why not?

- it needs too much data
- it needs too much compute
- it is not realistic for the time available in this course

That does **not** make this domain less interesting.
Modern language-model engineering is usually about:

- choosing a good pretrained model
- designing a useful workflow around it
- possibly adapting it
- building a clean application

That is already a very real and valuable engineering path.

## Example Applications

Good project ideas include:

- a chatbot for a narrow domain
- a study assistant for one course or one topic
- a summarizer for notes, articles, or transcripts
- a classifier for emails, tickets, or short documents
- a question-answering tool for a specific dataset
- an information-extraction tool
- a tool-calling assistant
- a writing helper for one clear task

You can also make this more practical and less generic.

For example:

- an assistant that summarizes uploaded lecture notes
- a system that classifies support tickets into categories
- a document helper that extracts deadlines, names, or action points
- an assistant that calls search, calculator, or API tools
- a study helper that turns notes into flashcards or summaries

The best ideas in this domain are usually not the biggest ones.
They are the clearest ones.

## Which Technical Paths Fit Best

### Path 2: Build with pretrained foundation models

This is the most natural route for many language-model projects.

It fits well if you want to:

- use an existing model
- build a chatbot or assistant
- create a useful text workflow
- focus on application design instead of training

This path is especially strong for:

- chat systems
- summarizers
- question-answering tools
- document workflows
- tool-calling assistants

### Path 3: Fine-tune or adapt large models

This path is more ambitious, but it is real and interesting.

It fits if you want to:

- adapt a model to a narrower domain
- explore LoRA or PEFT-style techniques
- do more than prompting, but less than full retraining

This can be a very good project if:

- you keep the scope small
- you choose a narrow task
- you are interested in the engineering side of adaptation

### Path 2 + Semantic Search

Many of the most useful language-model systems are not just "an LLM".

They also use:

- embeddings
- retrieval
- ranking
- document context

That means this domain often combines naturally with [semantic search and retrieval](04-semantic-search-and-retrieval.md).

If your idea involves:

- documents
- knowledge bases
- search
- grounding answers in a dataset

then you should probably read that domain note as well.

## Tool Calling: One of the Best Project Directions Here

Tool calling is especially powerful in this domain.

The basic idea is:

- the model reads the user request
- the model decides whether it should use another tool
- the tool runs
- the result comes back into the workflow
- the model generates the final answer

Example tools include:

- search
- calculator
- database lookup
- Python function call
- external API call

This is powerful because the system is no longer just "text in, text out".
It becomes an application that can do things.

That makes tool calling one of the strongest project ideas in this domain.

Good examples:

- a study assistant that searches a note collection
- a chatbot that looks up structured information
- an assistant that performs small automation steps
- a helper that classifies, summarizes, and stores information

## Recommended Starter Routes

You do not need to understand the whole language-model ecosystem before you begin.
Pick one route and make it work well.

### Route A: Local chatbot or assistant

This is the simplest route if you want to build something useful quickly.

Good fit for:

- chat systems
- question answering
- summarization
- small assistant apps

Recommended tools:

- Ollama
- a small local language model setup

Why choose this route:

- fast to prototype
- good for local experimentation
- easy to demo

### Route B: Hugging Face text application

This is a good route if you want more flexibility and access to many models and tasks.

Good fit for:

- text classification
- summarization
- question answering
- generation
- more experimental text workflows

Recommended tools:

- Hugging Face Transformers

Why choose this route:

- very broad ecosystem
- strong official docs
- easier to explore many task types

### Route C: Tool-calling assistant

This is one of the most interesting routes if you want a project that feels like a real product.

Good fit for:

- assistants
- multi-step text workflows
- applications with external tools

Recommended tools:

- Ollama or Transformers
- your own small helper functions or APIs

Why choose this route:

- modern and practical
- strong system-design component
- great for oral explanation during the exam

### Route D: LLM + retrieval workflow

This route is a strong choice if you want the system to work on a real dataset instead of only the model's built-in knowledge.

Good fit for:

- question answering over documents
- knowledge-base assistants
- note search and summarization

Recommended tools:

- Sentence Transformers
- Ollama or Transformers

Why choose this route:

- more grounded than a plain chatbot
- very realistic modern workflow
- excellent bridge between domains

## Which Frameworks to Start With

You do not need all of these.
Pick one main stack.

### Ollama

Use Ollama if:

- you want to run local models quickly
- you want a practical way to prototype a chat or assistant app
- you want the model-serving part to be simple

Ollama is often a very good default if you want to move fast.

### Hugging Face Transformers

Use Transformers if:

- you want access to many model types and tasks
- you want more flexibility
- you want to work closer to the broader model ecosystem

This is one of the most important official ecosystems for this domain.

### Sentence Transformers

Use Sentence Transformers if:

- your project involves embeddings
- you want semantic search or retrieval
- you want similarity-based workflows

This is especially useful if your text project needs more than plain chat.

## Official Docs and Starting Points

Start from the official docs, not random short tutorials.

- Ollama: <https://ollama.com/>
- Hugging Face Transformers: <https://huggingface.co/docs/transformers/en/index>
- Sentence Transformers: <https://www.sbert.net/>

If you want the fastest path to a working app, start with Ollama.

If you want the broadest official model ecosystem, start with Transformers.

If your idea involves retrieval or meaning-based search, include Sentence Transformers early.

For generic interface or backend tooling, use the top-level support-tooling page instead of this domain note.

## How To Choose a Good Language-Model Project

Before you start building, answer these questions:

1. What text comes in?
   User prompt, notes, emails, documents, messages, transcripts, or something else?
2. What should the system do?
   Answer, summarize, classify, extract, rewrite, rank, or call tools?
3. What extra context or tools does it need?
   Documents, search, APIs, calculator, database, or no extra tools?
4. What does the user actually see?
   A chat interface, upload form, dashboard, report, or generated output?

If you cannot answer those clearly, the project is probably still too vague.

## Good Advice Before You Begin

- narrow the scope
- avoid trying to build a general chatbot for everything
- give the app one clear purpose
- make the value of the system easy to explain
- use pretrained or fine-tuned models, not full training from scratch
- if the project needs documents or search, read the retrieval domain note as well

A small assistant that does one thing well is usually much better than a "smart AI platform" that never becomes stable.

For this course, this is one of the easiest domains to prototype quickly, but only if you keep it focused.
