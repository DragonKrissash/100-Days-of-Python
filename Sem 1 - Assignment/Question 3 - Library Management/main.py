from books import Books
from user import User
import time
in_the_library=True
book=Books()
user=User()
print('----------Welcome to our library!----------')
while in_the_library:
    print('\nWhat would you like to do?'
          '\n1) Add user'
          '\n2) Show books'
          '\n3) Show availability of a specific book'
          '\n4) Add a book'
          '\n5) Remove a book'
          '\n6) Borrow a book'
          '\n7) Return a book'
          '\n8) Extend due date'
          '\n9) Exit the library')
    print('\nEnter your choice from 1 - 9: ')
    choice=int(input())

    if choice==1:
        print('Enter your name and id: ')
        name=input()
        id=input()
        user.addUser(name,id)

    elif choice == 2:
        book.showBooks()

    elif choice == 3:
        print('Please enter the title of the book you are searching: ')
        title=input()
        book.showAvailability(title)

    elif choice == 4:
        print('Please enter the name of the author and title of the book: ')
        author=input()
        title=input()
        book.addBook(author,title)

    elif choice == 5:
        print('Please enter the name of the author and title of the book: ')
        author = input()
        title = input()
        book.removeBook(author,title)

    elif choice == 6:
        print("Please enter your user name, title of the book and author's name: ")
        user_name=input()
        title=input()
        author=input()
        user.bookBorrowed(user_name,title,author)

    elif choice == 7:
        print("Please enter your user name, title of the book and author's name: ")
        user_name = input()
        title = input()
        user.bookReturned(user_name, title)

    elif choice == 8:
        print("Please enter your user name, title of the book and author's name: ")
        user_name = input()
        title = input()
        author = input()
        user.extendDue(user_name, title)


    elif choice == 9:
        print('Thank you!\nVisit Again!')
        in_the_library=False

    else:
        print('Wrong input!\nPlease give correct choice!')