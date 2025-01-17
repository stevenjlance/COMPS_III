class Student:
    def __init__(self, name, major, gpa_for_semesters):
        self.name = name
        self.major = major
        self.__gpa_for_semesters = gpa_for_semesters
    
    def __str__(self):
        return f"{self.name} is studying {self.major}."
    
    def get_gpa(self):
        return self.__gpa_for_semesters
    
    def set_gpa(self, gpa_for_semesters):
        self.__gpa_for_semesters = gpa_for_semesters

    def calculate_average_gpa(self):
        return sum(self.get_gpa()) / len(self.get_gpa())
    
    def is_in_good_standing(self):
        return f"{self.name} is a student."

class UndergraduateStudent(Student):
    def __init__(self, name, major, gpa_for_semesters):
        Student.__init__(self, name, major, gpa_for_semesters)
    
    def __str__(self):
        return f"{self.name} is an undergraduate student studying {self.major}."
    
    def is_in_good_standing(self):
        if(self.calculate_average_gpa() >= 2.5):
            return f"{self.name} is in good academic standing."
        else:
            return f"{self.name} is not in good academic standing."

class GraduateStudent(Student):
    def __init__(self, name, major, gpa_for_semesters):
        Student.__init__(self, name, major, gpa_for_semesters)
    
    def __str__(self):
        return f"{self.name} is a graduate student studying {self.major}."
    
    def is_in_good_standing(self):
        if(self.calculate_average_gpa() >= 3.0):
            return f"{self.name} is in good academic standing."
        else:
            return f"{self.name} is not in good academic standing."