"""
    8. Output:
        1). open: model should be default value "r"(read only);
        2). file.readlines(): read all the lines and return them as list;
        3). can directly loop through the lines of the file;

    9. str.strip:
        1). str.strip():
            to remove whitespace from str(start and end position);
        2). str.lstrip():
            to remove whitespace from str(start position);
        3). str.rstrip():
            to remove whitespace from str(end position);

    10. sorted(iterable, key=None, reverse=False)

"""

""" 
    question:
        because a "\n" was manually inserted when write input the name before,
        and now the print result will have double "\n",
        because the end parameter also has the default parameter "\n".

    solutions:
        1. make print's parameter end is "";
        2. use str.rstrip(), to remove whitespace from str(end position);
"""

"""
output version 1 print
with open("names.txt","r") as file:
    lines = file.readlines()
    # print(lines)
    for line in lines:
        # print(f"hello, {line}", end="")
        print(f"hello, {line.rstrip()}")
"""

# output version 2 print by sorted
# with open("names.txt") as file:
#     # can directly loop through the lines of the file
#     for line in sorted(file): # sorted file by alphabetical
#         print(f"hello, {line.rstrip()}") # print names by sorted order

# output version 3 sorted and modify the file
with open("names.txt", ) as file:
    # sorted can reverse by "reverse = True"
    sorted_lines = sorted(file.readlines(), reverse = True) # use variable store sorted lines

with open("names.txt","w") as file: # use "w" parameter to rewrite names.txt file
    for line in sorted_lines:
        file.write(line)

