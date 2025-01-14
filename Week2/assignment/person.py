class Person:
    # Implement the Person class here
    def __init__(self,name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    # Method to check if a person can vote
    def can_vote(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    # Method to return a string representation of the object
    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."