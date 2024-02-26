"""
    1. oop: 
        1). object oriented programming;
        2). oop more generally encourages to encapsulate inside of a class all functionality related to that class;

    2. tuple: use tuple to return multiple values:
        1): return A,B,C is return one data, the data's type is tuple;
        2): fn can return multiple values: A,B,C and accept multiple values by unpack with sequence: A,B,C = fn();
        3). (A,B,C) is equal A,B,C but more readable and verbosely;
        4). tuple is similar to a list but it's indeed just immutable;
        5). tuple can use [index] to get element;
        6). ❕ TypeError: 'tuple' object does not support item assignment,
                it can be used to protect variables from being changed;
    
    3. [](list) vs ()(tuple):
        1). has sequence;
        2). use [index] to get element;
        3). list's element can be changed, but tuple's element can't to be changed;
        4). list must have square bracket [], but tuple can ignore parentheses ();

    4. classes:
        1). create own data types and actually give them names;
        2). a class is kind of like a blueprint or mold: designed exactly as self want;
        3). doc url: https://docs.python.org/3/tutorial/classes.html;
        4). keyword Class and use . to add attribute:
            class Student(capital letter);
            student =  Student();
            student.name = "小野";
        5). use classes will create an object;
        6). Student generally known as a Constructor that is going to constructor a student object;
        7). when Student() is called, __init__ function will be called automatically;
        8). __init__(self, parameters):
            a. initializes the contents of the object;
            b. accept parameters(self, other external parameters passed in);
            c. the parameter "self" is a link to access the current object(an instance of class);
            d. can check parameter and raise custom error alert;
        9). __str__(self):
            a. python will automatically call this function when the object(an instance of class) as a string ;
            b. if this function is not to be defined, will see the object as string with:
                <__main__.Student object at 0x101efe690(memory id)
            c. "self" is a link to access the current object(an instance of class);
        10). built in function:
            a. create functions built in class, AKA methods;
            b. default methods such as: __init__, __str__;
            c. method(self, parameters):
                i. method take at least one argument called self to access the current object;
                ii. other arguments is passed in by the programer;
                iii. this method can be called directly by object outside the class;
                iiii. __init__ and __str__ will be called automatically but custom methods must be called manually;
                iiiii. python will automatically pass in at least one argument to every method in a class, 
                    and the special argument is "self", reference to the current object;
        11). properties: 
            a. the object's attributes;
            b. can add, remove, change properties after construct;
        12). keywords:  @property and @property_name.setter:
            a. decorate symbol @;
            b. getter: is a function in class that gets some attribute,
                @property
                get_attribute_name(self):
                    return self._attribute_name
            b. setter: is a function in class that sets some attribute,
                @attribute_name.setter
                set_attribute_name(self, new_value):
                    self._attribute_name = new_value
            d. can use getters and setters to manage change to properties;
            e. if write property setter and getter:
                when get property, will call property's corresponding getter function;
                when set property(either create or override), will call property's corresponding setter function;
            f. ❕❕❕When getting or setting up a property:
                    must rename the attribute locally,
                    the convention is to prefix it with an underscore _;
                RecursionError: maximum recursion depth exceeded while calling a Python object
                

                

    5. ... :
        ... is a valid placeholder, wait to implement logic;

    6. class instance vs dict:
        1). class instance use . to add/get attribute, while dict use ["key"] to add/get values;
        2). class create object and object can only add specific attributes, while dict can add any key;
        3). class can ensure the correctness of data, error check, designed more complicated software;

    7. if not variable:
        if name not : equal if name == "": , if not "", will return True, else will return False;

    8. if not in str/list:
        if element or substr is not in list or str, not in will return True, else will return False;
    
    9. raise:
        1). programer can create own exceptions when something just really goes wrong:
            not wrong enough that want to quit and exit the whole program(sys.exit(msg)),
            but enough that need to somehow alert the programer that there has been an error something exceptional and let them to use try to catch that exception;
        2). raise errorType(alert message):
            raise ValueError("Missing name")

    10. Exception handling: Differentiating between instances of the same error in Python:
            a = 'hello'
        try:
           a.append(2)
        except AttributeError as e:
           if 'str' in e.args[0]:
               print('Need to handle string')
           elif 'float' in e.args[0]:
               print('Need to handle float')

    11.

"""
class Student:
    def __init__(self, name, country, patronus):
        # print(f"self is {self}") # self is <__main__.Student object at 0x101efe690>

        self.name = name
        self.country = country
        self.patronus = patronus

        # print(f"self is {self}") # self is <__main__.Student object at 0x103a866c0>

    def __str__(self):
        return f"{self.name} from {self.country}, and patronus is {self.patronus}"

    def show_skill(self):
        skill = ""
        match self.country:
            case "China":
                skill = "study"
            case "Japan":
                skill = "comics"
            case "America":
                skill = "play computer games"
            case "Canada":
                skill = "ski"
            case _:
                skill = "/"

        print(f"I'm good at {skill}")

        # skills = {
        #     "China": "study",
        #     "Japan": "comics",
        #     "America": "play computer games",
        #     "Canada": "ski"
        # }
        # print(f"I'm good at {skills[self.country]}")

    # name Getter
    @property
    def name(self):
        return self._name #_

    # name Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name #_
    
    # country Getter
    @property
    def country(self):
        return self._country # _

    # country Setter
    @country.setter
    def country(self, country):
        print(f"set country with {country}")
        if country not in ["China","Japan","America","Canada"]:
            raise ValueError("Invalid country and region")
        self._country = country # _

def main():
    # student = get_student()
    # student[1] = "America" # TypeError: 'tuple' object does not support item assignment

    # name, country = get_student()
    # print(f"{name} from {country}") 

    # print(f"{student[0]} from {student[1]}") 

    # """
    #     ❕two things:
    #         1). python dict's value must use square bracket;
    #         2). pay attention to the matching of single quotes and double quotes, do not nest the same quotes;
    # """
    # student = get_student()
    # print(f'{student["name"]} from {student["country"]}')

    # student = get_student()
    # print(f"{student.name} from {student.country}")

    # student = get_student()
    # student.show_skill()
    # print(student.__str__())

    student = get_student()
    # student.country = "None" # can use Setter function to stop this operate
    print(student)


def get_name():
    return input("What's your name ? ").title()

def get_country():
   return input("Where are you from ? ").title()

def get_student_information():
    name = input("What's your name ? ").title()
    country = input("Where are you from ? ").title()
    patronus =  input("What's your patronus ? ").title()
    return (name, country, patronus)

def get_student():
    # name = get_name()
    # country = get_country()
    # return (name, country)
    
    # return { # python dict's key must be "str" literally
    #     'name' : get_name(),
    #     'country' : get_country()
    # }

    # student = Student()
    # student.name = get_name()
    # student.country = get_country()

    # name = get_name()
    # country = get_country()

    name, country, patronus = get_student_information()

    try:
        return Student(name, country, patronus)
    except ValueError as e:
        print(f"e is {e}, { e == "Invalid country and region"}")
        if e.args[0] == "Missing name":
            print("please input name")
            name = get_name()
            return Student(name, country, patronus)

        elif e.args[0] == "Invalid country and region":
            print("please input country and region")
            country = get_country()
            return Student(name, country, patronus)
    else:
        print("everything is ok")



"""
    👇这行代码的意思：只有在直接执行这个文件的时候，main() 才会被调用；
    想要避免的情况是：当本文件被其它文件作为 module/package import时，main() 不会“意外地”被执行；
"""
if __name__ == "__main__":
    main()