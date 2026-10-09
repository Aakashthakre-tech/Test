"""Intentionally vulnerable demo app. For local security testing only."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("demo.db")


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
        conn.execute("DELETE FROM users")
        conn.executemany(
            "INSERT INTO users (username) VALUES (?)",
            [("alice",), ("bob",), ("charlie",)],
        )


def find_user(username: str):
    # INTENTIONALLY VULNERABLE: user input is interpolated into SQL.
    query = f"SELECT id, username FROM users WHERE username = '{username}'"
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(query).fetchall()


if __name__ == "__main__":
    init_db()
    print("Normal lookup:", find_user("alice"))
    print("Test lookup:", find_user("alice' OR '1'='1"))
