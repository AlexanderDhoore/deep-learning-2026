# Domain 4: Semantic Search and Retrieval

This domain is built around embeddings.

If you like search, knowledge bases, document systems, or AI applications that work on real data instead of only the model's built-in knowledge, this is one of the strongest domains in the course.

It is also one of the most practical modern AI workflows.
Many useful AI systems today are not just "an LLM".
They are retrieval systems with embeddings, search, ranking, and sometimes generation on top.

## What This Domain Is

The key idea starts with embeddings.

An embedding is a vector representation of something like:

- text
- image
- audio

If two things have similar meaning, a good embedding model should place them close together in vector space.

That makes it possible to:

- search by meaning, not only by exact words
- find similar items
- retrieve relevant context
- build systems that work on a document collection or knowledge base

So instead of matching only keywords, the system can ask:

> Which stored items are semantically closest to this query?

That is why this domain is so useful.

It gives you a way to connect AI to a real dataset in a clean, understandable pipeline.

## What Retrieval Usually Looks Like

A simple retrieval system often looks like this:

1. take a set of documents, notes, images, or other items
2. convert them into embeddings
3. store those embeddings
4. convert the user query into an embedding
5. search for the nearest or most similar items
6. show the results or pass them into another step

That last step can go in two ways:

- search-only workflow
  Show the most relevant results directly to the user.
- search + generation workflow
  Retrieve context first, then pass it to a language model to generate an answer.

The second pattern is usually called RAG.

## RAG: Retrieve First, Then Generate

RAG means retrieval-augmented generation.

The idea is:

- retrieve the most relevant documents first
- give that context to the language model
- generate an answer with better grounding

So the system is no longer answering from the model alone.
It is answering with help from the dataset you selected.

That is why RAG is so attractive:

- answers can be more grounded
- the project becomes connected to your own data
- the system can feel much more useful than a generic chatbot

RAG belongs in this domain because retrieval is the foundation.
Without the retrieval step, the generation step has nothing specific to ground itself in.

## Why You Might Choose It

This is a strong domain for this course for several reasons:

- it is one of the most practical modern AI workflows
- it is easier to scope than many full fine-tuning projects
- it works well for documents, notes, images, and knowledge bases
- it is a strong bridge between classic search and modern LLM apps
- it combines very naturally with web apps and assistant-style systems

It is also a very good choice if you want a project that feels useful very quickly.

For example:

- search through your own notes
- search through a document collection
- build a chatbot over a knowledge base
- find similar images or similar texts

This domain is often less flashy than image generation, but it is one of the most realistic and reusable options you can choose.

## Example Applications

Good project ideas include:

- semantic search through notes or documents
- a retrieval-augmented chatbot
- a similar-item finder
- a document search tool
- a knowledge-base search assistant
- an FAQ assistant grounded in a dataset
- an image or text similarity explorer
- a small course or study search tool

You can also shape this domain in different ways:

- search product: user searches and sees results
- assistant product: system retrieves context and answers questions
- similarity product: system finds related or nearest items
- backend system: embeddings and retrieval power another application

The strongest projects here usually have one clear dataset and one clear user task.

## Which Technical Paths Fit Best

### Path 2: Build with pretrained embedding models

This is the most natural route for many projects in this domain.

It fits well if you want to:

- use an existing embedding model
- build a retrieval pipeline
- focus on workflow and application design

This path is especially strong for:

- semantic search
- note or document retrieval
- RAG workflows
- similarity-based tools

### Path 3: Adapt part of the stack later

This path is possible, but it is usually not where you should start.

For example, later you might:

- swap in a better embedding model
- add a reranker
- adapt another part of the workflow

But for this course, the strongest first version is usually:

- embeddings
- similarity search
- clean interface
- maybe generation on top

### Strong connection to language-model projects

This domain combines naturally with [language models and text systems](02-language-models-and-llm-apps.md).

If your idea involves:

- a chatbot over documents
- grounded answers
- note search with summarization
- AI over a dataset

