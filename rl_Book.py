from datetime import datetime

class Book:
    """Model for a book."""
    
    def __init__(self, title, author, year, isbn, done='', date='', review='', score=''):
        """Initialize information about a book."""     
        self.info = {}   
        self.info['title'] = title
        self.info['author'] = author
        self.info['year'] = year
        self.info['isbn'] = isbn
        if done:
            self.info['status'] = done
        else:
            self.info['status'] = False
        if date:
            self.info['date'] = date
        else:
            self.info['date'] = str(datetime.now())
        if review:
            self.info['review'] = review
        else:
            self.info['review'] = ''
        if score:
            self.info['score'] = score
        else:
            self.info['score'] = 0
   
    def done(self):
        """Record that we have done reading the book."""
        self.info['status'] = True
        