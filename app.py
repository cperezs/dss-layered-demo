from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QHBoxLayout
import sys

# PyQt6 UI Class with embedded logic
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bookstore App")
        self.setGeometry(100, 100, 400, 300)
        
        # --------------------------------
        # CHANGE: Added sample data for demonstration
        # --------------------------------
        self.books = [
            {"title": "Dune", "author": "Frank Herbert", "price": "9.99"},
            {"title": "Neuromancer", "author": "William Gibson", "price": "8.99"},
            {"title": "Foundation", "author": "Isaac Asimov", "price": "7.99"},
            {"title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "price": "6.99"},
            {"title": "Snow Crash", "author": "Neal Stephenson", "price": "10.99"},
            {"title": "Hyperion", "author": "Dan Simmons", "price": "9.49"},
            {"title": "2001: A Space Odyssey", "author": "Arthur C. Clarke", "price": "8.49"},
            {"title": "Kindred", "author": "Octavia Butler", "price": "7.99"},
            {"title": "Binti", "author": "Nnedi Okorafor", "price": "6.49"},
            {"title": "The Broken Earth", "author": "N.K. Jemisin", "price": "9.99"},
            {"title": "A Door Into Ocean", "author": "Joan Slonczewski", "price": "8.79"},
            {"title": "China Mountain Zhang", "author": "Maureen F. McHugh", "price": "7.59"}
        ]
        # --------------------------------
        self.initUI()

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
        
        # --------------------------------
        # CHANGE: Added search text input and button
        # --------------------------------
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search Book Title")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_book)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)
        # --------------------------------
        
        central_widget.setLayout(layout)
    
    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        price = self.price_input.text()
        
        if title and author and price:
            self.books.append({"title": title, "author": author, "price": price})
            self.update_book_list()
            self.title_input.clear()
            self.author_input.clear()
            self.price_input.clear()
    
    def update_book_list(self):
        self.book_list.clear()
        for book in self.books:
            self.book_list.addItem(f"{book['title']} by {book['author']} - ${book['price']}")
    
    # --------------------------------
    # CHANGE: Added search functionality
    # --------------------------------
    def search_book(self):
        search_query = self.search_input.text().lower()
        self.book_list.clear()
        for book in self.books:
            if search_query in book['title'].lower():
                self.book_list.addItem(f"{book['title']} by {book['author']} - ${book['price']}")
    # --------------------------------

    # --------------------------------
    # CHANGE: Load data when window is shown
    # --------------------------------
    def showEvent(self, event):
        super().showEvent(event)
        self.update_book_list()
    # --------------------------------

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
