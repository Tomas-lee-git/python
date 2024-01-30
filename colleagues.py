"""
    1. .csv file operate:
        1). use split(",") to get specific values;
    
    2. split():
        1). return list;
        2). use a,b,c,…… = stir.split() to get the variable that refers to the order

"""
# version 1 ,use split(",") to get specific values
names = []
breeds = []
with open("colleagues.csv") as file:
    for line in file:
        name, breed = line.rstrip().split(",")
        # print(f"split return value is {line.rstrip().split(",")}")
        names.append(name)
        breeds.append(breed)
        print(f"His name is {name} and his breed is {breed}.")
print(f"names list is {names}", f"breeds list is {breeds}", sep="\n")

    