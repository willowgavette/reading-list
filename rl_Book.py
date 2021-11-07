from datetime import date
import wikipediaapi


wiki = wikipediaapi.Wikipedia('en')  # Creating a wikipedia object for wikipedia summaries


class Book:
    """Model for a book."""

    def __init__(self, title, author, **kwargs):
        """Initialize information about a book."""
        self.info = {
            'title': title,
            'author': author,
            'date': str(date.today()),
            'done': False,
        }

        for key, value in kwargs.items():
            self.info[key] = value

    def __str__(self):
        """Return string representation of a book object."""
        return f"{self.info['title']} by {self.info['author']}"

    def done(self):
        """Record that we have done reading the book & open up review and score parameters."""
        self.info['done'] = True
        self.info['review'] = ''
        self.info['score'] = None
        
    def print(self):
        """Print a single book and all associated information."""
        print(f"\t-Title: {self.info['title']}\n"
              f"\t-Author: {self.info['author']}\n"
              f"\t-ISBN: {self.info['isbn']}\n"
              f"\t-Publication year: {self.info['year']}")
        if self.info['done']:
            print("\t-Completion status: Completed")
            if self.info['review']:
                print("\t-Book review:\n"
                      f"{self.info['review']}")
            else:
                print("\t-You have not reviewed this book yet.")
            if self.info['score']:
                print(f"\t-Score: {self.info['score']}/5")
            else:
                print(f"\t-You have not scored this book yet.")
        else:
            print("\t-Completion status: Not completed")

    def edit(self):
        """Edit one of the books in the list."""
        fields = ['Title', 'Author', 'Year', 'ISBN', 'Completion status']
        print("The following information can be updated:\n"
              "\n1. Title"
              "\n2. Author"
              "\n3. Year"
              "\n4. ISBN"
              "\n5. Completion status")
        option = int(input("Please enter the number you would like to edit: "))
        if option != 5:
            change = input(f"Please enter the updated {fields[option-1]}: ")
            temp_str = str(fields[option-1])
            self.info[temp_str.lower()] = change.strip()
            print(f"{fields[option-1]} successfully updated.")
        elif option == 5:
            if self.info['done']:
                self.info['done'] = False
                print("Completion status updated.")
            else:
                self.done()
                print("Congrats on finishing the book!")
        else:
            print("Invalid input detected! Please try again.")
            self.edit()

    def review(self):
        """Enter a review for a book you've finished."""
        self.info['review'] = input("Please enter your review below:\n")
        score = int(input("Please enter a score (from one to five) for this book: "))
        if score > 0 < 6:
            self.info['score'] = score
            print("Review and score saved!")
        else:
            print("Invalid input detected!\nRemember to score the book on a scale from one to five.")
            self.review()
            
    def summarize(self):
        """Get a short summary of a book from Wikipedia and display it to the user."""
        book_page = wiki.page(self.info['title'])
        if book_page.exists():
            unparsed_sum = book_page.text
            book_sum = unparsed_sum.split("\n")[0]
            if book_sum == f"{self.info['title']} may refer to:":
                print("It looks like there are multiple Wikipedia articles under that name.\n"
                      "You'll have to check the disambiguation page on wikipedia.org to see a summary. Sorry!")
            else:
                print(f"Wikipedia summary for {self.info['title']}:\n"
                      "\t" + book_sum)
        else:
            print(f"We're sorry, but it looks like {self.info['title']} does not have a Wikipedia entry.")
