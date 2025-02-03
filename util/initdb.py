import os
import sqlite3

# Initialize database and populate with sample data
def init_db():
    if os.path.exists("books.db"):
        os.remove("books.db")
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    
    # Create books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    
    # Sample book data
    books = [
        ("Dune", "Frank Herbert", 9.99),
        ("Neuromancer", "William Gibson", 8.99),
        ("Foundation", "Isaac Asimov", 7.99),
        ("The Left Hand of Darkness", "Ursula K. Le Guin", 6.99),
        ("Snow Crash", "Neal Stephenson", 10.99),
        ("Hyperion", "Dan Simmons", 9.49),
        ("2001: A Space Odyssey", "Arthur C. Clarke", 8.49),
        ("Kindred", "Octavia Butler", 7.99),
        ("Binti", "Nnedi Okorafor", 6.49),
        ("The Broken Earth", "N.K. Jemisin", 9.99),
        ("A Door Into Ocean", "Joan Slonczewski", 8.79),
        ("China Mountain Zhang", "Maureen F. McHugh", 7.59)
    ]
    
    # Insert sample books
    cursor.executemany("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", books)
    conn.commit()
    conn.close()
    print("Database initialized with sample data.")

if __name__ == "__main__":
    init_db()
