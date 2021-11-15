import unittest
from funcs import *
from book import Book

class FunctionsTestCase(unittest.TestCase):
    """A series of tests for the reading list app's functions & the Book class."""
    
    def setUp(self):
        """Create a couple of test books for use in testing."""
        self.setup_book = Book('test title', 'test author', score=1)
        self.other_setup_book = Book('other test title', 'other test author')
        
    def test_done_update(self):
        """Does updating a book's status work?"""
        self.setup_book.done()
        self.assertTrue(self.setup_book.info['done'])
        
    def test_load_l(self):
        """
        Does giving a correct filename result in a loaded list?
        Does giving an incorrect filename result in a FileNotFoundError?
        """
        filename = './reading_list.json'
        test_book_list = load_l(filename)
        self.assertTrue(test_book_list)
        test_filename = './DNE.json'
        new_test_book_list = []
        try:
            new_test_book_list = load_l(test_filename)
        except FileNotFoundError:
            self.assertFalse(new_test_book_list)
            
    def test_create_l(self):
        """Does creating a new list work?"""
        test_filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\DNE.json'
        test_l = create_l(test_filename) # data entered does not matter, we're simply testing whether or not a list is able to be created
        self.assertTrue(test_l)
        
    def test_enter_book(self):
        """Does passing a title and author to enter_book work?"""
        test_book = enter_book('test title', 'test author')
        self.assertEqual(self.setup_book.info['title'], test_book.info['title'])
        self.assertEqual(self.setup_book.info['author'], test_book.info['author'])

    def test_print_l(self):
        """Does printing out the list of books work?"""
        book_list = []
        book_list.append(self.setup_book)
        book_list.append(self.other_setup_book)
        self.assertTrue(print_l(book_list))
        
    def test_print_b(self):
        """Does printing out a single book work?"""
        self.assertTrue(print_b(self.setup_book))

    def test_review(self):
        """Does entering a review and score for a book work?"""
        review_book = Book('test', 'test', done=True)
        review(review_book) # enter 'Excellent!' for review, 1 for score
        self.setup_book.done()
        self.setup_book.info['review'] = 'Excellent!'
        self.assertEqual(self.setup_book.info['review'], review_book.info['review'])
        self.assertEqual(self.setup_book.info['score'], review_book.info['score'])
        
    def test_edit(self):
        """Does editing a book in the list work?"""
        initial_book = Book('test title', 'test author')
        edit(self.setup_book) # data entered does not matter since we're just testing whether or not you can update a piece of information
        self.assertNotEqual(self.setup_book, initial_book)
        
    def test_sort_l(self):
        """Does sorting the list according to a given parameter work?"""
        book_list = []
        book_list.append(self.setup_book)
        book_list.append(self.other_setup_book)
        self.assertTrue(sort_l(book_list, '1'))

    def test_get_summary(self):
        """Does getting a summary from Wikipedia work?"""
        real_book = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling")
        self.assertTrue(get_summary(real_book))
        self.assertFalse(get_summary(self.setup_book))
    
    def test_delete(self):
        """Does deleting an entry from the reading list work?"""
        book_list = []
        book_list.append(self.setup_book)
        book_list.append(self.other_setup_book)
        delete(book_list, 1)
        self.assertNotIn(self.setup_book, book_list)
        
if __name__ == '__main__':
    unittest.main()