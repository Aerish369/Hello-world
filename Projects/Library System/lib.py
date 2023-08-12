# #Creating Library


class Library:
    numbook = 0
    def __init__(self):
        books = []
        Library.numbook += 1

    def addBook(self, book):
        self.book.append(book)

lib1 = Library()
lib1.addBook('Rich dad poor dad')