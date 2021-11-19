from funcs import *

# Check storage to see if a list already exists.
# If one does, load it. If one does not, create one.
filename = './reading_list.json'
try:
    book_list = load_l(filename)
except FileNotFoundError:
    book_list = create_l()
    
print("\nWelcome to your reading list! You can:")
main(book_list, filename)
