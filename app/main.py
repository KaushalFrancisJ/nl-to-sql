from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .schema import get_db_schema
from .prompt import sql_prompt
from .llm import llm
from .validator import validate_sql
from .executor import execute_sql
from .summarizer import summarize

app = FastAPI(title="NL to SQL Engine")

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_db(req: QueryRequest):
    schema = get_db_schema()
    prompt = sql_prompt(schema, req.question)

    sql = llm.invoke(prompt).content.strip()


    try:
        validate_sql(
            sql,
            allowed_tables=set(schema.keys()),
            allowed_columns=schema
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    result = execute_sql(sql)
    answer = summarize(req.question, result)

    return {
        "question": req.question,
        "sql": sql,
        "answer": answer,
        "data": {
            "columns": list(result["columns"]),
            "rows": result["rows"]
        }
    }
