from rl_Book import Book
import json

def enter_book():
    
    """Create a new book object and store user-entered info. Return created object."""
    active = True
    while active:
        print("\nPlease enter some information on the book you'd like to add.")

        # Create temporary variables to pass to the Book() class.
        title = input("Title: ")
        author = input("Author: ")
        year = input("Publication year: ")
        isbn = input("ISBN: ")

        # Check to make sure user entered the information correctly.
        print("The information you entered is as follows:")
        print(f"\tTitle: {title}")
        print(f"\tAuthor: {author}")
        print(f"\tPublication year: {year}")
        print(f"\tISBN: {isbn}")
        cont = input("Is this correct? (y/n): ")
        if cont.lower() == 'y':
            active = False
            new_book = Book(title, author, year, isbn)
            return new_book  
        elif cont.lower() == 'n':
            continue
        else:
            print("Invalid input detected! Please try again.")

def print_options():
    
    """Print the list of options the user can choose from."""
    print("\nWelcome to your reading list! You can:")
    print("\n1. Enter a new book")
    print("\n2. Update information on a book already in the list")
    print("\n3. Check your complete reading list")
    print("\n4. Save and quit")
    
def print_books(list_of_books):
    """Print the saved list of books."""
    
    book_number = 1
    for book in list_of_books:
        print(f"Book #{book_number}:")
        print(f"\t-Title: {book.book_info['title']}")
        print(f"\t-Author: {book.book_info['author']}")
        print(f"\t-Publication year: {book.book_info['year']}")
        print(f"\t-ISBN: {book.book_info['isbn']}\n")
        print(f"This book was entered into the app on {book.book_info['day']}.")
        if book.book_info['finished'] == True:
            print("You have finished reading this book! Good job :)")
        else:
            print("You have not finished reading this book yet.")
        book_number += 1
        
def load_list():
    """Load reading list into memory from JSON file."""
    filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'
    with open(filename, 'r') as book_list:
        temp_list = []
        for json_obj in book_list:
            temp_book = json.loads(json_obj)
            loaded_book = Book(temp_book['title'], temp_book['author'], temp_book['year'], temp_book['isbn'], temp_book['day'])
            temp_list.append(loaded_book)
        return temp_list
    
def edit_list(list_of_books):
    print_books()
    list_position = input("Please enter the number of the book you would like to edit: ")
    