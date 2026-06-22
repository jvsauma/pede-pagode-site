import sqlite3
from pathlib import Path

DATABASE_DIR = Path(__file__).resolve().parent

DATABASE_PATH = DATABASE_DIR / "database.db"

def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    return connection