"""
    1. inheritance, for reuse same logic:
        1). extract common logic as a class to be inherited: superclass class;
        2). def subclass(superclass): ...
        3). super() is reference to superclass;
        4). if superclass and subclass define same method such as __init__:
            i. should do call the superclass's same method manually with parameter:
                super().__init__(parameter);
            ii. otherwise, will only call the subclass's method and override superclass's same method:
                AttributeError: 'Student' object has no attribute 'name'

    2. hasattr(object, attribute_name): check if the object has attribute_name;

    3. python error has been inherited: valueError <= Exception <= BaseException;

"""
# extract common logic as a class to be inherited
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    def __str__(self):
        if hasattr(self, "house"):
            return f"hello, my name is {self.name}, my house is {self.house}"
        elif hasattr(self, "subject"):
            return f"hello, my name is {self.name}, my subject is {self.subject}"
        else:
            return f"hello, my name is {self.name}"

class Student(Wizard):
    def __init__(self, name, house):
        # if not name:
        #     raise ValueError("Missing name")
        # self.name = name
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        # if not name:
        #     raise ValueError("Missing name")
        # self.name = name

        super().__init__(name)
        self.subject = subject


def main():
    wizard = Wizard("Lee")
    print(wizard)

    student = Student("Lee", "China")
    print(student)

    professor = Professor("Joey", "Math")
    print(professor)


if __name__ == "__main__":
    main()