class Person:
    def __init__(self,name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def can_vote(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."