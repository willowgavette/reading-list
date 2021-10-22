import unittest
from rl_functions import *
from rl_Book import *

class FunctionsTestCase(unittest.TestCase):
    """A series of tests for the reading list app's functions & the Book class."""
    
    def setUp(self):
        """Create a couple of test books for use in testing."""
        self.setup_book = Book('test title', 'test author')
        self.other_setup_book = Book('test title', 'test author')
        
    def test_done_update(self):
        """Does updating a book's done work?"""
        self.setup_book.done()
        self.assertTrue(self.setup_book.info['done'])

    def test_review(self):
        """Does entering a review and score for a book work?"""
        review_book = Book('test', 'test', done=True)
        review(review_book) 
        self.setup_book.done()
        self.assertEqual(self.setup_book.info['review'], review_book.info['review'])
        self.assertEqual(self.setup_book.info['score'], review_book.info['score'])
        
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
        print("***Does not matter what info you enter***")
        test_l = create_l(test_filename) # Data entered does not matter, we're simply testing whether or not a list is able to be created
        self.assertTrue(test_l)
        
    def test_delete(self):
        """Does deleting an entry from the reading list work?"""
        book_list = []
        book_list.append(self.setup_book)
        book_list.append(self.other_setup_book)
        delete(book_list) # make sure to delete the first entry
        self.assertNotIn(self.setup_book, book_list)

if __name__ == '__main__':
    unittest.main()