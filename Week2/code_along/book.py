# 4. Define a `Book` class
class Book:
    # 5. Define constructor with title (String), author (String), and genre (String).
    def __init__(self, title, author, genre):
        # 6. Assign params to properties. Additionally, create a property called `is_checked_out` and initilize it with a boolean value of `False`.
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = False
        # Go to main.py to see the next steps.
    
    # 12. Define a check_out method that takes the object as an argument and checks the book out if it is not already checked out.
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out!")
        else:
            print(f"{self.title} is already checked out!")
    
    # 13. Define a check_in method that takes the object as an argument and checks the book in if it is already checked out.
    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been checked in!")
        else:
            print(f"{self.title} is already checked in!")
        # Go to main.py to see the next steps.
    
    # 17a. Create a __str__ method
    def __str__(self): 
        # 17b. Return a string with the title, author, genre, and the value of is_checked_out.
        # return f"{self.title} by {self.author} - {self.genre} ({self.is_checked_out})"

        # 18. Format this so we don't get a boolean value in the string. If is_checked_out is True, return "Checked Out". Otherwise, return "Available". Print the updated string.
        if self.is_checked_out:
            status = "Checked Out"
        else:
            status = "Available"
        return f"{self.title} by {self.author} - {self.genre} ({status})"