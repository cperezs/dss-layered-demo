from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel, QHBoxLayout
import sys

# PyQt6 UI Class with embedded logic
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bookstore App")
        self.setGeometry(100, 100, 400, 300)
        
        self.books = []
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

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
