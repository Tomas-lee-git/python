"""
    1. .csv file operate:
        1). use split(",") to get specific values;
    
    2. split():
        1). return list;
        2). use a,b,c,…… = stir.split() to get the variable that refers to the order
    
    3. 
        1). sorted(iterable, /, *, key=None, reverse=False);
        2). ❌ sorted([{},{}]):
            TypeError: '<' not supported between instances of 'dict' and 'dict';
        3). ❌ sorted(colleagues, key="name")
            TypeError: 'str' object is not callable;

"""
# version 1 ,use split(",") to get specific values
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

print(f"colleagues dictionary is {colleagues}")

def get_name(colleague):
    return colleague["name"]

for colleague in sorted(colleagues, key = get_name):
    # print(f"sorted(colleagues) is {sorted(colleagues)}") # TypeError: '<' not supported between instances of 'dict' and 'dict'
    print(f"{colleague['name']} is a {colleague['breed']}") #注意：在""中需要使用''



    