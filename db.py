from flask import g

import sqlite3

DATABASE = 'database.db'

def get_db():
    # Create a database connection in the current thread or reuse the existing one
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def create_tables():
    db = get_db()
    cursor = db.cursor()
    # Create User table
    db.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, hash TEXT NOT NULL)''')

    # Create Todo table
    db.execute('''CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Add the created column with default value
                FOREIGN KEY (user_id) REFERENCES users (id));''')

    cursor.commit()
    cursor.close()

    

#create_tables()
