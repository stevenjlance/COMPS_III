# Code Demo Instructions

## Overview
For this week we'll be building upon our library book management system. Last week, we built a `Book` class with properties and methods. This week, we'll be adding two additional classes (`Textbook` and `GraphicNovel`) that inherit some properties and methods from the `Book` class.

![Book class](./Library.png)

## Local Terminal - bash.sh has syntax instructions
1. Navigate to the folder that was created last week. There should be two files in the folder: `library.py` and `main.py`. Go to the `library.py` file.

## VS Code - library.py has syntax instructions
2. Define a `Textbook` class that is a child of the `Book` class.
3. Call the `__init__` method in the child class using either `Book` or `super()`. Set the `title`, `author`, and `genre` properties. `genre` can be default set to `"Textbook"` since every instance of the `Textbook` class will be a textbook.
4. Set the `subject` and `edition` properties to the values that are passed into the constructor.
5. Finally, create a property called `solutions_accessed` and initialize it with a boolean value of `False`.
6. Create a method called `access_solutions` that takes the object and password as arguments. If `password` matches some hard coded value (e.g. `"1234"`), then set `solutions_accessed` to True and return the string `"[TITLE] solutions accessed!"`. If `password` is incorrect, return the string `"Incorrect password. Solutions not accessed."`.

## VS Code - main.py has syntax instructions
7. Import the `Textbook` class into the file. The `Book` class was imported last week.
8. Inside the `main()` function that was created last week, create an instance of the `Textbook` class and `print()` out the object. Show how it inherited the `__str__` method from the `Book` class.
9. Call the `access_solutions()` method and print out the result and the new value of `solutions_accessed`. Call the method again with the wrong password to verify it prints the correct value.

## VS Code - library.py has syntax instructions
10. Define a `GraphicNovel` class that is a child of the `Book` class.
11. Call the `__init__` method in the child class using either `Book` or `super()`. Set the `title`, `author`, and `genre` properties. `genre` can be default set to `"Graphic Novel"` since every instance of the `GraphicNovel` class will be a textbook.
12. Set the `illustrator` and `color` to the values that are passed into the constructor. If no value is passed in for `color`, default its value to `True`.
13. Create a method called `get_art_details` that takes the object as an argument. If the novel is in color, return the string `"Illustrated by ILLUSTRATOR in color."`. If the novel is not in color, return the string `"Illustrated by ILLUSTRATOR in black and white."`.

## VS Code - main.py has syntax instructions
14. Import the `GraphicNovel` class into the file.
15. Inside the `main()` function, create an instance of the `GraphicNovel` class and `print()` out the object. Show how it also inherited the `__str__` method from the `Book` class.
16. Call the `get_art_details()` method and print out the resulting string.