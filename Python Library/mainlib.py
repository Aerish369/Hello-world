class Library:
    def __init__(self):
        self.noofbooks = 0
        self.books = []
    
    def addbooks(self, book):
        self.books.append(book)
        self.noofbooks = len(self.books)
    
    def showInfo(self):
        print(f"The no of books is {len(self.books)}. The books are ")
        for book in self.books:
            print(book)

b = Library()
b.addbooks("Rich dad")
b.showInfo()