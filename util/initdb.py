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
            price REAL NOT NULL,
            cover_url TEXT
        )
    """)
    
    # Sample book data with cover URLs
    books = [
        ("Dune", "Frank Herbert", 9.99, "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458.jpg"),
        ("Neuromancer", "William Gibson", 8.99, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR56DSVumdbiIkgbtFlR7eeiQlIWCD3gew4vA&s"),
        ("Foundation", "Isaac Asimov", 7.99, "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1417900846i/29579.jpg"),
        ("The Left Hand of Darkness", "Ursula K. Le Guin", 6.99, "https://m.media-amazon.com/images/I/514gzABfjwL._AC_UF1000,1000_QL80_.jpg"),
        ("Snow Crash", "Neal Stephenson", 10.99, "https://m.media-amazon.com/images/I/81p4Y+0HzbL.jpg"),
        ("Hyperion", "Dan Simmons", 9.49, "https://m.media-amazon.com/images/I/91Ky9KCfAIL._UF1000,1000_QL80_.jpg"),
        ("2001: A Space Odyssey", "Arthur C. Clarke", 8.49, "https://m.media-amazon.com/images/I/61lJNV04+wL._AC_UF1000,1000_QL80_.jpg"),
        ("Kindred", "Octavia Butler", 7.99, "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1339423248i/60931.jpg"),
        ("Binti", "Nnedi Okorafor", 6.49, "https://m.media-amazon.com/images/I/81v0QRdZAnL._SL1500_.jpg"),
        ("The Broken Earth", "N.K. Jemisin", 9.99, "https://m.media-amazon.com/images/I/91l4PotA0kL.jpg"),
        ("A Door Into Ocean", "Joan Slonczewski", 8.79, "https://mpd-biblio-covers.imgix.net/9780312876524.jpg"),
        ("China Mountain Zhang", "Maureen F. McHugh", 7.59, "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1346669090i/836964.jpg")
    ]
    
    # Insert sample books
    cursor.executemany("INSERT INTO books (title, author, price, cover_url) VALUES (?, ?, ?, ?)", books)
    conn.commit()
    conn.close()
    print("Database initialized with sample data.")

if __name__ == "__main__":
    init_db()
