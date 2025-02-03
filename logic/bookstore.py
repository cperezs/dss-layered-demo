from repositories.bookstore_repository import BookstoreRepository

# --------------------------------
# CHANGE: Bookstore class now uses the Repository
# --------------------------------
class Bookstore:
    def __init__(self):
        self.repository = BookstoreRepository()

    def add_book(self, title, author, price):
        self.repository.add_book(title, author, price)

    def get_books(self):
        return self.repository.get_books()

    def search_books(self, search_query):
        return self.repository.search_books(search_query)

    def delete_book_by_title(self, title):
        self.repository.delete_book_by_title(title)
    
    def delete_book_by_id(self, book_id):
        self.repository.delete_book_by_id(book_id)
# --------------------------------
