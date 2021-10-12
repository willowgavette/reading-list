from datetime import date

class Book:
    """Model for a book."""
    
    def __init__(self, title, author, year, isbn, finished_book=False):
        """
        Initialize book name, author name, the year the book was published, and the ISBN.
        """
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.when_entered = date.today()

    def __repr__(self):
        return "Book()"
    
    def __str__(self):
        return "member of Book"
        
    def finished(self):
        """Record that we have finished reading the book."""
        self.finished_book = True

    def when_entered(self):
        """Tell user when this book was entered into the reading list."""
        print(f"This book was entered into the list on {self.when_entered}.")
