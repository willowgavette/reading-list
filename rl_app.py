from rl_functions import *
from rl_Book import *

# Check storage to see if a list already exists.
# If one does, load it. If one does not, create one.
filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'
try:
    list_of_books = load_list(filename)
except FileNotFoundError:
    list_of_books = []
    print("It looks like this is your very first time using the app!")
    print("Let's get your first book onto the list.")
    new_book = enter_book()
    list_of_books.append(new_book)
    
flag = True
print("\nWelcome to your reading list! You can:")

# Allow user to choose what action they would like to take.
while flag:
    print_options()
    option = input("Please enter the number of the option you'd like: ")
    if option == '1':
        new_book = enter_book()
        list_of_books.append(new_book)
    elif option == '2':
        if len(list_of_books) > 1:
            print_books(list_of_books)
            book_to_edit = int(input("Please enter the number of the book you would like to edit: "))
            edit_entry(list_of_books[book_to_edit - 1])
        else:
            edit_entry(list_of_books[0])
    elif option == '3':
        print_books(list_of_books)
    elif option == '4':
        save_list(list_of_books)
        flag = False
        break
    elif option == '5':
        if len(list_of_books) > 1:
            print_books(list_of_books)
            book_to_review = int(input("Please enter the number of the book you would like to review: "))
            review_book(list_of_books[book_to_review - 1])
        else:
            review_book(list_of_books[0])
    #elif option == '6':
        #sort_list()
    else:
        print("Invalid input detected! Please try again.")
    