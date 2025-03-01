import sqlite3

conn = sqlite3.connect("coffee.sqlite")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS coffee (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roast_level TEXT NOT NULL,
    type TEXT NOT NULL,
    taste_description TEXT,
    price REAL NOT NULL,
    package_size INTEGER NOT NULL
)
""")

conn.commit()
conn.close()