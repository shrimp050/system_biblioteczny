def add_book(library, book_id, title, author):
    if book_id in library:
        return "Book already exists"
    library[book_id] = {"title": title, "author": author, "available": True}
    return "Book added"

def search_book(library, title):
    return [book for book in library.values() if title.lower() in book["title"].lower()]

def borrow_book(library, book_id):
    if book_id not in library:
        return "Book not found"
    if not library[book_id]["available"]:
        return "Book not available"
    library[book_id]["available"] = False
    return "Book borrowed"

def return_book(library, book_id):
    if book_id not in library:
        return "Book not found"
    if library[book_id]["available"]:
        return "Book was not borrowed"
    library[book_id]["available"] = True
    return "Book returned"

def remove_book(library, book_id):
    if book_id in library:
        del library[book_id]
        return "Book removed"
    return "Book not found"