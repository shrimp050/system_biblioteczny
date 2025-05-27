from library import add_book, search_book, borrow_book, return_book, remove_book

# Testy add_book
def test_add_book_success():
    lib = {}
    assert add_book(lib, 1, "1984", "Orwell") == "Book added"

def test_add_book_duplicate():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    assert add_book(lib, 1, "1984", "Orwell") == "Book already exists"

def test_add_book_multiple():
    lib = {}
    add_book(lib, 1, "Book A", "Author A")
    add_book(lib, 2, "Book B", "Author B")
    assert len(lib) == 2

def test_add_book_data_check():
    lib = {}
    add_book(lib, 3, "Brave New World", "Huxley")
    assert lib[3]["author"] == "Huxley"

# Testy search_book
def test_search_book_found():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    assert len(search_book(lib, "1984")) == 1

def test_search_book_not_found():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    assert len(search_book(lib, "Brave")) == 0

def test_search_book_partial_match():
    lib = {1: {"title": "Brave New World", "author": "Huxley", "available": True}}
    assert len(search_book(lib, "brave")) == 1

def test_search_book_case_insensitive():
    lib = {1: {"title": "The Hobbit", "author": "Tolkien", "available": True}}
    assert len(search_book(lib, "hobbit")) == 1

# Testy borrow_book
def test_borrow_book_success():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    assert borrow_book(lib, 1) == "Book borrowed"

def test_borrow_book_not_found():
    lib = {}
    assert borrow_book(lib, 1) == "Book not found"

def test_borrow_book_unavailable():
    lib = {1: {"title": "1984", "author": "Orwell", "available": False}}
    assert borrow_book(lib, 1) == "Book not available"

def test_borrow_book_flag_changes():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    borrow_book(lib, 1)
    assert lib[1]["available"] is False

# Testy return_book
def test_return_book_success():
    lib = {1: {"title": "1984", "author": "Orwell", "available": False}}
    assert return_book(lib, 1) == "Book returned"

def test_return_book_not_found():
    lib = {}
    assert return_book(lib, 1) == "Book not found"

def test_return_book_not_borrowed():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    assert return_book(lib, 1) == "Book was not borrowed"

def test_return_book_flag_changes():
    lib = {1: {"title": "1984", "author": "Orwell", "available": False}}
    return_book(lib, 1)
    assert lib[1]["available"] is True

# Testy remove_book
def test_remove_book_success():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    assert remove_book(lib, 1) == "Book removed"

def test_remove_book_not_found():
    lib = {}
    assert remove_book(lib, 1) == "Book not found"

def test_remove_book_effect():
    lib = {1: {"title": "1984", "author": "Orwell", "available": True}}
    remove_book(lib, 1)
    assert 1 not in lib

def test_remove_book_multiple():
    lib = {
        1: {"title": "Book A", "author": "A", "available": True},
        2: {"title": "Book B", "author": "B", "available": True},
    }
    remove_book(lib, 2)
    assert len(lib) == 1
