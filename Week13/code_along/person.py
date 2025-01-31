class Person:
    '''
    A class to represent a person.

    Attributes:
    ----------
    name : str
        Name of the person
    age : int
        Age of the person

    Methods:
    -------
    greet():
        Prints a greeting message.
    '''
    def __init__(self, name, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters:
        ----------
        name : str
            Name of the person
        age : int
            Age of the person
        """
        self.name = name
        self.age = age

    def greet(self):
        """
        Prints a greeting message with the person's name and age.
        """
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")