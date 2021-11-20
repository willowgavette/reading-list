import unittest
from funcs import *
from book import Book


test_filename = './DNE.json'


class FunctionsTestCase(unittest.TestCase):
    """A series of tests for the reading list app's functions & the Book class."""
    
    def setUp(self):
        """Create a couple of test books for use in testing."""
        self.book1 = Book('test title', 'test author')
        self.book2 = Book('other test title', 'other test author')
        self.book_list = [
            self.book1,
            self.book2,
        ]
        
    def test_done_update(self):
        """Does updating a book's status work?"""
        self.book1.done()
        self.assertTrue(self.book1.info['done'])
        
    def test_load_l(self):
        """
        Does giving a correct filename result in a loaded list?
        Does giving an incorrect filename result in a FileNotFoundError?
        """
        filename = './reading_list.json'

        test_list = load_l(filename)
        self.assertTrue(test_list)
        new_test_book_list = []
        try:
            new_test_book_list = load_l(test_filename)
        except FileNotFoundError:
            pass
        self.assertFalse(new_test_book_list)
            
    def test_create_l(self):
        """Does creating a new list work?"""
        test_l = create_l()
        self.assertTrue(test_l)
        
    def test_enter_book(self):
        """Does passing a title and author to enter_book work?"""
        print("enter 'test title', 'test author'")
        test_book = enter_book()
        self.assertEqual(self.book1.info['title'], test_book.info['title'])
        self.assertEqual(self.book1.info['author'], test_book.info['author'])

    def test_full_print(self):
        """Does printing out the list of books work?"""
        self.assertIsNone(full_print(self.book_list))
        
    def test_print_b(self):
        """Does printing out a single book work?"""
        self.assertIsNone(self.book1.print())

    def test_review(self):
        """Does entering a review and score for a book work?"""
        review_book = Book('test', 'test', done=True)
        print("enter 'Excellent!' for review, 5 for score")
        review_book.review()
        self.book1.done()
        self.book1.info['review'] = 'Excellent!'
        self.book1.info['score'] = 5
        self.assertEqual(self.book1.info['review'], review_book.info['review'])
        self.assertEqual(self.book1.info['score'], review_book.info['score'])
        
    def test_edit(self):
        """Does editing a book in the list work?"""
        initial_book = Book('test title', 'test author')
        self.book1.edit() # data entered does not matter since we're just testing
                        # whether or not you can update a piece of information
        self.assertNotEqual(self.book1, initial_book)
        
    def test_sort_l(self):
        """Does sorting the list according to a given parameter work?"""
        self.assertIsNone(sort_l(self.book_list, 1))

    def test_get_summary(self):
        """Does getting a summary from Wikipedia work?"""
        real_book = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling")
        self.assertIsNone(real_book.summarize())
        self.assertFalse(self.book1.summarize())
    
    def test_delete(self):
        """Does deleting an entry from the reading list work?"""
        delete(self.book_list, 1)
        self.assertNotIn(self.book1, self.book_list)
        
if __name__ == '__main__':
    unittest.main()