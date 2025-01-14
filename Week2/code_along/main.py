# 7. Import the `Book` class into the file.
from book import Book

# 8. Create `main()` function with a `print()` statement. Call the function.
def main():
    # 9. Create 2 instances of the `Book` class and `print()` out a few of the properties for this class.
    book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    book2 = Book("Catcher in the Rye", "J.D. Salinger", "Fiction")
    print(book1.title)
    print(book1.author)
    print(book2.title)
    print(book2.genre)
    print(book2.is_checked_out)

    # 14. Check out and check in the books.
    book1.check_out()
    book2.check_in() # This should not be able to check out a book that is already checked in.
    # 15. Check the book you checked out back in.
    book1.check_in()

    # 15. Print out the books to see the memory address and show why we need the __str__ method.
    print(book1)
    print(book2)
    # Go back to book.py to see the next steps.

# 10. Call the main() function. See bash.sh for directions on how to run in your terminal.
main()