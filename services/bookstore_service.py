from logic.bookstore import Bookstore

# --------------------------------
# CHANGE: BookstoreService offers extended functionalities related to the Bookstore
# --------------------------------
class BookstoreService:
    def __init__(self):
        self.bookstore = Bookstore()
        self.user_discounts = {  # Example user-based discount mapping
            "regular": 0.0,
            "member": 0.1,  # 10% discount
            "vip": 0.2  # 20% discount
        }
    
    def get_discounted_price(self, user_type, price):
        discount = self.user_discounts.get(user_type.lower(), 0.0)
        return round(price * (1 - discount), 2)
    
    def get_books(self, user_type="regular"):
        books = self.bookstore.get_books()
        return [(id, title, author, self.get_discounted_price(user_type, price), cover_url) for id, title, author, price, cover_url in books]

    def search_books(self, search_query, user_type="regular"):
        books = self.bookstore.search_books(search_query)
        return [(id, title, author, self.get_discounted_price(user_type, price), cover_url) for id, title, author, price, cover_url in books]
    
    def add_book(self, title, author, price):
        self.bookstore.add_book(title, author, price)
    
    def delete_book_by_title(self, title):
        self.bookstore.delete_book(title)
    
    def delete_book_by_id(self, book_id):
        self.bookstore.delete_book_by_id(book_id)
# --------------------------------
