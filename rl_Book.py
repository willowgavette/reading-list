from datetime import date


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
