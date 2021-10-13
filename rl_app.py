from rl_functions import *

import csv

# Create a list of book objects to store the reading list.
list_of_books = []

flag = True

# Allow user to choose what action they would like to take.
while flag:
    print_options()
    option = input("Please enter the number of the option you'd like: ")
    if option == '1':
        new_book = enter_book()
        list_of_books.append(new_book)
    elif option == '2':
        break
    elif option == '3':
        print_books(list_of_books)
    elif option == '4':
        filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.csv'
        print("Saving your list...")
        with open(filename, 'a') as r_l:
            for book in list_of_books:
                r_l.write(f"\n{book.title}")
                r_l.write(f"\n{book.author}")
                r_l.write(f"\n{book.year}")
                r_l.write(f"\n{book.isbn}")
                when_entered = str(book.when_entered)
                finished_book = str(book.finished_book)
                r_l.write(f"\n{when_entered}")
                r_l.write(f"\n{finished_book}")
            print("List successfully saved!")
        print("Thank you for using our reading list app!")
        flag = False
        break
    else:
        print("***Invalid input detected! Please try again.***")
    