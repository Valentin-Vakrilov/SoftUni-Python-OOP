from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, content: str):
        self.content = content


class Formatter(Book, ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class Printer(Formatter):
    def format(self, book: Book) -> str:
        return book.content

    def get_book(self, book: Book):
        return format(book)
