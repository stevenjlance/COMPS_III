class Student:
    student_id = 1
    def __init__(self, name, major, gpa_for_semesters):
        self.name = name
        self.major = major
        self.gpa = gpa_for_semesters
        self.__student_id = Student.student_id
        Student.student_id += 1

    def get_student_id(self):
        return self.__student_id
    
    def set_student_id(self, student_id):
        self.__student_id = student_id
    
    def __str__(self):
        return f"{self.name} is studying {self.major}."
    
    def calculate_average_gpa(self):
        return sum(self.gpa) / len(self.gpa)
    
    def is_in_good_standing(self):
        return f"{self.name} is a student."

class UndergraduateStudent(Student):
    def __init__(self, name, major, gpa_for_semesters, age):
        Student.__init__(self, name, major, gpa_for_semesters)
        self.age = age
    
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