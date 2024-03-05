"""
    1. variables only exist when the program is running and disappear when the program exists;
        but, we need something to preserve the information long term: File I/O;
    2. File I/O(input and output of files):
        hang on to information [long term], writing code that:
            Input: write to that is [save information];
            Output: read from that is [load information];

    3. "for i in obj" loop:
        if obj is list: i is the every element;
        if obj is dict: i is the every key;

    4. range(len):
        return a list of specific length, element is init from 0;
        range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    5. list operations:
        1). list[start, end]:  
            include list[start] but don't include list[end]；
        2). list.append(element):
            append element into a list with last element;
        3). sorted(list):
            return sorted list, the default sort rule is "numerical and alphabetical order"
    
    6. Input:   
        open/create => write/read => close/save and close: 
            first step: open/create a file:
                file_obj = open(file, mode="r"):
                    1). equivalent of like double clicking on an icon on Mac or Pc;
                    2). open a file but to open it up programmatically:
                        so the programer can read information from it and write information to it;
                    3). [file] is file path, include absolute or relative path;
                            'r' open for reading (default);
                            ❕'w' open for writing, truncating the file first(recreate: first erase and then write new information);
                            'x' open for exclusive creation, failing if the file already exists;
                            ✅'a' open for writing, appending to the end of file if it exists;
                            'b' binary mode;
                            't' text mode (default);
                            '+' open for updating (reading and writing);
                    4). file_obj is a [file object], can write and read information form this file link;

            second step: write to/read from the file:
                5). file_obj.write(str), write to information;

            third step: close/close and save the file:
                6). file_obj.close(), close and effectively save the file;

            🩷other: use "with…as" can ignore file.close() func;
        
    7. CLI(command line interface) for file:
        1): code a, create or open a;
        2): mkdir b, create an folder named b;
        3): rm c, delete a file named c;
        4): rm -r d, delete a file named d(not empty);

"""

n = int(input("How many names do you want to collect? "))
names = []  # empty list, can add things

for _ in range(n):  # range(len), return a list of specific length
    names.append(
        input("What's your name ? ").title()
    )  # add an element into a list with last element


"""
input version  1
for name in sorted(names): # sorted(list) will return sorted list
    print(f"hello, {name}")
"""

# input version  2
# file.write(names) # TypeError: write() argument must be str, not list

for name in sorted(names):
    # file.write() without newline, should manually use "/n"
    # write to names.txt file, if the file doesn't exist yet it's going to create the file
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")  # write information to file
        # file.close() # close and effectively save the file
