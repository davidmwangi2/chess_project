
import sqlite3
from contextlib import contextmanager

DB_FILE = "chess_game.db"

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_FILE)
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()

def init_db():
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            white TEXT,
            black TEXT,
            result TEXT
        )""")
        c.execute("""
        CREATE TABLE IF NOT EXISTS moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER,
            move TEXT,
            FOREIGN KEY(game_id) REFERENCES games(id)
        )""")

def create_game(white, black):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO games (white, black) VALUES (?,?)", (white, black))
        return c.lastrowid

def add_move(game_id, move):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO moves (game_id, move) VALUES (?,?)", (game_id, move))

def game_moves(game_id):
    with get_conn() as conn:
        c = conn.cursor()
        return [row[0] for row in c.execute("SELECT move FROM moves WHERE game_id=? ORDER BY id", (game_id,))]
