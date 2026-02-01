def sql_prompt(schema: dict, question: str) -> str:
    return f"""
You are an expert SQL generator.

Database schema:
{schema}

Rules:
- Use ONLY the tables and columns listed above
- Generate ONLY SELECT queries
- Use PostgreSQL syntax
- Do NOT use INSERT, UPDATE, DELETE, DROP
- Return ONLY the SQL query

User question:
{question}
"""
