"""
    1. oop: 
        object oriented programming;

    2. tuple: use tuple to return multiple values:
        1): return A,B,C is return one data, the data's type is tuple;
        2): fn can return multiple values: A,B,C and accept multiple values by unpack with sequence: A,B,C = fn();
        3). (A,B,C) is equal A,B,C but more readable and verbosely;
        4). tuple is similar to a list but it's indeed just immutable;
        5). tuple can use [index] to get element;


"""
def main():
    # student = get_student()
    # print(f"{student["name"]} from {student["house"]}") # python dict's value must use square bracket

    # name, house = get_student()
    # print(f"{name} from {house}") 

    student = get_student()
    print(f"{student[0]} from {student[1]}") 


def get_name():
    return input("What's your name ? ").title()

def get_house():
   return input("Where are you from ? ").title()

def get_student():
    # return { # python dict's key must be "str" literally
    #     'name' : get_name(),
    #     'house' : get_house()
    # }
    name = get_name()
    house = get_house()
    return name, house
    
"""
    👇这行代码的意思：只有在直接执行这个文件的时候，main() 才会被调用；
    想要避免的情况是：当本文件被其它文件作为 module/package import时，main() 不会“意外地”被执行；
"""
if __name__ == "__main__":
    main()