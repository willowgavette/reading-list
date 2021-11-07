from rl_Book import Book
import json
import shutil

columns, lines = shutil.get_terminal_size()  # Getting size of terminal for pretty printing
columns = int(columns)


def load_l(filename):
    """Load reading list into memory from JSON file."""
    with open(filename, 'r') as book_list:
        t_list = []
        for json_obj in book_list:
            book = json.loads(json_obj)
            loaded_book = Book(**book)
            t_list.append(loaded_book)
        return t_list


def create_l():
    """Create a new list and enter the first book into that list."""
    print("Welcome to the reading list app! Let's get your very first book entered.")
    t_list = []
    new_book = enter_book()
    t_list.append(new_book)
    return t_list


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
    book_number = 1
    for book in book_list:
        print(f"\nBook #{book_number}:\n"
              f"\t-Title: {book.info['title']}\n"
              f"\t-Author: {book.info['author']}\n"
              f"\t-ISBN: {book.info['isbn']}")
        if book.info['year']:
            print(f"\t-Publication year: {book.info['year']}")
        if book.info['isbn']:
            print(f"\t-ISBN: {book.info['isbn']}")
        if book.info['done']:
            print("\t-Completion status: Completed")
            if book.info['review']:
                print("\t-Book review:\n"
                      f"{book.info['review']}")
            else:
                print("You have not reviewed this book yet.")
            if book.info['score']:
                print(f"\t-Score: {book.info['score']}/5")
            else:
                print(f"\t-You have not scored this book yet.")
        else:
            print("\t-Completion status: Not completed")
        print(columns * '-')
        book_number += 1


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


def save_l(book_list, filename):
    """Save the list of books to a JSON file."""
    print("Saving your list...")
    with open(filename, 'w') as f:
        for book in book_list:
            json.dump(book.info, f)
            f.write('\n')


def sort_l(book_list, option):
    """Sort the list of books according to parameters given by the user."""
    if option == 4:
        score_sort(book_list, reverse=True)
    elif option == 5:
        score_sort(book_list)
    else:
        temp_list = []
        for book in book_list:
            temp_var = book.info[option]
            temp_list.append(temp_var)
        temp_list.sort()
        print(f"Here is your reading list sorted by {option}:")
        for item in temp_list:
            for book in book_list:
                if book.info[option] == item:
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


def delete(book_list, to_del):
    """Delete an entry from the reading list."""
    book_list.remove(book_list[to_del-1])
    print("Entry successfully deleted!")
