"""
    1. type(), will return data type:
        1): print(type(Student)) # <class 'type'>;
        2): print(type(student)) # <class '__main__.Student'>;
"""
print(type(50)) # <class 'int'>
print(type(int(50))) # <class 'int'>

print(type(1.2)) # <class 'float'>
print(type(float(1.2))) # <class 'float'>

print(type("50")) # <class 'str'>
print(type(str("50"))) # <class 'str'>

print(type({})) # <class 'dict'>
print(type(dict())) # <class 'dict'>

print(type([])) # <class 'list'>
print(type(list())) # <class 'list'>

print(type(())) # <class 'tuple'>
print(type(tuple())) # <class 'tuple'>

print(type(False)) # <class 'bool'>
print(type(bool(False))) # <class 'bool'>

def func():
    return "ha"
print(type(func)) # <class 'function'>

class Student:
    def __init__(self, name, book):
        self.name = name
        self.book = book
    def __str__(self):
        return f"I'm a student, my name is {self.name}"
    def read(self):
        print(f"ok, i'm reading {self.book}")
print(type(Student)) # <class 'type'>

print(type(str)) # <class 'type'>


student = Student("Lee", "Learning Japanese")
print(student)
student.read()

print(type(student)) # <class '__main__.Student'>