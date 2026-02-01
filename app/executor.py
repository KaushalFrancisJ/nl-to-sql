from sqlalchemy import text
from .db import engine

def execute_sql(sql: str):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        columns = list(result.keys())  # ✅ convert to list

    return {
        "columns": columns,
        "rows": [list(row) for row in rows]  # ✅ ensure JSON-safe
    }
