"""
    1. .csv file operate:
        1). use split(",") to get specific values;
    
    2. split():
        1). return list;
        2). use a,b,c,…… = str.split() to get the variable that refers to the order
    
    3. sorted(iterable, /, *, key=None, reverse=False)
        1). ❌ sorted([{},{}]):
            TypeError: '<' not supported between instances of 'dict' and 'dict';
        2). ❌ sorted(colleagues, key="name")
            TypeError: 'str' object is not callable;
        3). key specifics a function of one argument that is used to extract a comparison key from each element in iterable
    
    4. lambda function: 
        1). an anonymous function that just has no name, because only going to call it in once place;
        2). lambda [parameter] : expression:
            need:
                a: need keyword: lambda;
                b. parameter is optional;
                c. : symbol to separate parameter and return value;
                d. expression;
            unnecessary:
                a. keyword: def;
                b. function name;
                c. parameter's parentheses;
                c. keyword: return;
    
    5. .csv file:
        1). can put quotes("") around any English string that itself contains a comma(,);

"""
# step 1 ,use split(",") to get specific values
colleagues = []
with open("colleagues.csv") as file:
    for line in sorted(file):
        name, breed = line.rstrip().split(",") # unpack
        # print(f"split return value is {line.rstrip().split(",")}")
        # print(f"His name is {name} and his breed is {breed}.")

        # to sort csv information by specific column name
        colleague = { # 注意：key 应该被明显地写成 str 类型，也就是说，需要加"key"，否则就是变量了
            "name": name,
            "breed": breed
        }
        colleagues.append(colleague)

# print(f"colleagues list is {colleagues}")


# step 2, sort a list of dictionaries by dictionaries's key

# def sort_name(colleague): # each element in iterable
#     return colleague["names"] # specifics one argument that is used to extract a comparison key

# def sort_breed(colleague):
#     return colleague["breed"]

# create function to return a specific function 😊
# sort_by("breed")
# sort_by("name")
def sort_by(key):
    def sort(dict):
        return dict[key]
    return sort

# lambda [parameter] : expression:

for colleague in sorted(colleagues, key = lambda colleague : colleague["breed"], reverse="True"): # key specifics a function of one argument that is used to extract a comparison key from each element in iterable
    # print(f"sorted(colleagues) is {sorted(colleagues)}") # TypeError: '<' not supported between instances of 'dict' and 'dict'
    print(f"{colleague['name']} is a {colleague['breed']}") #注意：在""中需要使用''



    