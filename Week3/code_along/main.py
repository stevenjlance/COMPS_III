# 7. Import the `Textbook` class into the file. The `Book` class was imported last week.
# 14. Import the `GraphicNovel` class into the file.
from library import Book, Textbook, GraphicNovel

def main():
    # 8. Inside the `main()` function that was created last week, create an instance of the `Textbook` class and `print()` out the object. Show how it inherited the `__str__` method from the `Book` class.
    math_book = Textbook("Algebra Foundations", "Dr. Smith", "Mathematics", 3)
    print(math_book)
    # 9. Call the `access_solutions()` method and print out the result and the new value of `solutions_accessed`. Call the method again with the wrong password to verify it prints the correct value.
    print(math_book.access_solutions("1234"))
    print(math_book.solutions_accessed)
    print(math_book.access_solutions("123"))

    # 15. Inside the `main()` function, create an instance of the `GraphicNovel` class and `print()` out the object. Show how it also inherited the `__str__` method from the `Book` class.
    manga = GraphicNovel("One Piece Vol. 1", "Eiichiro Oda", "Eiichiro Oda")
    print(manga)
    # 16. Call the `get_art_details()` method and print out the resulting string.
    print(manga.get_art_details())

main()