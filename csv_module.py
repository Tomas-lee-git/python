"""
    csv module:
        1. csv.reader(csvfile, dialect='excel', **fmtparams):
            1). return a reader object that will process lines from the given csvfile;
            2). each row read from the csv file is returned as a list of strings:
                    the row element will be:
                        [row1, string, …],
                        [row2, string, …],

"""
import csv

colleagues = []
with open("colleagues.csv") as file:
    reader = csv.reader(file)
    # print(f"reader is {reader}")
    # for row in reader:
    #     # print(f"row is {row}") # row is ['Dowson', 'dog', '23', 'abc,def']
    #     colleagues.append({"name":row[0],"breed":row[1]})

    for name, breed, age, other in reader: # if iterable's element is list, just unpack it in this place
        colleagues.append({
            "name": name, 
            "breed": breed,
            "age": age,
            "other": other,
            })

# print(f"colleagues list is {colleagues}")

sorted_colleagues = sorted(colleagues, key = lambda colleague : colleague["age"], reverse="True")

for colleague in sorted_colleagues : 
    print(f"{colleague['name']} is a {colleague['breed']}, age is {colleague['age']}, other is {colleague['other']}") 



    