then retrieval is probably part of the design, even if the interface looks like a chat app.

## Recommended Starter Routes

You do not need to start with a full production-style vector system.
Pick one route and make it work clearly.

### Route A: Simple semantic search

This is the best starter route if you want to understand the core idea directly.

Good fit for:

- note search
- document search
- similar-text search

Recommended tools:

- Sentence Transformers
- cosine similarity

Why choose this route:

- easiest to understand
- easiest to explain
- very strong first prototype

This route can even start without a full vector database.
For a small dataset, plain embeddings plus similarity search can already be enough.

### Route B: Retrieval + chatbot

This is one of the strongest routes if you want a project that feels like a modern AI product.

Good fit for:

- document question answering
- knowledge-base chat
- study assistants

Recommended tools:

- Sentence Transformers
- Ollama or Transformers for the generation part

Why choose this route:

- practical and modern
- grounded in real data
- easy to demonstrate well

### Route C: Vector search system

This route is stronger if you want more systems flavor.

Good fit for:

- larger datasets
- more structured retrieval pipelines
- backend-oriented projects

Recommended tools:

- Sentence Transformers
- Qdrant or Faiss

Why choose this route:

- stronger engineering feel
- more backend-oriented
- good if you care about retrieval infrastructure

## Which Frameworks to Start With

You do not need all of these.
Pick one main stack.

### Sentence Transformers

Use Sentence Transformers if:

- you want embeddings quickly
- you want semantic search
- you want similarity-based workflows
- you want a very practical starting point

This is the most important first tool in this domain.

### Hugging Face Transformers

Use Transformers if:

- you want broader control over models
- you want to explore other embedding-capable models
- you want generation and retrieval in the same broader ecosystem

### Faiss

Use Faiss if:

- you want efficient similarity search
- you want a classic retrieval library
- you want to build a smaller custom retrieval system

Faiss is especially useful if you want retrieval infrastructure without immediately introducing a bigger external service.

### Qdrant

Use Qdrant if:

- you want a vector database with an API
- you want a more production-style retrieval setup
- you want filtering, metadata, and a retrieval service feel

For many student projects, Qdrant is not required.
But it is a good option if you want the storage and search layer to feel more like a real backend system.

## Official Docs and Starting Points

Start from the official docs, not random short tutorials.

- Sentence Transformers: <https://www.sbert.net/>
- Hugging Face Transformers: <https://huggingface.co/docs/transformers/en/index>
- Hugging Face tasks: <https://huggingface.co/tasks>
- Faiss: <https://faiss.ai/>
- Qdrant: <https://qdrant.tech/documentation/>

If you want the easiest route, start with Sentence Transformers and a small dataset.

If you want a stronger backend flavor, add Faiss or Qdrant.

If you want a chatbot over documents, combine retrieval with a language model only after the retrieval step is already working clearly.

For generic interface or backend tooling, use the top-level support-tooling page instead of this domain note.

## How To Choose a Good Retrieval Project

Before you start building, answer these questions:

1. What are you searching through?
   Notes, PDFs, articles, images, course material, or another dataset?
2. What is the user trying to do?
   Search, ask questions, find similar items, or explore a collection?
3. What should the output be?
   Search results, similar items, retrieved passages, or a generated answer?
4. Does the project really need generation?
   Or is search itself already the useful product?

That last question matters a lot.

Many projects become better if you first build:

- retrieval

and only later add:

- generation

This keeps the system understandable and easier to debug.

## Good Advice Before You Begin

- start with embeddings and cosine similarity
- keep the retrieval pipeline understandable
- focus on one dataset and one clear user task
- do not add generation too early if search alone already makes sense
- remember that RAG is retrieval first, then generation
- make sure the final user experience is easy to explain

A simple retrieval system with a clean demo is often better than a complicated RAG system that the builder does not fully understand.

For this course, this is one of the safest and strongest domains if you want a project that feels modern, useful, and technically solid without requiring huge model training.
