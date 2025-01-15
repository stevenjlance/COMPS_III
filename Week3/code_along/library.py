# This is the Book class that we built in the previous code along.
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out!")
        else:
            print(f"{self.title} is already checked out!")
    
    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been checked in!")
        else:
            print(f"{self.title} is already checked in!")
    
    def __str__(self): 
        if self.is_checked_out:
            status = "Checked Out"
        else:
            status = "Available"
        return f"{self.title} by {self.author} - {self.genre} ({status})"

# 2 Define a `Textbook` class that is a child of the `Book` class.
class Textbook(Book):
    # 3. Call the `__init__` method in the child class using either `Book` or `super()`. Set the `title`, `author`, and `genre` properties. `genre` can be default set to `"Textbook"` since every instance of the `Textbook` class will be a textbook.
    def __init__(self, title, author, subject, edition):
        Book.__init__(self, title, author, "Textbook")
        # 4. Set the `subject` and `edition` properties to the values that are passed into the constructor.
        self.subject = subject
        # 5. Finally, create a property called `solutions_accessed` and initialize it with a boolean value of `False`.
        self.edition = edition
        self.solutions_accessed = False

    # 6. Create a method called `access_solutions` that takes the object and password as arguments.
    def access_solutions(self, password):
        # If `password` matches some hard coded value (e.g. `"1234"`), then set `solutions_accessed` to True and return the string `"[TITLE] solutions accessed!"`. If `password` is incorrect, return the string `"Incorrect password. Solutions not accessed."`
        if password == "1234":
            self.solutions_accessed = True
            return f"{self.title} solutions accessed!"
        else:
            return "Incorrect password. Solutions not accessed."
    
# 10. Define a `GraphicNovel` class that is a child of the `Book` class.
class GraphicNovel(Book):
    # 11. Call the `__init__` method in the child class using either `Book` or `super()`. 
    def __init__(self, title, author, illustrator, color=True):
        # Set the `title`, `author`, and `genre` properties. `genre` can be default set to `"Graphic Novel"` since every instance of the `GraphicNovel` class will be a textbook.
        Book.__init__(self, title, author, "Graphic Novel")
        # 12. Set the `illustrator` and `color` to the values that are passed into the constructor. If no value is passed in for `color`, default its value to `True`.
        self.illustrator = illustrator
        self.is_color = color
    # 13. Create a method called `get_art_details` that takes the object as an argument. 
    def get_art_details(self):
        # If the novel is in color, return the string `"Illustrated by ILLUSTRATOR in color."`. If the novel is not in color, return the string `"Illustrated by ILLUSTRATOR in black and white."`.
        if self.is_color:
            return f'Illustrated by {self.illustrator} in color.'
        else:
            return f'Illustrated by {self.illustrator} in black and white.'