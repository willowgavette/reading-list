from rl_Book import Book
import json
import shutil
import wikipediaapi

columns, lines = shutil.get_terminal_size() # Getting size of terminal for pretty printing
columns = int(columns)
lines = int(lines)
wiki = wikipediaapi.Wikipedia('en') # Creating a wikipedia object for wikipedia summaries

# The list of functions we need to actually manipulate data inside our reading list.

def load_l(filename):
    """Load reading list into memory from JSON file."""
    with open(filename, 'r') as book_list:
        t_list = []
        for json_obj in book_list:
            book = json.loads(json_obj)
            loaded_book = Book(book['title'], book['author'], book['year'], book['isbn'], book['done'], book['date'], book['review'], book['score'])
            t_list.append(loaded_book)
        return t_list
    
def create_l(filename):
    """Create a new list and enter the first book into that list."""
    print("Welcome to the reading list app! Let's get your very first book entered.")
    t_list = []
    new_book = enter_book()
    t_list.append(new_book)
    return  t_list
    
def enter_book(title='', author=''):
    """Create a new book object and store user-entered info. Return created object."""
    if title and author:
        new_book = Book(title, author)
        return new_book
    else:
        print("\nPlease enter some information on the book you'd like to add.")
        # Create temporary variables to pass to the Book() class.
        title = input("Title: ")
        if title == '':
            print("You must input a title!")
            enter_book()
        author = input("Author: ")
        if author == '':
            print("You must input an author!")
            enter_book()
        year = input("Publication year: ")
        isbn = input("ISBN: ")
    
        # Check to make sure user entered the information correctly.
        print("The information you entered is as follows:")
        print(f"\tTitle: {title}")
        print(f"\tAuthor: {author}")
        if title:
            print(f"\tPublication year: {year}")
        if isbn:
            print(f"\tISBN: {isbn}")
        cont = input("Is this correct? (y/n): ")
        if cont.lower().strip() == 'y':
            new_book = Book(title.strip(), author.strip().title(), year.strip(), isbn.strip())
            return new_book 
            print(columns * '-')
        elif cont.lower().strip() == 'n':
            enter_book()     
        else:
            print("Invalid input detected! Please try again.")
            enter_book()
            
def options():  
    """Print the list of options the user can choose from."""
    print("1. Check your reading list")
    print("2. Enter a new book")
    print("3. Update a book entry")
    print("4. Review and score a book")
    print("5. Sort your reading list")
    print("6. Delete an entry from the list")
    print("7. Get Wikipedia.org summary for a book")
    print("8. Save and quit")
    option = input("Please enter the number of the option you'd like: ")
    print(columns * '-')
    return option.strip()

def print_l(book_list):
    """Print the entire saved list of books."""  
    book_number = 0
    for book in book_list:
        book_number += 1
        print(f"\nBook #{book_number}:")
        print(f"\t-Title: {book.info['title']}")
        print(f"\t-Author: {book.info['author']}")
        if book.info['year']:
            print(f"\t-Publication year: {book.info['year']}")
        if book.info['isbn']:
            print(f"\t-ISBN: {book.info['isbn']}")
        print(f"\t-Date & time entered: {book.info['date']}")
        if book.info['done'] == True:
            print("\t-Completion status: Completed")
            if book.info['review']:
                print("\t-Book review:")
                print(f"{book.info['review']}")
            if book.info['score'] != 0:
                print(f"\t-Score: {book.info['score']}/5")
            print(columns * '-')
        else:
            print("\t-Completion status: Not completed")
    return True
        
def print_b(book_obj):
    """Print a single book and all associated information."""
    print(f"\t-Title: {book_obj.info['title']}")
    print(f"\t-Author: {book_obj.info['author']}")
    if book_obj.info['year']:
        print(f"\t-Publication year: {book_obj.info['year']}")
    if book_obj.info['isbn']:
        print(f"\t-ISBN: {book_obj.info['isbn']}")
    print(f"\t-Date & time entered: {book_obj.info['date']}")
    if book_obj.info['done'] == True:
        print("\t-Completion status: Finished")
        if book_obj.info['review']:
            print("\t-Book review:")
            print(f"{book_obj.info['review']}")
        if book_obj.info['score']:
            print(f"\t-Score: {book_obj.info['score']}/5")
    else:
        print("\t-Completion status: Not finished")
    print(columns * '-')
    return True
            
