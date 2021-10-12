from rl_Book import Book

def enter_book():

    active = True
    while active:
        print("\nPlease enter some information on the book you'd like to add.")

        title = input("Title: ")
        author = input("Author: ")
        year = input("Publication year: ")
        isbn = input("ISBN: ")

        print(f"The information you entered is as follows:")
        print(f"\tTitle: {title}")
        print(f"\tAuthor: {author}")
        print(f"\tPublication year: {year}")
        print(f"\tISBN: {isbn}")
        cont = input("Is this correct? (y/n): ")
        if cont.lower() != 'n':
            active = False
            new_book = Book(title, author, year, isbn)
            return new_book  

def print_options():
    print("Welcome to your reading list! You can:")
    print("\n1. Enter a new book")
    print("\n2. Update information on a book already in the list")
    print("\n3. Check your complete reading list")
    print("\n4. Save and quit")

list_of_books = []

flag = True
while flag:

    print_options()
    option = input("Please enter the number of the option you'd like: ")
    option = int(option)
    if option == 1:
        new_book = enter_book()
        list_of_books.append(new_book)
    elif option == 2:
        break
    elif option == 3:
        break
    elif option == 4:
        break
    else:
        print("Invalid input detected.")
        print_options()
