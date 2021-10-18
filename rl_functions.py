from rl_Book import Book
import json

def load_list(filename):
    """Load reading list into memory from JSON file."""
    with open(filename, 'r') as book_list:
        t_list = []
        for json_obj in book_list:
            book = json.loads(json_obj)
            loaded_book = Book(book['title'], book['author'], book['year'], book['isbn'], book['finished'], book['date'], book['review'], book['score'])
            t_list.append(loaded_book)
        return t_list
    
def enter_book():
    """Create a new book object and store user-entered info. Return created object."""
    active = True
    while active:
        print("\nPlease enter some information on the book you'd like to add.")

        # Create temporary variables to pass to the Book() class.
        title = input("Title: ")
        author = input("Author: ")
        year = input("Publication year: ")
        isbn = input("ISBN: ")

        # Check to make sure user entered the information correctly.
        print("The information you entered is as follows:")
        print(f"\tTitle: {title}")
        print(f"\tAuthor: {author}")
        print(f"\tPublication year: {year}")
        print(f"\tISBN: {isbn}")
        cont = input("Is this correct? (y/n): ")
        if cont.lower().strip() == 'y':
            active = False
            new_book = Book(title.strip(), author.strip().title(), year.strip(), isbn.strip())
            return new_book  
        elif cont.strip() == 'n':
            continue
        else:
            print("Invalid input detected! Please try again.")
            
def print_options():  
    """Print the list of options the user can choose from."""
    print("\n1. Check your reading list")
    print("\n2. Enter a new book")
    print("\n3. Post a review of a book")
    print("\n4. Update information on a book already in the list")
    print("\n5. Sort your reading list")
    print("\n6. Save and quit")

def print_list(list_of_books):
    """Print the saved list of books."""  
    book_number = 0
    for book in list_of_books:
        book_number += 1
        print(f"\nBook #{book_number}:")
        print(f"\t-Title: {book.info['title']}")
        print(f"\t-Author: {book.info['author']}")
        print(f"\t-Publication year: {book.info['year']}")
        print(f"\t-ISBN: {book.info['isbn']}")
        print(f"\t-Date & time entered: {book.info['date']}")
        if book.info['finished'] == True:
            print("\t-Status: Completed")
        else:
            print("\t-Status: Not completed")
        if book.info['review']:
            print("\t-Book review:")
            print(f"{book.info['review']}")
        else:
            continue
        if book.info['score'] != 0:
            print(f"\t-Score: {book.info['score']}/5")
        else:
            continue
        
def print_book(book_obj):
    """Print a single book and all associated information."""
    print(f"\t-Title: {book_obj.info['title']}")
    print(f"\t-Author: {book_obj.info['author']}")
    print(f"\t-Publication year: {book_obj.info['year']}")
    print(f"\t-ISBN: {book_obj.info['isbn']}")
    print(f"\t-Date & time entered: {book_obj.info['date']}")
    if book_obj.info['finished'] == True:
        print("\t-Status: Completed")
    else:
        print("\t-Status: Not completed")
    if book_obj.info['review']:
        print("\t-Book review:")
        print(f"{book_obj.info['review']}")
    if book_obj.info['score'] != 0:
        print(f"\t-Score: {book_obj.info['score']}/5")
            
def review_book(book_obj):
    """Enter a review for a book you've finished."""
    if book_obj.info['finished'] == False:
        print("You haven't finished this book yet! Please update the book entry first.")
    else:
        book_obj.info['review'] = input("Please enter your review here:\n")
        book_obj.info['score'] = int(input("Please enter a score (out of five) for this book: "))
        print("Review and score saved!")

def edit_entry(book_obj):
    """Edit one of the books in the list."""
    print("Please name the item you would like to edit (ex: title, author, etc.")
    edit = input("If you have finished the book, please type 'finished' and press enter: ")
    edit = edit.lower().strip()
    while edit:
        if edit == 'title':
            change = input("Please enter the updated title: ")
            book_obj.info['title'] = change.strip()
            print("Title successfully updated.")
            break
        elif edit == 'author':
            change = input("Please enter the updated author: ")
            book_obj.info['author'] = change.strip().title()
            print("Author successfully updated.")
            break
        elif edit == 'year':
            change = input("Please enter the updated year: ")
            book_obj.info['year'] = change.strip()
            print("Year successfully updated.")
            break
        elif edit == 'isbn':
            change = input("Please enter the updated ISBN: ")
            book_obj.info['isbn'] = change.strip()
            print("ISBN successfully updated.")
            break
        elif edit == 'finished':
            book_obj.finished()
            print("Congrats on finishing the book!")
            break
        else:
            print("Invalid input detected! Please try again.")
            edit_entry(book_obj)
    

def save_list(list_of_books):
    """Save the list of books to a JSON file."""
    filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'
    print("Saving your list...")
    with open(filename, 'w') as reading_list:
        for book in list_of_books:
            json.dump(book.info, reading_list)
            reading_list.write('\n')
        print("List successfully saved!")
    print("Thank you for using our reading list app!")

def sort_menu(list_of_books):
    """Sort the list of books according to parameters given by the user."""
    print("You may sort your reading list by:")
    print("\t1. Title")
    print("\t2. Author")
    print("\t3. Year of publication(newest to oldest")
    print("\t4. Score(highest to lowest")
    option = input("Please enter the number of the option you'd like: ")
    active = True
    while active:
        if option.strip() == '1':
            title_list = []
            for book in list_of_books:
                temp_title = book.info['title']
                title_list.append(temp_title)
            title_list.sort()
            print("Here is your reading list sorted by title:")
            for item in title_list:
                print(f"\t-{item}")
                active = False 
        if option.strip() == '2':
            author_list = []
            for book in list_of_books:
                temp_author = book.info['author']
                author_list.append(temp_author)
            author_list.sort()
            print("Here is your reading list sorted by author:")
            for item in author_list:
                print(f"\t-{item}")
                active = False 
        if option.strip() == '3':
            year_list = []
            for book in list_of_books:
                temp_year = int(book.info['year'])
                year_list.append(temp_year)
            year_list.sort(reverse=True)
            print("Here is your reading list sorted by year, from oldest to newest:")
            for item in year_list:
                print(f"\t-{item}")
                active = False
        if option.strip() == '4':
            score_list = []
            for book in list_of_books:
                temp_score = book.info['score']
                if temp_score:
                    score_list.append(temp_score)
            score_list.sort(reverse=True)
            print("Here is your reading list sorted by score, from highest to lowest:")
            for item in score_list:
                print(f"\t-{item}")
                active = False 
                
def sort_list(option):
    """Sort and pass back the reading list."""
    