def review(book_obj):
    """Enter a review for a book you've finished."""
    if book_obj.info['done'] == False:
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
    print("The following information can be updated:")
    print("\n1. Title\n2. Author\n3. Publication year\n4. ISBN\n5. Completion status")
    edit = input("Please enter the number you would like to edit: ")
    while edit:
        if edit == '1':
            change = input("Please enter the updated title: ")
            book_obj.info['title'] = change.strip()
            print("Title successfully updated.")
            print(columns * '-')
            break
        elif edit == '2':
            change = input("Please enter the updated author: ")
            book_obj.info['author'] = change.strip().title()
            print("Author successfully updated.")
            print(columns * '-')
            break
        elif edit == '3':
            change = input("Please enter the updated year: ")
            book_obj.info['year'] = change.strip()
            print("Year successfully updated.")
            print(columns * '-')
            break
        elif edit == '4':
            change = input("Please enter the updated ISBN: ")
            book_obj.info['isbn'] = change.strip()
            print("ISBN successfully updated.")
            print(columns * '-')
            break
        elif edit == '5':
            book_obj.done()
            print("Congrats on finishing the book!")
            print(columns * '-')
            break
        else:
            print("Invalid input detected! Please try again.")
            edit(book_obj)   

def save_l(book_list, filename='C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'):
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
    if option.strip() == '1':
        title_list = []
        for book in book_list:
            temp_title = book.info['title']
            title_list.append(temp_title)
        title_list.sort()
        print("Here is your reading list sorted by title:")
        for item in title_list:
            for book in book_list:
                if book.info['title'] == item:
                    print_b(book)
    if option.strip() == '2':
        author_list = []
        for book in book_list:
            temp_author = book.info['author']
            author_list.append(temp_author)
        author_list.sort()
        print("Here is your reading list sorted by author:")
        for item in author_list:
            for book in book_list:
                if book.info['author'] == item:
                    print_b(book)
    if option.strip() == '3':
        year_list = []
        for book in book_list:
            temp_year = book.info['year']
            year_list.append(temp_year)
        year_list.sort(reverse=True)
        print("Here is your reading list sorted by year, from newest to oldest:")
        for item in year_list:
            for book in book_list:
                if book.info['year'] == item:
                    print_b(book)
    if option.strip() == '4':
        year_list = []
        for book in book_list:
            temp_year = book.info['year']
            year_list.append(temp_year)
        year_list.sort()
        print("Here is your reading list sorted by year, from oldest to newest:")
        for item in year_list:
            for book in book_list:
                if book.info['year'] == item:
                    print_b(book)
    if option.strip() == '5':
        score_list = []
        for book in book_list:
            temp_score = book.info['score']
            if temp_score:
                score_list.append(temp_score)
        score_list.sort(reverse=True)
        print("Here is your reading list sorted by score, from highest to lowest:")
        for item in score_list:
            for book in book_list:
                if book.info['score'] == item:
                    print_b(book)
    if option.strip() == '6':
        score_list = []
        for book in book_list:
            temp_score = book.info['score']
            if temp_score:
                score_list.append(temp_score)
        score_list.sort()
        print("Here is your reading list sorted by score, from lowest to highest:")
        for item in score_list:
            for book in book_list:
                if book.info['score'] == item:
                    print_b(book)
    return True

def get_summary(book_obj):
    """Get a short summary of a book from Wikipedia and display it to the user."""
    book_page = wiki.page(book_obj.info['title'])
    if book_page.exists():
        unparsed_sum = book_page.text
        book_sum = unparsed_sum.split("\n")[0]
        print(columns * '-')
        print(f"Wikipedia summary for {book_obj.info['title']}:")
        print("\t" + book_sum)
        print(columns * '-')
        return True
    else:
        print(f"We're sorry, but it looks like {book_obj.info['title']} does not have a Wikipedia entry.")
        return False
                
def delete(book_list, to_del):
    """Delete an entry from the reading list."""
    book_list.remove(book_list[to_del-1])
    print("Entry successfully deleted!")
    print(columns * '-')
