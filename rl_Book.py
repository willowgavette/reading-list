from datetime import date

class Book:
    """Model for a book."""
    
    def __init__(self, title, author, year, isbn, day=''):
        """Initialize information about a book."""     
        self.book_info = {}   
        self.book_info['title'] = title
        self.book_info['author'] = author
        self.book_info['year'] = year
        self.book_info['isbn'] = isbn
        self.book_info['finished'] = False
        if day:
            self.book_info['day'] = day
        else:
            self.book_info['day'] = str(date.today())
        self.book_info['review'] = ''
        self.book_info['score'] = 0
        
    def finished(self):
        """Record that we have finished reading the book."""
        self.book_info['finished'] = True
        