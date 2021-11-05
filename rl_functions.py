from rl_Book import Book
import json
import shutil
import wikipediaapi

columns, lines = shutil.get_terminal_size()  # Getting size of terminal for pretty printing
columns = int(columns)
wiki = wikipediaapi.Wikipedia('en')  # Creating a wikipedia object for wikipedia summaries


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


def enter_book(title='', author=''):
    """Create a new book object and store user-entered info. Return created object."""
    if title and author:
        new_book = Book(title, author)
        return new_book
    else:
        print("\nPlease enter some information on the book you'd like to add.")
        # Create temporary dictionary to pass to the Book() class.
        dict = {
            'title': input("Title: "),
            'author': input("Author: "),
            'year': input("Publication year: "),
            'isbn': input("ISBN: "),
        }
        if dict['title'] == '' or dict['author'] == '':
            print("You must enter a title and author!")
            enter_book()

        # Check to make sure user entered the information correctly
        print("The information you entered is as follows:")
        print(
            f"\tTitle: {dict['title']}\n"
            f"\tAuthor: {dict['author']}\n"
            f"\tPublication year: {dict['year']}\n"
            f"\tISBN: {dict['isbn']}\n"
        )
        cont = input("Is this correct? (y/n): ")
        if cont.lower().strip() == 'y':
            new_book = Book(**dict)
            print(columns * '-')
            return new_book
        elif cont.lower().strip() == 'n':
            enter_book()     
        else:
            print("Invalid input detected! Please try again.")
            enter_book()


def options():  
    """Print the list of options the user can choose from."""
    print("1. Check your reading list\n"
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


def print_l(book_list):
    """Print the entire saved list of books."""
    book_number = 0
    for book in book_list:
        book_number += 1
        print(f"\nBook #{book_number}:\n"
              f"\t-Title: {book.info['title']}\n"
              f"\t-Author: {book.info['author']}")
        if book.info['year']:
            print(f"\t-Publication year: {book.info['year']}")
        if book.info['isbn']:
            print(f"\t-ISBN: {book.info['isbn']}")
        print(f"\t-Date & time entered: {book.info['date']}")
        if book.info['done']:
            print("\t-Completion status: Completed")
            if book.info['review']:
                print("\t-Book review:\n"
                      f"{book.info['review']}")
            if book.info['score']:
                print(f"\t-Score: {book.info['score']}/5")
            else:
                print(f"\t-You have not scored this book yet.")
        else:
            print("\t-Completion status: Not completed")
        print(columns * '-')


def print_b(book_obj):
    """Print a single book and all associated information."""
    print(f"\t-Title: {book_obj.info['title']}\n"
          f"\t-Author: {book_obj.info['author']}")
    if book_obj.info['year']:
        print(f"\t-Publication year: {book_obj.info['year']}")
    if book_obj.info['isbn']:
        print(f"\t-ISBN: {book_obj.info['isbn']}")
    print(f"\t-Date & time entered: {book_obj.info['date']}")
    if book_obj.info['done']:
        print("\t-Completion status: Finished")
        if book_obj.info['review']:
            print("\t-Book review:\n"
                  f"{book_obj.info['review']}")
        if book_obj.info['score']:
            print(f"\t-Score: {book_obj.info['score']}/5")
    else:
        print("\t-Completion status: Not finished")
    print(columns * '-')


def review(book_obj):
    """Enter a review for a book you've finished."""
    if not book_obj.info['done']:
        print("You haven't finished this book yet! Please update the book entry first.")
        print(columns * '-')
    else:
        book_obj.info['review'] = input("Please enter your review here:\n")
        print(columns * '-')
        score = int(input("Please enter a score (from one to five) for this book: "))
        if score > 0 < 6:
            book_obj.info['score'] = score
            print("Review and score saved!")
            print(columns * '-')
        else:
            print("Invalid input detected!\nRemember to score the book on a scale from one to five.")


def edit(book_obj):
    """Edit one of the books in the list."""
    options = ['Title', 'Author', 'Year', 'ISBN', 'Completion status']
    print("The following information can be updated:\n"
          "\n1. Title"
          "\n2. Author"
          "\n3. Year"
          "\n4. ISBN"
          "\n5. Completion status")
    edit = int(input("Please enter the number you would like to edit: "))
    if edit != 5:
        change = input(f"Please enter the updated {options[edit-1]}: ")
        temp_str = str(options[edit-1])
        book_obj.info[temp_str.lower()] = change.strip()
        print(f"{options[edit-1]} successfully updated.")
        print(columns * '-')
    elif edit == 5:
        if book_obj.info['done']:
            book_obj.info['done'] = False
            print("Completion status updated.")
        else:
            book_obj.done()
            print("Congrats on finishing the book!")
        print(columns * '-')
    else:
        print("Invalid input detected! Please try again.")
        edit(book_obj)


def save_l(book_list, filename):
    """Save the list of books to a JSON file."""
    print("Saving your list...")
    with open(filename, 'w') as f:
        for book in book_list:
            json.dump(book.info, f)
            f.write('\n')
        print("List successfully saved!")
        print(columns * '-')


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
                    print_b(book)


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
        print_l(score_list)
    else:
        print("Here is your reading list sorted by score, from lowest to highest:")
        print_l(score_list)


def get_summary(book_obj):
    """Get a short summary of a book from Wikipedia and display it to the user."""
    book_page = wiki.page(book_obj.info['title'])
    if book_page.exists():
        unparsed_sum = book_page.text
        book_sum = unparsed_sum.split("\n")[0]
        if book_sum == f"{book_obj.info['title']} may refer to:":
            print(columns * '*')
            print("It looks like there are multiple Wikipedia articles under that name.\n"
                  "You'll have to check the disambiguation page on wikipedia.org to see a summary. Sorry!")
            print(columns * '*')
        else:
            print(columns * '-')
            print(f"Wikipedia summary for {book_obj.info['title']}:\n"
                  "\t" + book_sum)
            print(columns * '-')
    else:
        print(f"We're sorry, but it looks like {book_obj.info['title']} does not have a Wikipedia entry.")


def delete(book_list, to_del):
    """Delete an entry from the reading list."""
    book_list.remove(book_list[to_del-1])
    print("Entry successfully deleted!")
    print(columns * '-')
