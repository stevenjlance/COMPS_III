from Week3.assignment.school import *

def test_can_create_person():
    '''Test that the person object is created correctly'''
    person_1 = Person("John", 17, "Canada")
    assert person_1.name == "John"
    assert person_1.age == 17
    assert person_1.country == "Canada"

def test_person_string():
    '''Test that the __str__ method returns the correct string'''
    person_1 = Person("John", 17, "Canada")
    assert str(person_1) == "John is 17 years old and is from Canada."

def test_can_make_student():
    '''Test that the student object is created correctly'''
    student = Student("John", 17, "Canada", "Computer Science", 3.5)
    assert student.name == "John"
    assert student.age == 17
    assert student.country == "Canada"
    assert student.major == "Computer Science"
    assert student.gpa == 3.5
    assert isinstance(student, Student) == True
    assert isinstance(student, Person) == True

def test_student_study():
    '''Test that the study method returns the correct string'''
    student = Student("John", 17, "Canada", "Computer Science", 3.5)
    assert student.study() == "John is studying Computer Science with a current GPA of 3.5"

def test_can_make_staff():
    '''Test that the staff object is created correctly'''
    staff = Staff("Jane", 30, "USA", "Professor", "Computer Science")
    assert staff.name == "Jane"
    assert staff.age == 30
    assert staff.country == "USA"
    assert staff.position == "Professor"
    assert staff.department == "Computer Science"
    assert isinstance(staff, Staff) == True
    assert isinstance(staff, Person) == True

def test_staff_work():
    '''Test that the work method returns the correct string'''
    staff = Staff("Jane", 30, "USA", "Professor", "Computer Science")
    assert staff.work() == "Jane works as a Professor in the Computer Science department."