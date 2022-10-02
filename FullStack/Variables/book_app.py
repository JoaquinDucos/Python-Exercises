from books import Book
import json

def print_options():
    print("Press the specific button for that action")
    print("1- create a new book")
    print("2- save books locally")
    print("3- load books from the disk")
    print("4- issue book")
    print("5- return a book")
    print("6- update a book")
    print("7- show all books")
    print("8- Find book by id")    

def input_book_info():
    id = input("ID: ")
    name = input("NAME: ")
    description = input("DESCRIPTION: ")
    isbn = input("ISBN: ")
    page_count = input("PAGE COUNT: ")
    issued = input("ISSUED:y/Y for True, anything else for False ")
    issued = (issued =="y" or issued == "Y")
    author = input("AUTHOR: ")
    year = int(input("YEAR: "))
    return{

        'id': id,    
        'name' : name,
        'description': description,
        'isbn': isbn,
        'page_count': page_count,
        'issued': issued,
        'author': author,
        'year': year
    }

def create_book():
    print("Please enter your book information: ")    
    book_input = input_book_info()
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    
    print(book.to_dict())
    return book

def save_books(books):
     json_books = []
     for book in books:
         json_books.append(book.to_dict())    
     try:
         file = open("books.dat", "w")    
         file.write(json.dumps(json_books, indent = 4))
     except:
         print("We had an error saving books")    

def load_books():
     books = []
     try:
         file = open("books.dat", "r")
         loaded_books = json.loads(file.read())
         
         for book in loaded_books:
              new_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
              books.append(new_obj)
         print("Succesfully loaded books")    
         return books    
     except:
         print("The file doesn't existe or an error ocurred during loading")

def find_book(books,id):
     for index, book in enumerate(books):
            if book.id == id:
                return index
     return None       

def issue_book(books):
      id = input("Enter the id of the book you want to issue: ")  
      index = find_book(books, id)
      if index != None:
          books[index].issued = True
          print("Book succesfully issued")
      else:
          print("Could not find the book you are looking for")

def return_book(books):
      id = input("Enter the id of the book you want to return: ")  
      index = find_book(books, id)
      if index != None:
          books[index].issued = False
          print("Book succesfully returned")
      else:
          print("Could not find the book you are looking for")
def update_book(books):
    id = input("Enter the ID of book you want to update")
    index = find_book(books,id)
    if index != None:
         new_book = create_book()
         old_book = books[index]
         books[index]= new_book
         del old_book
         print("Book successfully updated")
    else:
        print("We could not find you book") 

def show_all_book(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input("Please enter id of the book")
    index = find_book(books, id)
    if index != None:

        print(books[index].to_dict())
    else:
        print("We couldn't find your book")                      