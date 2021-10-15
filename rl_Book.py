import json
from json import JSONEncoder
from datetime import date

class Book:
    """Model for a book."""
    
    def __init__(self, title, author, year, isbn):
        """
        Initialize book name, author name, the year the book was published, and the ISBN.
        """        
        self.book_info['title'] = title
        self.book_info['author'] = author
        self.book_info['year'] = year
        self.book_info['isbn'] = isbn
        self.book_info['date'] = str(date.today())
        self.book_info['finished'] = False
        
    def finished(self):
        """Record that we have finished reading the book."""
        self.finished = True
        