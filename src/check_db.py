"""Smoke test: confirm Python can reach the project database."""
import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

required = ["DB_NAME", "DB_USER", "DB_PASSWORD"]
missing = [name for name in required if not os.getenv(name)]
if missing:
    raise SystemExit(
        f"Missing environment variables: {', '.join(missing)}"
    )

with psycopg.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432"),
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        print(cur.fetchone()[0])