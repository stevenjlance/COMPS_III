from polymorphism import *
import pytest 

def test_student():
    '''Test that the student object is created correctly'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    assert student1.name == "John"
    assert student1.major == "Computer Science"
    assert str(student1) == "John is studying Computer Science."

def test_cannot_directly_access_gpa():
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    with pytest.raises(AttributeError, match="has no attribute '__gpa_for_semesters'"):
        # Attempt to access a the gpa attribute directly
        _ = student1.__gpa_for_semesters

def test_can_get_gpa():
    '''Test that the get_gpa method returns the correct value'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert student1.get_gpa() == [3.5, 4.0, 3.0]
    assert student2.get_gpa() == [2.5, 3.0, 3.5, 4.0, 3.0]

def test_can_set_gpa():
    '''Test that the set_gpa method sets the correct value'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    student1.set_gpa([3.0, 3.5, 4.0])
    student2.set_gpa([3.0, 3.5, 4.0, 3.0, 3.5])
    assert student1.get_gpa() == [3.0, 3.5, 4.0]
    assert student2.get_gpa() == [3.0, 3.5, 4.0, 3.0, 3.5]

def test_can_calculate_gpa():
    '''Test that the calculate_average_gpa method returns the correct value'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert student1.calculate_average_gpa() == 3.5
    assert student2.calculate_average_gpa() == 3.2

def test_in_good_standing():
    '''Test that the is_in_good_standing method returns the correct value'''
    student1 = Student("John", "Computer Science", [3.5, 4.0, 3.0])
    student2 = Student("Becky", "Mathematics", [2.5, 3.0, 3.5, 4.0, 3.0])
    assert student1.is_in_good_standing() == "John is a student."
    assert student2.is_in_good_standing() == "Becky is a student."

def test_undergraduate_student():
    '''Test that the undergraduate student object is created correctly'''
    undergrad_student = UndergraduateStudent("Adama", "Marketing", [2.0, 3.3, 3.5])
    assert undergrad_student.name == "Adama"
    assert undergrad_student.major == "Marketing"
    assert undergrad_student.get_gpa() == [2.0, 3.3, 3.5]

def test_undergraduate_polymorphism():
    '''Test that the __str__ method returns the correct value for undergraduate students'''
    undergrad_student = UndergraduateStudent("Adama", "Marketing", [2.0, 3.3, 3.5])
    assert str(undergrad_student) == "Adama is an undergraduate student studying Marketing."
    assert undergrad_student.is_in_good_standing() == "Adama is in good academic standing."

def test_graduate_student():
    '''Test that the graduate student object is created correctly'''
    grad_student = GraduateStudent("Ivan", "Math", [2.0, 3.3, 3.5])
    assert grad_student.name == "Ivan"
    assert grad_student.major == "Math"
    assert grad_student.get_gpa() == [2.0, 3.3, 3.5]

def test_graduate_polymorphism():
    '''Test that the __str__ method returns the correct value for graduate students'''
    grad_student = GraduateStudent("Ivan", "Math", [2.0, 3.3, 3.5])
    assert str(grad_student) == "Ivan is a graduate student studying Math."
    assert grad_student.is_in_good_standing() == "Ivan is not in good academic standing."