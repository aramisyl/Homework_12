class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def read(self, pages_read):
        percent_read = pages_read/self.pages * 100
        print(f"Прочитано {percent_read} процентов книги.")
class Library:

    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)