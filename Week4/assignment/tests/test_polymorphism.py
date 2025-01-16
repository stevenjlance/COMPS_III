from polymorphism import *
import pytest 

def test_student():
    '''Test that the student object is created correctly'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    assert student1.name == "John"
    assert student1.major == "Computer Science"
    assert student1.gpa == [3.5, 4.0, 3.0]

def test_can_calculate_gpa():
    '''Test that the calculate_average_gpa method returns the correct value'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert student1.calculate_average_gpa() == 3.5
    assert student2.calculate_average_gpa() == 3.2

def test_can_get_student_id():
    '''Test that the get_student_id method returns an integer'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert type(student1.get_student_id()) == int
    assert type(student2.get_student_id()) == int

def test_can_set_student_id():
    '''Test that the set_student_id method sets the correct value'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    student1.set_student_id(10)
    student2.set_student_id(20)
    assert student1.get_student_id() == 10
    assert student2.get_student_id() == 20

def test_cannot_directly_access_id():
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    with pytest.raises(AttributeError, match="has no attribute '__student_id'"):
        # Attempt to access a the student_id attribute directly
        _ = student1.__student_id

def test_undergraduate_student():
    '''Test that the undergraduate student object is created correctly'''
    undergrad_student = UndergraduateStudent("Roberto", "Game Design", [3.5, 4.0, 3.0], 22)
    assert undergrad_student.name == "Roberto"
    assert undergrad_student.major == "Game Design"
    assert undergrad_student.gpa == [3.5, 4.0, 3.0]
    assert undergrad_student.age == 22
    assert undergrad_student.is_in_good_standing() == "Roberto is in good academic standing."

def test_undergraduate_polymorphism():
    '''Test that the __str__ method returns the correct value for undergraduate students'''
    undergrad_student = UndergraduateStudent("Roberto", "Game Design", [3.5, 4.0, 3.0], 22)
    assert str(undergrad_student) == "Roberto is an undergraduate student studying Game Design."

def test_graduate_student():
    '''Test that the graduate student object is created correctly'''
    grad_student = GraduateStudent("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert grad_student.name == "Becky"
    assert grad_student.major == "Mathematics"
    assert grad_student.gpa == [2.5, 3.0, 3.5, 4.0, 3.0]
    assert grad_student.is_in_good_standing() == "Becky is in good academic standing."

def test_graduate_polymorphism():
    '''Test that the __str__ method returns the correct value for graduate students'''
    grad_student = GraduateStudent("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert str(grad_student) == "Becky is a graduate student studying Mathematics."