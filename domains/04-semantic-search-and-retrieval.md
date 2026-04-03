# Domain 4: Semantic Search and Retrieval

This domain is built around embeddings.

## What This Domain Is

An embedding is a vector representation of something like text, image, or audio.

The key idea is simple:

- similar meaning leads to nearby vectors
- that lets you search by meaning instead of only by exact words
- that also makes retrieval and RAG-style systems possible

## Why You Might Choose It

- it is one of the most practical modern AI workflows
- it is easier to scope than many full fine-tuning projects
- it works well for documents, notes, images, and knowledge bases
- it is a strong bridge between classic search and modern LLM apps

## Example Applications

- semantic search through notes or documents
- retrieval-augmented chatbot
- similar-item finder
- document search tool
- knowledge-base search assistant

## Which Technical Paths Fit Best

- Path 2 if you want to build with pretrained embedding models
- Path 3 if you later want to adapt part of a larger stack
- this domain combines naturally with language-model applications

## Recommended Frameworks to Start With

- Sentence Transformers
- Hugging Face Transformers
- a vector search library or vector database
- Gradio / Streamlit / FastAPI

## Official Docs and Starting Points

- Sentence Transformers: <https://www.sbert.net/>
- Hugging Face Transformers: <https://huggingface.co/docs/transformers/en/index>
- Hugging Face tasks: <https://huggingface.co/tasks>
- Gradio: <https://www.gradio.app/docs>
- Streamlit: <https://docs.streamlit.io/>
- FastAPI: <https://fastapi.tiangolo.com/>

## Good Advice Before You Begin

- start with embeddings and cosine similarity
- keep the retrieval pipeline understandable
- focus on one dataset and one clear user task
- remember that RAG is retrieval first, then generation
