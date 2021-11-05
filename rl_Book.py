from datetime import datetime


class Book:
    """Model for a book."""

    def __init__(self, title, author, **kwargs):
        """Initialize information about a book."""
        self.info = {
            'title': title,
            'author': author,
            'date': str(datetime.now()),
            'done': False,
        }

        for key, value in kwargs.items():
            self.info[key] = value

    def done(self):
        """Record that we have done reading the book & open up review and score parameters."""
        self.info['done'] = True
        self.info['review'] = ''
        self.info['score'] = None
