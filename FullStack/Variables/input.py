import book_app
import os

book_app.print_options()

print("To get out, simply input 'X' ")

s = input()
books = []

while s != 'x' and s != 'X':
     if s =='1':

         books.append(book_app.create_book())

     elif s == '2':
         book_app.save_books(books)
    
     elif s == '3':

         books = book_app.load_books()

     elif s == '4':
         book_app.issue_book(books)
     elif s == '5':
         book_app.return_book(books)
     elif s == '6':    
         book_app.update_book(books)
     elif s == '7':
         book_app.show_all_book(books) 
     elif s == '8':
         book_app.show_book(books)         

     else:
         print("The given command doesn't exist..")
     input("Press enter to continue...")  
            


     os.system("cls")
     book_app.print_options()
     s = input()