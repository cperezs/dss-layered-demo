import sqlite3

# --------------------------------
# CHANGE: Created a separate Data Access Layer
# --------------------------------
class BookstoreRepository:
    def __init__(self, db_path="books.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def add_book(self, title, author, price):
        self.cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
        self.conn.commit()

    def get_books(self):
        self.cursor.execute("SELECT id, title, author, price, cover_url FROM books")
        return self.cursor.fetchall()

    def search_books(self, search_query):
        self.cursor.execute("SELECT id, title, author, price, cover_url FROM books WHERE LOWER(title) LIKE ?", (f"%{search_query}%",))
        return self.cursor.fetchall()

    def delete_book_by_title(self, title):
        self.cursor.execute("DELETE FROM books WHERE LOWER(title) = ?", (title.lower(),))
        self.conn.commit()

    def delete_book_by_id(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.conn.commit()
