import sqlite3

# --------------------------------
# CHANGE: Created a separate Business Logic Layer
# --------------------------------
class Bookstore:
    def __init__(self, db_path="books.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def add_book(self, title, author, price):
        self.cursor.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
        self.conn.commit()

    def get_books(self):
        self.cursor.execute("SELECT title, author, price FROM books")
        return self.cursor.fetchall()

    def search_books(self, search_query):
        self.cursor.execute("SELECT title, author, price FROM books WHERE LOWER(title) LIKE ?", (f"%{search_query}%",))
        return self.cursor.fetchall()

    def delete_book(self, title):
        self.cursor.execute("DELETE FROM books WHERE LOWER(title) = ?", (title.lower(),))
        self.conn.commit()
# --------------------------------
