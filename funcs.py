from book import Book
import json
import shutil
import os

columns, lines = shutil.get_terminal_size()  # Getting size of terminal for pretty printing
columns = int(columns)


def load_l(filename):
    """Load reading list into memory from JSON file."""
    with open(filename, 'r') as book_list:
        t_list = []
        books = json.load(book_list)
        for i in books:
            new_book = Book(**i)
            t_list.append(new_book)
        return t_list


def create_l():
    """Create a new list and enter the first book into that list."""
    print("Welcome to the reading list app! Let's get your very first book entered.")
    t_list = []
    new_book = enter_book()
    t_list.append(new_book)
    return t_list


def save_l(book_list, filename):
    """Save the list of books to a JSON file."""
    json_list = []
    for book in book_list:
        temp = book.to_json()
        json_list.append(temp)
    with open(filename, 'w') as f:
        json.dump(json_list, f, indent=4)


def main(book_list, filename):
    """Give user available actions, prompt for input, and process and direct that input."""
    task = options()
    if task == '1':
        # If there are no entries to display, alert user.
        if not book_list:
            print("\nThere are no entries to show!\n",
                  columns * '-')
        elif len(book_list) == 1:
            book_list[0].print()
        else:
            full_print(book_list)
    elif task == '2':
        new_book = enter_book()
        book_list.append(new_book)
        print(columns * '-')
    elif task == '3':
        if not book_list:
            print("\nThere are no entries to update!\n",
                  columns * '-')
        elif len(book_list) == 1:  # If there is only one book in the list, automatically update that book.
            book_list[0].edit()
            print(columns * '-')
        else:
            edit_num = quick_print(book_list)
            book_list[edit_num-1].edit()
            print(columns * '-')
    elif task == '4':
        if not book_list:
            print("\nThere are no entries to review & score!\n",
                  columns * '-')
        elif len(book_list) == 1:
            book_list[0].review()
            print(columns * '-')
        else:
            review_num = quick_print(book_list)
            if not book_list[review_num-1]:
                print("You haven't finished this book yet!\n"
                      "Please update the completion status before reviewing.\n",
                      columns * '-')
            else:
                book_list[review_num-1].review()
                print(columns * '-')
    elif task == '5':
        if not book_list:
            print("\nThere are no entries to sort!\n",
                  columns * '-')
        elif len(book_list) == 1:
            print("\nYou can't sort a list with only one entry!\n",
                  columns * '-')
        else:
            print("You may sort your reading list by:\n"
                  "\t1. Title\n"
                  "\t2. Author\n"
                  "\t3. Year of publication(newest to oldest)\n"
                  "\t4. Score(highest to lowest)\n"
                  "\t5. Score(lowest to highest)")
            choice = int(input("Please enter the number of the option you'd like: "))
            if 0 < choice < 6:
                sort_l(book_list, choice-1)
            else:
                print("Invalid input detected! Please try again.\n",
                      columns * '-')
    elif task == '6':
        if not book_list:
            print("\nThere are no entries to delete!\n",
                  columns * '-')
        elif len(book_list) == 1:
            delete(book_list[0])
        else:
            to_del = quick_print(book_list)
            delete(book_list, to_del)
            print(columns * '-')
    elif task == '7':
        if not book_list:
            print("There are no entries to summarize!\n",
                  columns * '-')
        elif len(book_list) == 1:
            book_list[0].summarize()
            print(columns * '-')
        else:
            to_sum = quick_print(book_list)
            book_list[to_sum-1].summarize()
            print(columns * '-')
    elif task == '8':
        # If the user has deleted all entries, erase JSON file where the books are stored.
        if not book_list:
            os.remove(filename)
            print("All entries deleted.\n"
                  "Thank you for using our reading list app!\n",
                  columns * '-')
            quit()
        else:
            print("Saving your list...")
            save_l(book_list, filename)
            print("List successfully saved!\n",
                  "Thank you for using our reading list app!\n",
                  columns * '-')
            quit()
    else:
        print("Invalid input detected! Please try again.\n",
              columns * '-')
    main(book_list, filename)


def enter_book():
    """Create a new book object and store user-entered info. Return created object."""
    print("\nPlease enter some information on the book you'd like to add.")
    # Create temporary dictionary to pass to the Book() class.
    temp_dict = {
        'title': input("Title: "),
        'author': input("Author: "),
        'year': input("Publication year: "),
        'isbn': input("ISBN: "),
    }
    if temp_dict['title'] == '' or temp_dict['author'] == '':
        print("You must enter a title and author!")
        enter_book()

    # Check to make sure user entered the information correctly
    print("The information you entered is as follows:")
    print(
        f"\tTitle: {temp_dict['title']}\n"
        f"\tAuthor: {temp_dict['author']}\n"
        f"\tPublication year: {temp_dict['year']}\n"
        f"\tISBN: {temp_dict['isbn']}\n"
    )
    cont = input("Is this correct? (y/n): ")
    if cont.lower().strip() == 'y':
        new_book = Book(**temp_dict)
        return new_book
    elif cont.lower().strip() == 'n':
        enter_book()
    else:
        print("Invalid input detected! Please try again.")
        enter_book()


def options():  
    """Print the list of options the user can choose from."""
    print("1. Check your full reading list\n"
          "2. Enter a new book\n"
          "3. Update a book entry\n"
          "4. Review and score a book\n"
          "5. Sort your reading list\n"
          "6. Delete an entry from the list\n"
          "7. Get Wikipedia.org summary for a book\n"
          "8. Save and quit")
    option = input("Please enter the number of the option you'd like: ")
    print(columns * '-')
    return option.strip()


def full_print(book_list):
    """Print the entire saved list of books."""
    num = 1
    for book in book_list:
        print(f"Book #{num}:")
        book.print()
        print(columns * '-')
        num += 1


def quick_print(book_list):
    """Print out one-line string containing a book's title and author, used for book selection."""
    book_num = 1
    for book in book_list:
        print(
            f"Book #{book_num}:",
            str(book),
        )
        book_num += 1
    choice = int(input("Please enter the number of the book you want: "))
    return choice


def sort_l(book_list, option):
    """Sort the list of books according to parameters given by the user."""
    options = ['title', 'author', 'year']
    if option == 3:
        score_sort(book_list, reverse=True)
    elif option == 4:
        score_sort(book_list)
    else:
        temp_list = []
        for book in book_list:
            temp_var = book.info[options[option]]
            temp_list.append(temp_var)
        temp_list.sort()
        print(f"Here is your reading list sorted by {options[option]}:")
        for item in temp_list:
            for book in book_list:
                if book.info[options[option]] == item:
                    book.print()
                    print(columns * '-')


def score_sort(book_list, reverse=False):
    """Minor function to sort book list by score. Reverse option flips the sort."""
    score_list = []
    for num in range(1, 6):
        for book in book_list:
            if book.info['score'] == num:
                score_list.append(book)
    if reverse:
        score_list.reverse()
        print("Here is your reading list sorted by score, from highest to lowest:")
        full_print(score_list)
    else:
        print("Here is your reading list sorted by score, from lowest to highest:")
        full_print(score_list)


def delete(book_list, to_del=''):
    """Delete an entry from the reading list."""
    if to_del:
        book_list.remove(book_list[to_del-1])
    else:
        book_list.pop()
    print("Entry successfully deleted!")
