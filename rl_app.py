from rl_functions import *
import os

# Check storage to see if a list already exists.
# If one does, load it. If one does not, create one.
filename = './reading_list.json'
try:
    book_list = load_l(filename)
except FileNotFoundError:
    create_l(filename)
    
print("\nWelcome to your reading list! You can:")

while True:
    task = options()
    if task == '1':
        # If there are no entries to display, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to show!")
        else:
            print_l(book_list)
    elif task == '2':
        new_book = enter_book()
        book_list.append(new_book)
    elif task == '3':
        if len(book_list) == 0:
            print("\nThere are no entries to update!")
        elif len(book_list) > 1:
            print_l(book_list)
            edit_num = int(input("Please enter the number of the book you would like to edit: "))
            edit(book_list[edit_num - 1])
        else:  # If there is only one book in the list, automatically update that book.
            edit(book_list[0])
    elif task == '4':
        if len(book_list) == 0:
            print("\nThere are no entries to review & score!")
        elif len(book_list) > 1:
            print_l(book_list)
            review_num = int(input("Please enter the number of the book you would like to review: "))
            review(book_list[review_num-1])
        else:
            review(book_list[0])          
    elif task == '5':
        if len(book_list) == 0:
            print("\nThere are no entries to sort!")
        elif len(book_list) > 1:
            print("You may sort your reading list by:\n"
                  "\t1. Title\n"
                  "\t2. Author\n"
                  "\t3. Year of publication(newest to oldest)\n"
                  "\t4. Year of publication(oldest to newest)\n"
                  "\t5. Score(highest to lowest)\n"
                  "\t6. Score(lowest to highest)")
            option = input("Please enter the number of the option you'd like: ")
            sort_l(book_list, option)
        else:
            print("\nYou can't sort a list with only one entry!")
    elif task == '6':
        if len(book_list) == 0:
            print("\nThere are no entries to delete!")
        else:
            print_l(book_list)
            to_del = input("Please enter the number of the entry you would like to delete: ")
            to_del = int(to_del)
            delete(book_list, to_del)
    elif task == '7':
        if len(book_list) == 0:
            print("There are no entries to summarize!")
        elif len(book_list) == 1:
            get_summary(book_list[0])
        else:
            print_l(book_list)
            to_sum = input("Please enter the number of the book you'd like to summarize: ")
            to_sum = int(to_sum)
            get_summary(book_list[to_sum-1])
    elif task == '8':
        # If the user has deleted all entries, erase JSON file where the books are stored.
        if len(book_list) == 0:
            os.remove(filename)
            print("All entries deleted.\n"
                  "Thank you for using our reading list app!")
            break
        else:
            save_l(book_list)
            print("Thank you for using our reading list app!")
            break
    else:
        print("Invalid input detected! Please try again.")
    