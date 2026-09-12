from __future__ import annotations
import json
import sqlite3
from datetime import datetime
from pathlib import Path

APP_DIR = Path.home() / ".peabox_streamlit_llm"
APP_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = APP_DIR / "workbench.db"
CONFIG_PATH = APP_DIR / "config.json"


def connect():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    with connect() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS conversations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            provider TEXT,
            model TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )""")
        con.execute("""CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            thinking TEXT DEFAULT '',
            created_at TEXT NOT NULL,
            FOREIGN KEY(conversation_id) REFERENCES conversations(id)
        )""")


def new_conversation(title="New chat"):
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as con:
        cur = con.execute(
            "INSERT INTO conversations(title, created_at, updated_at) VALUES(?,?,?)",
            (title, now, now),
        )
        return cur.lastrowid


def list_conversations():
    with connect() as con:
        return [dict(r) for r in con.execute(
            "SELECT * FROM conversations ORDER BY updated_at DESC"
        ).fetchall()]


def load_messages(conversation_id):
    with connect() as con:
        return [dict(r) for r in con.execute(
            "SELECT role, content, thinking, created_at FROM messages WHERE conversation_id=? ORDER BY id",
            (conversation_id,),
        ).fetchall()]


def add_message(conversation_id, role, content, thinking=""):
    now = datetime.now().isoformat(timespec="seconds")
    with connect() as con:
        con.execute(
            "INSERT INTO messages(conversation_id, role, content, thinking, created_at) VALUES(?,?,?,?,?)",
            (conversation_id, role, content, thinking, now),
        )
        con.execute("UPDATE conversations SET updated_at=? WHERE id=?", (now, conversation_id))


def update_conversation(conversation_id, title=None, provider=None, model=None):
    fields, values = [], []
    for name, value in (("title", title), ("provider", provider), ("model", model)):
        if value is not None:
            fields.append(f"{name}=?")
            values.append(value)
    if not fields:
        return
    values.append(conversation_id)
    with connect() as con:
        con.execute(f"UPDATE conversations SET {', '.join(fields)} WHERE id=?", values)


def delete_conversation(conversation_id):
    with connect() as con:
        con.execute("DELETE FROM messages WHERE conversation_id=?", (conversation_id,))
        con.execute("DELETE FROM conversations WHERE id=?", (conversation_id,))


def load_config():
    if not CONFIG_PATH.exists():
        return {}
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_config(config):
    CONFIG_PATH.write_text(json.dumps(config, indent=2), encoding="utf-8")
