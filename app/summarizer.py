from .llm import llm

def summarize(question: str, result: dict) -> str:
    prompt = f"""
User question:
{question}

SQL result:
Columns: {result['columns']}
Rows: {result['rows']}

Summarize the answer in plain English.
Do not mention SQL or tables.
"""
    return llm.invoke(prompt).content
