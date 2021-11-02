from datetime import datetime


class Book:
    """Model for a book."""
    
    def __init__(self, title, author, year='', isbn='', done=False, date='', review='', score=''):
        """Initialize information about a book."""     
        self.info = {
            'title': title,
            'author': author,
        }
        if year:
            self.info['year'] = year
        else:
            self.info['year'] = ''
        if isbn:
            self.info['isbn'] = isbn
        else:
            self.info['isbn'] = ''
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
            self.info['score'] = 'Not rated'
   
    def done(self):
        """Record that we have done reading the book."""
        self.info['done'] = True
        