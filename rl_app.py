from rl_functions import *
from rl_Book import *

filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'

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
        print("Saving your list...")
        with open(filename, 'w') as reading_list:
            for book in list_of_books:
                json.dump(book.book_info, reading_list)
                reading_list.write('\n')
            print("List successfully saved!")
        print("Thank you for using our reading list app!")
        flag = False
        break
    else:
        print("Invalid input detected! Please try again.")
    