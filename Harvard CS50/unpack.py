"""
    1. unpack:
        1). unpack list to multiple variables:
            fist, second = [1, 2]
        2). unpack list to multiple function parameters:
            add a "*" before list parameter:
                func(*[1, 2, 3]) => func(a, b, c);
    2. * symbol:
        1). for regular expression, * means any number;
        2). for number, * means multiple;
        3). for string, * means concatenate str with multiple numbers;
        4). for unpack:
            a. single * means unpack list parameter to individual parameters;
            b. double ** means unpack dict parameter to individual parameters(pass key = value pairs),
                the premise is that the key of the dict is consistent with the name of function parameter;
    
    3. name of parameters:
        1). func(a = 1, b = 2, c = 3 ) => func(a, b, c);
        2). if name the parameters when calling a function,
            don't need to follow the order of parameters when the function was defined;

    4. variable numbers of arguments:
        1). positional arguments should precede than named arguments;
        2). *args:
                i. take some variable number of positional arguments;
                ii. args is tuple: (1, 2, 3);
        3). **kwargs:
                i. take some variable number of named arguments(keyword arguments);
                ii. kwargs is dict: {'key1': 'ha', 'key2': 'xi'};
        4). ❕ defined with */**, but use without */**;

    5. 

"""

# unpack list

# first_name, second_name =  input("What's your name? ").split()
# print(f"first_name is {first_name}")
# print(f"second_name is {second_name}")


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# unpack list parameter

# wallet = [100, 50, 25]
# print(f"{total(*wallet)} knuts")
# TypeError: total() missing 2 required positional arguments: 'sickles' and 'knuts'

# name of parameters

# print(f"{total(sickles = 50, galleons = 100, knuts = 25)} knuts")

# unpack dict

# wallet = {
#     "sickles": 50,
#     "galleons": 100,
#     "knuts": 25
# }
# print(f"{total(**wallet)} knuts")

# *args and *kwargs


def f(*args, **kwargs):
    print(f"Positional arguments is {args}")  # (1, 2, 3)
    print(f"Positional arguments's type is {type(args)}")  # <class 'tuple'>
    print(f"Keyword arguments is {kwargs}")  # {'key1': 'ha', 'key2': 'xi'}
    print(f"Keyword arguments's type is {type(kwargs)}")  # <class 'dict'>


f(1, 2, 3, key1="ha", key2="xi")


def count(*args, **kwargs):
    add = 0
    for v in args:
        add += v
    return (add * kwargs["multiple"]) / kwargs["divide"]


print(count(1, 2, 3, 4, 5, multiple=5, divide=15))
