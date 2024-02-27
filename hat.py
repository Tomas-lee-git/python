"""
    1. class methods:
        1). some action to be associated with the class itself,
            no matter what the specific objects own values or instance variables are;
        2). keyword, @classmethod:
            i. don't pass self any more (reference to instance object);
            ii. pass in the reference to the class itself: cls;
            iii. call class method by Student.sort();
        3). class variable, can be used in any of methods by cls.variable;
        4). instance object can call classmethod succeed;
        5). can call cls(parameters) to instantiate a object, same as call Class(parameters)
"""
# import random
from random import choice

class Hat:
    # class variable
    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {choice(cls.house)}")

hat = Hat()
hat.sort("Harry")

Hat.sort("Harry")
