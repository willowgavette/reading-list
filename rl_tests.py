import unittest
from rl_functions import *
from rl_Book import *

class FunctionsTestCase(unittest.TestCase):
    """A series of tests for the reading list app's functions & the Book class."""
    
    def setUp(self):
        """Create a test book for use in testing."""
        self.test_book = Book('The Test Title', 'Test Testerson III', '2021', '91839575345', False, '2021-10-21 21:40.00', 'Fantastic test, would test again!', 3)
        self.test_mini_book = Book('test title', 'test author', 'test year', 'test isbn')

    def test_Book_class(self):
        """Does a book with a bunch of spaces and weird characters work?"""
        test_book = Book('   !@#  $%^&*  ()~`|}{   ', '   !@#  $%^&*  ()~`|}{   ', '   !@#  $%^&*  ()~`|}{   ', '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['title'], '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['author'], '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['year'], '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['isbn'], '   !@#  $%^&*  ()~`|}{   ')
        
    def test_done_update(self):
        """Does updating a book's done work?"""
        self.assertEqual(self.test_book.info['done'], False)
        self.test_book.done()
        self.assertEqual(self.test_book.info['done'], True)

    def test_review(self):
        """Does entering a review and score for a book work?"""
        review_book = Book('test', 'test', 'test', 'test', done=True)
        review(review_book) # We enter the same review (Fantastic test, would test again!) and score (3)
        self.test_book.info['done'] = True
        self.assertEqual(self.test_book.info['review'], review_book.info['review'])
        self.assertEqual(self.test_book.info['score'], review_book.info['score'])
        
    def test_load_l(self):
        """
        Does giving a correct filename result in a loaded list?
        Does giving an incorrect filename result in a FileNotFoundError?
        """
        filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\reading_list.json'
        test_book_list = load_l(filename)
        self.assertTrue(test_book_list)
        test_filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\DNE.json'
        new_test_book_list = []
        try:
            new_test_book_list = load_l(test_filename)
        except FileNotFoundError:
            self.assertFalse(new_test_book_list)
            
    def test_create_l(self):
        """Does creating a new list work?"""
        test_filename = 'C:\\Users\\Admin\\Documents\\GitHub\\reading-list\\DNE.json'
        print("Current test: test_create_l")
        test_l = create_l(test_filename) # Data entered does not matter, we're simply testing whether or not a list is able to be created
        self.assertTrue(test_l)
        
    def test_enter_book(self):
        """Does entering a new book work? Is the new information stored correctly?"""
        print("Current test: test_enter_book()")
        test_book_2 = enter_book() # data entered should match test_book ("The Test Title, Test Testerson III, etc.)
        self.assertEqual(self.test_mini_book, test_book_2)
        
if __name__ == '__main__':
    unittest.main()