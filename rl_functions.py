# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:10:32 2021

@author: Admin
"""
from rl_Book import Book

def enter_book():
    
    """Create a new book object and store user-entered info. Return created object."""
    active = True
    while active:
        print("\nPlease enter some information on the book you'd like to add.")

        # Create temporary variables to pass to the Book() class.
        title = input("Title: ")
        author = input("Author: ")
        year = input("Publication year: ")
        isbn = input("ISBN: ")

        # Check to make sure user entered the information correctly.
        print("The information you entered is as follows:")
        print(f"\tTitle: {title}")
        print(f"\tAuthor: {author}")
        print(f"\tPublication year: {year}")
        print(f"\tISBN: {isbn}")
        cont = input("Is this correct? (y/n): ")
        if cont.lower() != 'n':
            active = False
            new_book = Book(title, author, year, isbn)
            return new_book  

def print_options():
    
    """Print the list of options the user can choose from."""
    print("\nWelcome to your reading list! You can:")
    print("\n1. Enter a new book")
    print("\n2. Update information on a book already in the list")
    print("\n3. Check your complete reading list")
    print("\n4. Save and quit")
    
def print_books(list):
    """Print the saved list of books."""
    book_number = 1
    for book in list:
        print(f"Book #{book_number}:")
        print(f"\tTitle: {book.title}")
        print(f"\tAuthor: {book.author}")
        print(f"\tPublication year: {book.year}")
        print(f"\tISBN: {book.isbn}\n")
        print(f"This book was entered into the app on {book.when_entered}.")
        if book.finished_book == True:
            print("You have finished reading this book! Good job :)")
        else:
            print("You have not finished reading this book yet.")
        book_number += 1