class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."

class Student(Person):
    def __init__(self, name, age, country, major, gpa):
        Person.__init__(self, name, age, country)
        self.major = major
        self.gpa = gpa
    
    def study(self):
        return f"{self.name} is studying {self.major} with a current GPA of {self.gpa}."

class Staff(Person):
    def __init__(self, name, age, country, position, department):
        Person.__init__(self, name, age, country)
        self.position = position
        self.department = department
    
    def work(self):
        return f'{self.name} works as a {self.position} in the {self.department} department.'