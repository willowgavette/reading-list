from datetime import datetime

class Book:
    """Model for a book."""
    
    def __init__(self, title, author, year='', isbn='', done=False, date='', review='', score=''):
        """Initialize information about a book."""     
        self.info = {}   
        self.info['title'] = title
        self.info['author'] = author
        if year:
            self.info['year'] = year
        else:
            self.info['year'] = None
        if isbn:
            self.info['isbn'] = isbn
        else:
            self.info['isbn'] = None
        if done:
            self.info['done'] = done
        else:
            self.info['done'] = False
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
            self.info['score'] = None
   
    def done(self):
        """Record that we have done reading the book."""
        self.info['done'] = True
        