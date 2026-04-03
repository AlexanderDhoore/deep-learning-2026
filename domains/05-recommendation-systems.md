# Domain 5: Recommendation Systems

Recommendation systems are closely related to embeddings and ranking, but the user experience is different from search.

If you like music, media, products, personalization, ranking, or user-facing web applications, this is a very strong domain for a project.

It is also one of the best domains if you want to build something that feels like a real product instead of only a technical demo.

## What This Domain Is

A recommendation system suggests useful items to a user.

That can mean:

- recommending songs, videos, or movies
- suggesting products or articles
- proposing similar items
- ranking options for a user
- personalizing what a user sees first

The big difference from search is this:

- in search, the user asks and the system returns matches
- in recommendation, the system proposes items that might be useful or interesting

So even if search and recommendation can both use embeddings, they create a different kind of application.

A recommendation system is usually trying to answer questions like:

- What should this user probably see next?
- Which items are similar to this one?
- Which options are most relevant for this situation?

That makes recommendation a very product-oriented domain.

## Why You Might Choose It

This is a strong domain for this course for several reasons:

- recommendation is everywhere on the modern web
- it is a realistic product-oriented AI domain
- it can lead to a strong demo with a clear user experience
- it is a good fit if you like music, media, products, or content platforms

It is also a nice domain if you want a project that feels close to real web products.

For example:

- music recommender
- movie suggestion app
- article or content recommender
- product recommendation demo
- "similar items" explorer

This domain is often less about huge models and more about making a good recommendation workflow:

- what information do you use?
- how do you score or compare items?
- how do you show the recommendations?

That makes it a very good fit for a practical course project.

## Example Applications

Good project ideas include:

- a music or media recommender
- a product recommendation demo
- a similar-item recommender
- a recommendation app based on embeddings
- a content-based recommendation tool
- a movie, book, or game suggestion tool
- a curated "discover similar items" explorer

You can shape this domain in several ways:

- similarity recommender
  "If you like this item, you may also like these."
- profile-based recommender
  Recommend based on a user's preferences or selected examples.
- ranking interface
  Show the best candidates first for a chosen goal.

The strongest student projects here usually keep the dataset and the user experience simple.

## How Recommendation Is Different from Search

This is worth making very explicit.

Search:

- the user writes a query
- the system returns matching or similar items

Recommendation:

- the system already knows something about the user, item, or context
- the system proposes useful items without needing a full search query every time

So recommendation is usually about:

- ranking
- similarity
- personalization
- suggestions

That is why this domain is a good fit if you care about product thinking and user experience.

## Which Technical Paths Fit Best

### Path 2: Build with pretrained embeddings

This is the most natural route for many recommendation projects.

It fits well if you want to:

- use embeddings from existing models
- compare items by similarity
- build a recommender without training a large model from scratch

This is especially strong for:

- content-based recommendation
- similar-item recommendation
- media or product discovery

### Path 1: Custom ranking experiments

This path is possible if you want a slightly more custom machine-learning route.

It fits if you want to:

- build a custom ranking model
- experiment with scoring functions
- use PyTorch more directly

For this course, many recommendation projects will probably be strongest if they start simple with embeddings and only become more custom later if needed.

### Strong connection to retrieval

This domain is closely related to [semantic search and retrieval](04-semantic-search-and-retrieval.md).

The difference is not mainly the embedding technology.
The difference is the user experience:

- search helps the user find something
- recommendation helps the system suggest something

So if your project idea is somewhere between both, that is completely fine.
Just decide what the main interaction should be.

## Recommended Starter Routes

You do not need to build a full Netflix-style system.
Pick one clear recommendation idea and make it work well.

### Route A: Similar-item recommender

This is one of the best starter routes.

Good fit for:

- songs
- movies
- books
- products
- images

Recommended tools:

- Sentence Transformers
- similarity scoring
- Gradio or Streamlit

Why choose this route:

- very understandable
- easy to explain
- easy to demo

This route often starts with:

- choose one item
- find nearby items in embedding space
- show the recommendations

That is already a valid and useful recommendation system.

### Route B: Content-based recommender

This route is strong if you have metadata, descriptions, or item text.

Good fit for:

- articles
- products
- media catalogs
- curated item collections

Recommended tools:

- Sentence Transformers
- PyTorch only if you need more custom ranking later
- Gradio, Streamlit, or FastAPI

Why choose this route:

- realistic
- grounded in actual item information
- easier to scope than heavy personalization

### Route C: User-profile recommender

This route is more ambitious, but still possible if kept small.

Good fit for:

- user preference demos
- selecting favorite items and generating recommendations
- profile-based ranking

Recommended tools:

- embeddings
- simple ranking logic
- frontend for selecting preferences

Why choose this route:

- more product-like
- more interactive
- more obviously personalized

## Which Frameworks to Start With

You do not need all of these.
Pick one main stack.

### Sentence Transformers

Use Sentence Transformers if:

- you want embeddings quickly
- you want similarity-based recommendation
- your items have useful text descriptions
- you want the easiest strong starting point

This is the most important first tool in this domain for many projects.

### PyTorch

Use PyTorch if:

- you want more custom ranking experiments
- you want to move beyond simple similarity scoring
- you want more direct model control

For many student projects, PyTorch is optional here rather than the first thing to touch.

### Vector search library or vector database

Use one of these if:

- you want efficient nearest-neighbor retrieval
- you want to scale beyond a tiny in-memory demo
- you want stronger backend structure

For a small project, you may not need a full vector database immediately.

### Gradio or Streamlit

Use these if:

- you want a quick interface
- you want users to browse recommendations
- you want the frontend to stay simple

These are especially useful because recommendation systems benefit from visible interaction.

### FastAPI

Use FastAPI if:

- you want a backend API
- you want a more service-oriented architecture
- you want to separate frontend and recommendation logic

## Official Docs and Starting Points

Start from the official docs, not random short tutorials.

- Sentence Transformers: <https://www.sbert.net/>
- PyTorch: <https://pytorch.org/>
- Gradio: <https://www.gradio.app/docs>
- Streamlit: <https://docs.streamlit.io/>
- FastAPI: <https://fastapi.tiangolo.com/>

If you want the easiest route, start with Sentence Transformers and a small curated dataset.

If you later want a more custom ranking story, bring in PyTorch.

If you want a richer web-app feel, use Streamlit or Gradio first and only move to a more custom frontend if you really need it.

## How To Choose a Good Recommendation Project

Before you start building, answer these questions:

1. What kinds of items are you recommending?
   Songs, products, articles, movies, images, books, games, or something else?
2. What information do you have about those items?
   Titles, descriptions, tags, metadata, or user choices?
3. What is the recommendation interaction?
   Similar item, personalized ranking, discovery feed, or suggested next step?
4. What does the user actually see?
   A recommendation list, cards, ranked items, or an interactive explorer?

If those answers are clear, your project is probably well scoped.

## Good Advice Before You Begin

- start with a simple content-based approach
- keep the recommendation logic understandable
- focus on one dataset and one clear user experience
- embeddings are often the core building block here
- do not overcomplicate personalization too early
- make the output easy to browse and explain

A simple recommender with a clean UI and understandable logic is usually stronger than a complicated personalization system that nobody can clearly explain.

For this course, this is one of the nicest domains if you want something practical, modern, and strongly connected to real products on the web.
