"""
    1. unpack:
        1). unpack list to multiple variables:
            fist, second = [1, 2]
        2). unpack list to multiple function parameters:
            add a "*" before list parameter:
                func(*[1, 2, 3]) => func(a, b, c);
    2. * symbol:
        i. for regular expression, * means any number;
        ii. for number, * means multiple;
        iii. for string, * means concatenate str with multiple numbers;
        iiii. for unpack, * means unpack list parameter to individual parameters;
    
    3. name of parameters:
        i. func(a = 1, b = 2, c = 3 ) => func(a, b, c);
        ii. if name the parameters when calling a function,
            don't need to follow the order of parameters when the function was defined;

"""
# unpack list

# first_name, second_name =  input("What's your name? ").split()
# print(f"first_name is {first_name}")
# print(f"second_name is {second_name}")

# unpack list parameter

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

# wallet = [100, 50, 25]
# print(f"{total(*wallet)} knuts")
# TypeError: total() missing 2 required positional arguments: 'sickles' and 'knuts'

# name of parameters
print(f"{total(sickles = 50, galleons = 100, knuts = 25)} knuts")

