from flask import Flask, jsonify, request
from flask_cors import CORS

from logic.bookstore import Bookstore

app = Flask(__name__)
CORS(app)  # Enable CORS to allow local calls

# Initialize repository and bookstore
bookstore = Bookstore()

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(bookstore.get_books())

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = bookstore.get_book(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    if not all(key in data for key in ("title", "author", "price", "cover_url")):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_book_id = bookstore.add_book(data["title"], data["author"], data["price"], data["cover_url"])
    return jsonify({"id": new_book_id, **data}), 201

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    bookstore.delete_book_by_id(book_id)
    return jsonify({"message": "Book deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
