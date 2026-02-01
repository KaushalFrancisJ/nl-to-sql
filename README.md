# Natural Language to SQL Query Engine

An end-to-end system that allows users to query a relational database using
plain English, without writing SQL.

## Features
- Natural language → SQL generation using LLMs
- Schema-aware prompt injection to reduce hallucinations
- Foreign-key aware joins for correct multi-table queries
- SQL validation layer (SELECT-only, table/column whitelisting)
- Safe execution on PostgreSQL
- Natural language summarization of query results
- Exposed via FastAPI

## Tech Stack
- Python 3.11
- FastAPI
- LangChain
- PostgreSQL
- SQLAlchemy
- Groq / OpenAI / Ollama (pluggable)

## Architecture
User Question → Prompt + Schema → LLM → SQL Validation → Execution → Summarization → Response

## Example Query
**Input**
```json
{ "question": "What is the count of employees?" }
