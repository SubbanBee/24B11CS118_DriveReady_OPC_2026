# Day 5 – Memory and RAG

## Project
Sweet Crumbs Home Bakery – AI Agent

## Objective
Build an AI agent that remembers individual customer conversations and retrieves relevant bakery information using Retrieval-Augmented Generation (RAG).

## Concepts Covered
- Conversation memory using LangGraph `InMemorySaver`
- Customer-specific memory using `thread_id`
- Text embeddings using Hugging Face
- Vector database using ChromaDB
- Semantic search
- Document retrieval
- RAG integration with an AI agent

## Tools and Technologies
- Python
- Google Colab
- Groq API
- LangChain
- LangGraph
- Hugging Face Sentence Transformers
- ChromaDB

## Implementation
1. Configured Groq LLM.
2. Implemented customer-specific conversation memory.
3. Generated text embeddings.
4. Created a ChromaDB vector database.
5. Stored bakery FAQ information.
6. Implemented semantic search.
7. Created a `search_faq` tool.
8. Integrated FAQ retrieval with the AI agent.
9. Tested memory and RAG together.

## Test Results
- Customer memory retrieval: Successful
- Customer separation: Successful
- Delivery FAQ retrieval: Successful
- Plum Cake price retrieval: Successful
- Chocolate Cake price retrieval: Successful
- Eggless availability: Successful

## Business Information
- Chocolate Cake: Rs. 650
- Plum Cake: Rs. 500
- Both cakes have eggless versions.
- Unconfirmed business policies are referred to the owner.

## Files
- `README.md`
- `task.py`
- `Sweet_crumbs_AI_Day5.ipynb`

## Status
Day 5 implementation completed successfully.
