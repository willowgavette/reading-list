from rl_functions import *
import os

# Check storage to see if a list already exists.
# If one does, load it. If one does not, create one.
filename = './reading_list.json'
try:
    book_list = load_l(filename)
except FileNotFoundError:
    create_l()
    
print("\nWelcome to your reading list! You can:")

while True:
    task = options()
    if task == '1':
        # If there are no entries to display, alert user.
        if len(book_list) == 0:
            print("\nThere are no entries to show!\n",
                  columns * '-')
        else:
            full_print(book_list)
    elif task == '2':
        new_book = enter_book()
        book_list.append(new_book)
        print(columns * '-')
    elif task == '3':
        if len(book_list) == 0:
            print("\nThere are no entries to update!\n",
                  columns * '-')
        elif len(book_list) == 1:  # If there is only one book in the list, automatically update that book.
            to_edit = book_list[0]
            to_edit.edit()
            print(columns * '-')
        else:
            edit_num = quick_print(book_list)
            to_edit = book_list[edit_num-1]
            to_edit.edit()
            print(columns * '-')
    elif task == '4':
        if len(book_list) == 0:
            print("\nThere are no entries to review & score!\n",
                  columns * '-')
        elif len(book_list) > 1:
            review_num = quick_print(book_list)
            to_review = book_list[review_num-1]
            if not to_review.info['done']:
                print("You haven't finished this book yet!\n"
                      "Please update the completion status before reviewing.\n",
                      columns * '-')
            else:
                to_review.review()
                print(columns * '-')
        else:
            to_review = book_list[0]
            to_review.review()
            print(columns * '-')
    elif task == '5':
        if len(book_list) == 0:
            print("\nThere are no entries to sort!\n",
                  columns * '-')
        elif len(book_list) == 1:
            print("\nYou can't sort a list with only one entry!\n",
                  columns * '-')
        else:
            choices = ['title', 'author', 'year', 'score high to low', 'score low to high']
            print("You may sort your reading list by:\n"
                  "\t1. Title\n"
                  "\t2. Author\n"
                  "\t3. Year of publication(newest to oldest)\n"
                  "\t4. Score(highest to lowest)\n"
                  "\t5. Score(lowest to highest)")
            choice = int(input("Please enter the number of the option you'd like: "))
            if choice <= 3:
                choice = str(choices[choice-1])
                sort_l(book_list, choice)
            elif 3 < choice > 6:
                sort_l(book_list, choice)
            else:
                print("Invalid input detected! Please try again.\n",
                      columns * '-')
    elif task == '6':
        if len(book_list) == 0:
            print("\nThere are no entries to delete!\n",
                  columns * '-')
        else:
            to_del = quick_print(book_list)
            delete(book_list, to_del)
            print(columns * '-')
    elif task == '7':
        if len(book_list) == 0:
            print("There are no entries to summarize!\n",
                  columns * '-')
        elif len(book_list) == 1:
            to_sum = book_list[0]
            to_sum.summarize()
            print(columns * '-')
        else:
            to_sum = quick_print(book_list)
            book = book_list[to_sum-1]
            book.summarize()
            print(columns * '-')
    elif task == '8':
        # If the user has deleted all entries, erase JSON file where the books are stored.
        if len(book_list) == 0:
            os.remove(filename)
            print("All entries deleted.\n"
                  "Thank you for using our reading list app!\n",
                  columns * '-')
            break
        else:
            save_l(book_list, filename)
            print("List successfully saved!\n",
                  "Thank you for using our reading list app!\n",
                  columns * '-')
            break
    else:
        print("Invalid input detected! Please try again.\n",
              columns * '-')
    