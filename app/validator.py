import sqlglot

FORBIDDEN_KEYWORDS = {
    "insert", "update", "delete", "drop",
    "alter", "truncate", "create"
}

def validate_sql(sql: str, allowed_tables: set, allowed_columns: dict):
    parsed = sqlglot.parse_one(sql)

    # Ensure SELECT only
    if parsed.key != "select":
        raise ValueError("Only SELECT queries are allowed")

    sql_lower = sql.lower()
    for word in FORBIDDEN_KEYWORDS:
        if word in sql_lower:
            raise ValueError(f"Forbidden keyword detected: {word}")

    # Table validation
    tables = {t.name for t in parsed.find_all(sqlglot.expressions.Table)}
    if not tables.issubset(allowed_tables):
        raise ValueError("Query references unauthorized tables")

    # Column validation
    for col in parsed.find_all(sqlglot.expressions.Column):
        table = col.table
        name = col.name
        if table and name not in allowed_columns.get(table, []):
            raise ValueError(f"Unauthorized column: {table}.{name}")

    return True
