
import sqlite3

DB_FILE = "chess.db"

def init_db():
    """Create tables if they don’t exist yet."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            result TEXT
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER,
            move TEXT,
            FOREIGN KEY (game_id) REFERENCES games(id)
        )
    """)

    conn.commit()
    conn.close()


def new_game():
    """Insert a new game and return its id."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO games (result) VALUES (?)", (None,))
    game_id = c.lastrowid
    conn.commit()
    conn.close()
    return game_id


def add_move(game_id, move):
    """Store a move for a game."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO moves (game_id, move) VALUES (?, ?)", (game_id, move))
    conn.commit()
    conn.close()


def game_moves(game_id):
    """Retrieve all moves for a game, in order."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT move FROM moves WHERE game_id=? ORDER BY id", (game_id,))
    moves = [row[0] for row in c.fetchall()]
    conn.close()
    return moves


def update_result(game_id, result):
    """Set the final result of the game."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE games SET result=? WHERE id=?", (result, game_id))
    conn.commit()
    conn.close()
