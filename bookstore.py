from bookstore_repository import BookstoreRepository

# --------------------------------
# CHANGE: Bookstore class now uses the Repository
# --------------------------------
class Bookstore:
    def __init__(self, repository: BookstoreRepository):
        self.repository = repository

    def add_book(self, title, author, price):
        self.repository.add_book(title, author, price)

    def get_books(self):
        return self.repository.get_books()

    def search_books(self, search_query):
        return self.repository.search_books(search_query)

    def delete_book(self, title):
        self.repository.delete_book(title)
# --------------------------------
