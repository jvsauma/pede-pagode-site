from backend.database.connection import get_connection




SCHEMA = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_users_email ON users(email);

CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist TEXT NOT NULL,
    genre TEXT NOT NULL,
    likes INTEGER DEFAULT 0,
    dislikes INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS song_request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name TEXT NOT NULL,
    song_name TEXT NOT NULL,
    observation TEXT,
    status TEXT DEFAULT 'Pendente',
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS membership_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'PENDING',
    requested_at TEXT NOT NULL,
    reviewed_by INTEGER,
    reviewed_at TEXT,
    user_id INTEGER
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_membership_requests_email
    ON membership_requests(email)
    WHERE status != 'REJECTED';


"""




def init_db():

    connection = get_connection()

    connection.executescript(SCHEMA)

    connection.commit()

    connection.close()