"""
    csv module:
        1. csv.reader(csvfile, dialect='excel', **fmtparams):
            1). return a reader object that will process lines from the given csvfile;
            2). each row read from the csv file is returned as a list of strings:
                    the row element has be split(",") and it  will be:
                        [row1, string, …],
                        [row2, string, …],

        2. csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds):
            1). Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter;
            2). The fieldnames parameter is a sequence. If fieldnames is omitted, the values in the first row of file f will be used as the fieldnames;
            3). return an iterable object whose elements are dict:
                key is the content of the first column;
                value is the contents of each column  except the fist(which will be the key);

        3. file.seek(0): after reader/DictReader(), need to seek to the beginning of the file
            just like people's reading habits, after reading a file, 
            if you want to read it again, you need to go back to the starting point of the file;

"""
import csv

colleagues = []
with open("colleagues.csv") as file:
# csv.reader()
    reader = csv.reader(file)
    # print(f"reader is {reader}")
    # for row in reader:
    #     # print(f"row is {row}") # row is ['Dowson', 'dog', '23', 'abc,def']
    #     colleagues.append({"name":row[0],"breed":row[1]})

    for name, breed, age, evaluate in reader: # if iterable's element is list, just unpack it in this place
        colleagues.append({
            "name": name, 
            "breed": breed,
            "age": age,
            "evaluate": evaluate,
            })
    # print(f"colleagues list is {colleagues}")

    sorted_colleagues = sorted(colleagues, key = lambda colleague : colleague["age"], reverse="True")

    # for colleague in sorted_colleagues : 
    #     print(f"{colleague['name']} is a {colleague['breed']}, age is {colleague['age']}, evaluate is {colleague['evaluate']}") 


# csv.DictReader() add column key, insensitive to column order
    file.seek(0) # seek to the beginning of the file
    dict_reader = csv.DictReader(file)
    # print(f"dict_reader is {dict_reader}")
    for colleague in dict_reader: # directly unpack dict
        """
            question:
                the code inside the loop is not executed

            reason: https://stackoverflow.com/questions/11150155/why-cant-i-repeat-the-for-loop-for-csv-reader
                The csv reader is an iterator over the file. 
                Once you go through it once, you read to the end of the file, so there is no more to read. 
                If you need to go through it again, you can seek to the beginning of the file:
                    fh.seek(0)

            check:
                i executed "reader = csv.reader(file)" on line 19, so i need to resolve it

            solution:
                file.seek(0)
        """
        # print(f"dict_reader's element is {colleague}")
        print(f"{colleague["name"].title()} is a {colleague["breed"]}, its age is {colleague["age"]} years old. We all think he is a {colleague["evaluate"]}")
    

    