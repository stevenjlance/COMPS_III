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

class Textbook(Book):
    def __init__(self, title, author, subject, edition):
        Book.__init__(self, title, author, "Textbook")
        self.subject = subject
        self.edition = edition
        self.solutions_accessed = False

    def access_solutions(self, password):
        if password == "1234":
            self.solutions_accessed = True
            return f"{self.title} solutions accessed!"
        else:
            return "Incorrect password. Solutions not accessed."
    
    def __str__(self):
        # Build on parent's __str__ method so we can practice DRY principles and not recreate the conditional statement.
        basic_info = super().__str__()
        return f"{basic_info}\nSubject: {self.subject}, Edition: {self.edition}"

class GraphicNovel(Book):
    def __init__(self, title, author, illustrator, color=True):
        Book.__init__(self, title, author, "Graphic Novel")
        self.illustrator = illustrator
        self.is_color = color
    
    def get_art_details(self):
        if self.is_color:
            return f'Illustrated by {self.illustrator} in color.'
        else:
            return f'Illustrated by {self.illustrator} in black and white.'

    def __str__(self):
        basic_info = super().__str__()
        return f"{basic_info}\nIllustrated by: {self.illustrator}"

math_book = Textbook("Algebra Foundations", "Dr. Smith", "Mathematics", "3rd")
print(math_book)
print(math_book.access_solutions("1234"))
# manga = GraphicNovel("One Piece Vol. 1", "Eiichiro Oda", "Eiichiro Oda")
# print(manga)
# print(manga.get_art_details())