"""
    8. Output:
        1). open: model should be default value "r"(read only);
        2). file.readlines(): read all the lines and return them as list;

    9. str.strip:
        1). str.strip():
            to remove whitespace from str(start and end position);
        2). str.lstrip():
            to remove whitespace from str(start position);
        3). str.rstrip():
            to remove whitespace from str(end position);

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
output 版本1
with open("names.txt","r") as file:
    lines = file.readlines()
    # print(lines)
    for line in lines:
        # print(f"hello, {line}", end="")
        print(f"hello, {line.rstrip()}")
"""

# output 版本2
with open("names.txt","r") as file:
    for line in file: # can directly loop through the lines of the file
        print(f"hello, {line.rstrip()}")