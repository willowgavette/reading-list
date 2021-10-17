from rl_functions import *
from rl_Book import *

# Create a list of book objects to store the reading list.

list_of_books = load_list()

flag = True

# Allow user to choose what action they would like to take.
while flag:
    print_options()
    option = input("Please enter the number of the option you'd like: ")
    if option == '1':
        new_book = enter_book()
        list_of_books.append(new_book)
    elif option == '2':
        edit_list(list_of_books)
    elif option == '3':
        print_books(list_of_books)
    elif option == '4':
        save_list(list_of_books)
        flag = False
        break
    elif option == '5':
        review_book()
    #elif option == '6':
        #sort_list()
    else:
        print("Invalid input detected! Please try again.")
    