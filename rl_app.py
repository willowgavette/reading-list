from rl_functions import *
from rl_Book import *
import os

# Check storage to see if a list already exists.
# If one does, load it. If one does not, create one.
filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'
try:
    book_list = load_list(filename)
except FileNotFoundError:
    book_list = []
    print("It looks like this is your very first time using the app! As such, let's get your first book entered.")
    new_book = enter_book()
    book_list.append(new_book)
    
print("\nWelcome to your reading list! You can:")

while True:
    options()
    task = input("Please enter the number of the option you'd like: ")
    if task.strip() == '1':
        # If there are no entries to display, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to show!")
        else:
            print_l(book_list)
    elif task.strip() == '2':
        new_book = enter_book()
        book_list.append(new_book)
    elif task.strip() == '3':
        # If there are no entries to update, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to update!")
        # If there is only one book in the list, automatically update that book.
        elif len(book_list) > 1:
            print_l(book_list)
            edit_num = int(input("Please enter the number of the book you would like to edit: "))
            edit(book_list[edit_num-1])
        else:
            edit(book_list[0])
    elif task.strip() == '4':
        # If there are no entries to review & score, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to review & score!")
        # If there is only one book in the list, automatically review & score that book.
        elif len(book_list) > 1:
            print_l(book_list)
            review_num = int(input("Please enter the number of the book you would like to review: "))
            review(book_list[review_num-1])
        else:
            review(book_list[0])          
    elif task.strip() == '5':
        # If there are no entries to sort, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to sort!")
        # If there is only one book in the list, alert user.
        if len(book_list) > 1:
            print("\nYou can't sort a list with only one entry!")
        else:
            sort_l(book_list)
    elif task.strip() == '6':
        # If the list is empty, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to delete!")
        else:
         delete(book_list)
    elif task.strip() == '7':
        # If the user has deleted all entries, erase JSON file where the books are stored.
        if len(book_list) == 0:
            os.remove(filename)
            print("All entries deleted.")
            print("Thank you for using our reading list app!")
            break
        else:
            save_list(book_list)
            break
    else:
        print("Invalid input detected! Please try again.")
    