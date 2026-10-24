import sqlite3

def _create_table(cur: sqlite3.Cursor) -> None:
    """Create a `sessions` table if it doesn't exist."""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY,
            logged_at TEXT NOT NULL,
            minutes INTEGER NOT NULL,
            focus TEXT NOT NULL
        )
    """)


def _insert_session(cur: sqlite3.Cursor, minutes: int, focus: str) -> None:
    """Insert a session into the db."""
    cur.execute(
        """
        INSERT INTO sessions(logged_at, minutes, focus)
        VALUES (datetime('now', 'localtime'), ?, ?)
        """,
        (minutes, focus)
    )


def initialize_database() -> None:
    """Initialize a db and create a`sessions` table."""
    con = sqlite3.connect("sessions.db")

    try:
        cur = con.cursor()
        _create_table(cur)
        con.commit()
    finally:
        con.close()


def create_session(minutes: int, focus: str) -> None:
    """Save a practice session to the database."""
    con = sqlite3.connect("sessions.db")

    try:
        cur = con.cursor()
        _insert_session(cur, minutes, focus)
        con.commit()
    finally:
        con.close()
