from rl_Book import Book
import json
import shutil

# The list of functions we need to actually manipulate data inside our reading list.

def load_list(filename):
    """Load reading list into memory from JSON file."""
    with open(filename, 'r') as book_list:
        t_list = []
        for json_obj in book_list:
            book = json.loads(json_obj)
            loaded_book = Book(book['title'], book['author'], book['year'], book['isbn'], book['status'], book['date'], book['review'], book['score'])
            t_list.append(loaded_book)
        return t_list
    
def enter_book():
    """Create a new book object and store user-entered info. Return created object."""
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
        new_book = Book(title.strip(), author.strip().title(), year.strip(), isbn.strip())
        return new_book  
    elif cont.lower().strip() == 'n':
        enter_book()     
    else:
        print("Invalid input detected! Please try again.")
        enter_book()
            
def options():  
    """Print the list of options the user can choose from."""
    print("\n1. Check your reading list")
    print("\n2. Enter a new book")
    print("\n3. Update a book entry")
    print("\n4. Review and score a book")
    print("\n5. Sort your reading list")
    print("\n6. Delete an entry from the list")
    print("\n7. Save and quit")
    option = input("Please enter the number of the option you'd like: ")
    return option.strip()

def print_l(book_list):
    """Print the entire saved list of books."""  
    book_number = 0
    for book in book_list:
        book_number += 1
        print(f"\nBook #{book_number}:")
        print(f"\t-Title: {book.info['title']}")
        print(f"\t-Author: {book.info['author']}")
        print(f"\t-Publication year: {book.info['year']}")
        print(f"\t-ISBN: {book.info['isbn']}")
        print(f"\t-Date & time entered: {book.info['date']}")
        if book.info['status'] == True:
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
        
def print_b(book_obj):
    """Print a single book and all associated information."""
    print(f"\t-Title: {book_obj.info['title']}")
    print(f"\t-Author: {book_obj.info['author']}")
    print(f"\t-Publication year: {book_obj.info['year']}")
    print(f"\t-ISBN: {book_obj.info['isbn']}")
    print(f"\t-Date & time entered: {book_obj.info['date']}")
    if book_obj.info['status'] == True:
        print("\t-Status: Finished")
        if book_obj.info['review']:
            print("\t-Book review:")
            print(f"{book_obj.info['review']}")
        if book_obj.info['score']:
            print(f"\t-Score: {book_obj.info['score']}/5")
    else:
        print("\t-Status: Not Finished")
            
def review(book_obj):
    """Enter a review for a book you've finished."""
    if book_obj.info['status'] == False:
        print("You haven't finished this book yet! Please update the book entry first.")
    else:
        book_obj.info['review'] = input("Please enter your review here:\n")
        score = int(input("Please enter a score (from one to five) for this book: "))
        if score > 0 < 6:
            book_obj.info['score'] = score
            print("Review and score saved!")
        else:
            print("Invalid input detected!\nRemember to score the book on a scale from one to five.")

def edit(book_obj):
    """Edit one of the books in the list."""
    print("The following information can be updated:")
    print("\n1. Title\n2. Author\n3. Publication year\n4. ISBN\n5. Status")

    edit = input("Please enter the number you would like to edit: ")
    while edit:
        if edit == '1':
            change = input("Please enter the updated title: ")
            book_obj.info['title'] = change.strip()
            print("Title successfully updated.")
            break
        elif edit == '2':
            change = input("Please enter the updated author: ")
            book_obj.info['author'] = change.strip().title()
            print("Author successfully updated.")
            break
        elif edit == '3':
            change = input("Please enter the updated year: ")
            book_obj.info['year'] = change.strip()
            print("Year successfully updated.")
            break
        elif edit == '4':
            change = input("Please enter the updated ISBN: ")
            book_obj.info['isbn'] = change.strip()
            print("ISBN successfully updated.")
            break
        elif edit == '5':
            book_obj.done()
            print("Congrats on finishing the book!")
            break
        else:
            print("Invalid input detected! Please try again.")
            edit(book_obj)   

def save_l(book_list, filename='C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'):
    """Save the list of books to a JSON file."""
    print("Saving your list...")
    with open(filename, 'w') as file_obj:
        for book in book_list:
            json.dump(book.info, file_obj)
            file_obj.write('\n')
        print("List successfully saved!")
    print("Thank you for using our reading list app!")

def sort_l(book_list):
    """Sort the list of books according to parameters given by the user."""
    print("You may sort your reading list by:")
    print("\t1. Title")
    print("\t2. Author")
    print("\t3. Year of publication(newest to oldest)")
    print("\t4. Year of publication(oldest to newest)")
    print("\t5. Score(highest to lowest)")
    print("\t6. Score(lowest to highest)")
    option = input("Please enter the number of the option you'd like: ")
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
                    print('-------------------------------------------')
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
                    print('-------------------------------------------')
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
                    print('-------------------------------------------')
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
                    print('-------------------------------------------')
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
                    print('-------------------------------------------')
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
                    print('-------------------------------------------')
                
def delete(book_list):
    """Delete an entry from the reading list."""
    print_l(book_list)
    to_del = input("Please enter the number of the entry you would like to delete: ")
    to_del = int(to_del)
    book_list.remove(book_list[to_del - 1])
    print("Entry successfully deleted!")
    