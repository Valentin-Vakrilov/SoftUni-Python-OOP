class Library:
    def __init__(self):
        self.books = []

    def find_book(self, title):
        for book in self.books:
            if book == title:
                return book
