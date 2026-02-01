from sqlalchemy import inspect
from .db import engine

def get_db_schema():
    inspector = inspect(engine)
    schema = {}

    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        schema[table] = [col["name"] for col in columns]

    return schema
