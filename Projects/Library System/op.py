# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class library:
  def __init__(self):
    self.no_of_books = 0
    self.books = []

class library1(library): #class libray to manage books

  #function to add new books
  def addBook(self):
    self.bookName = input("Enter book name: ")
    self.price = int(input("Enter price of book: "))
    self.books.append([self.bookName,self.price]) 
    f = open("booklist.txt",'a')
    for book in self.books:
      f.write(f"book name: {book[0]}\tprice: {book[1]}\n")
    f.close()


  #function to display all books availible
  def showBook(self):
    self.Bname = []
    f = open("booklist.txt","r")
    while True:
      line = f.readlines()
      if not line:
        break
      for data in line:
        print (data)

  #functiion to display how many number of books are availible
  def number_of_books(self):
    f = open("booklist.txt","r")
    while True:
      line = f.readlines()
      if not line:
        break
      print("total number of books are: ",len(line))

  #function to search a perticular book
  def searchBook(self):
    flag = 0
    Search = input("Enter Book name to search: ")
    f = open("booklist.txt","r")
    while True:
      line = f.readlines()
      if not line:
        break
      for data in line:
        if Search in data:
          print(f"Book is found.\n{data}")
          flag = 1
      if(flag == 0):
        print("book not found.")

#menu driven program
while True:
  obj=library1()
  userINP = int(input("\n\nMENU\n1.add a book\n2.print all books\n3.search book\n4.number of books\n5.exit\nEnter choice: "))

  print("\n")
  
  if(userINP==1):  #to add book
    obj.addBook()
    
  elif(userINP==2):  #to display all books
    obj.showBook()
    
  elif(userINP==3):  #to search book
    obj.searchBook()
    
  elif(userINP==4):  #to display total number of books
    obj.number_of_books()
    
  elif(userINP==4):  #to exit from loop
    break