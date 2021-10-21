import unittest
from rl_functions import *
from rl_Book import *

class FunctionsTestCase(unittest.TestCase):
    """A series of tests for the reading list app's functions & the Book class."""
    def test_Book_class(self):
        """Does a book with a bunch of spaces and weird characters work?"""
        test_book = Book('   !@#  $%^&*  ()~`|}{   ', '   !@#  $%^&*  ()~`|}{   ', '   !@#  $%^&*  ()~`|}{   ', '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['title'], '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['author'], '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['year'], '   !@#  $%^&*  ()~`|}{   ')
        self.assertEqual(test_book.info['isbn'], '   !@#  $%^&*  ()~`|}{   ')
        
    def test_done_update(self):
        """
        Does updating a book's status work?
        Does initializing an already done book work?
        """
        test_book = Book('test', 'test', 'test', 'test', done=False)
        self.assertEqual(test_book.info['status'], False)
        test_book.done()
        self.assertEqual(test_book.info['status'], True)
        test_book_2 = Book('test_2', 'test_2', 'test_2', 'test_2', done=True)
        self.assertEqual(test_book_2.info['status'], True)

    def test_review(self):
        """Does entering a review and score for a book work?"""
        test_book = Book('test', 'test', 'test', 'test', )

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
        test_l = create_l(test_filename)
        self.assertTrue(test_l)
        
    def test_enter_book(self):
        """Does entering a new book work? Is the new information stored correctly?"""
        test_book = Book('test', 'Test', 'test', 'test') # author is a title
        # For the enter_book() function, we will be entering '   test   ' for every field.
        # Then we will see if the information was stored as 'test'.
        test_book_2 = enter_book()
        self.assertEqual(test_book, test_book_2)
        
if __name__ == '__main__':
    unittest.main()