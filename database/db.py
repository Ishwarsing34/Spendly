import sqlite3
import os

DATABASE = 'database.db'

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS."""
    with get_db() as conn:
        # Users Table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Expenses Table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date DATE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        ''')
        conn.commit()

def seed_db():
    """Inserts sample data for development."""
    with get_db() as conn:
        # Sample User
        try:
            conn.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                         ("demo_user", "demo@example.com", "password123"))
            user_id = conn.execute("SELECT id FROM users WHERE username='demo_user'").fetchone()[0]

            # Sample Expenses
            expenses = [
                (user_id, 500.0, 'Food', 'Dinner at restaurant', '2026-10-01'),
                (user_id, 1200.0, 'Bills', 'Electricity bill', '2026-10-02'),
                (user_id, 200.0, 'Transport', 'Uber ride', '2026-10-03'),
                (user_id, 150.0, 'Health', 'Pharmacy', '2026-10-04'),
            ]
            conn.executemany("INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)", expenses)
            conn.commit()
        except sqlite3.IntegrityError:
            pass # Data already seeded
