from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QHBoxLayout

from logic.bookstore import Bookstore

# PyQt6 UI Class
# --------------------------------
# CHANGE: Created a separate Presentation Layer
# --------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bookstore App")
        self.setGeometry(100, 100, 400, 300)
        
        # Initialize the Business Logic Layer
        self.bookstore = Bookstore()
        self.initUI()
        self.update_book_list()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        self.book_list = QListWidget()
        layout.addWidget(self.book_list)
        
        form_layout = QHBoxLayout()
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title")
        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Author")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Price")
        
        form_layout.addWidget(self.title_input)
        form_layout.addWidget(self.author_input)
        form_layout.addWidget(self.price_input)
        layout.addLayout(form_layout)
        
        add_button = QPushButton("Add Book")
        add_button.clicked.connect(self.add_book)
        layout.addWidget(add_button)
        
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search Book Title")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_book)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)
        
        delete_layout = QHBoxLayout()
        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("Title to delete")
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_book)
        delete_layout.addWidget(self.delete_input)
        delete_layout.addWidget(self.delete_button)
        layout.addLayout(delete_layout)
        
        central_widget.setLayout(layout)
    
    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        price = self.price_input.text()
        
        if title and author and price:
            # Add book to the database
            self.bookstore.add_book(title, author, price)
            self.update_book_list()
            self.title_input.clear()
            self.author_input.clear()
            self.price_input.clear()
    
    def update_book_list(self):
        self.book_list.clear()
        # Fetch books from the database and add to the list
        for book in self.bookstore.get_books():
            self.book_list.addItem(f"{book[1]} by {book[2]} - ${book[3]}")
    
    def search_book(self):
        search_query = self.search_input.text().lower()
        self.book_list.clear()
        # Fetch books from the database and add to the list
        for book in self.bookstore.search_books(search_query):
            self.book_list.addItem(f"{book[1]} by {book[2]} - ${book[3]}")
    
    def delete_book(self):
        delete_query = self.delete_input.text().lower()
        # Delete book from the database
        self.bookstore.delete_book_by_title(delete_query)
        self.update_book_list()
        self.delete_input.clear()
    
    def showEvent(self, event):
        super().showEvent(event)
        self.update_book_list()
