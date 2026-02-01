import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

# Get project root (parent of app/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(BASE_DIR / ".env")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

print("DB CONFIG:", DB_HOST, DB_PORT, DB_NAME, DB_USER)

if not all([DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD]):
    raise RuntimeError("Database environment variables not loaded")

DB_URL = (
    f"postgresql+psycopg2://{DB_USER}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}:"
    f"{DB_PORT}/"
    f"{DB_NAME}"
)

engine = create_engine(DB_URL)
