"""     
    1.lambda function: 
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

    2. str.upper("abc"):
        1). equal abc.upper();

    3. list comprehension:
        1). the ability to very easily construct a list with one-liner,
            and without loop and new empty [];
        2). map:
            i. map(function, iterable,...):
                a. make an iterator that computes the function using arguments from each of the iterables. 
                    stops when the shortest iterable is exhausted;
                b. function is action for iterable;
                c. iterable is contain many children need to be actioned;
            ii. create a new list more simply:
                a. [element.action() for element in list];
                b. in an empty list, for loop an exist list;
                c. do something for every element before "for loop" logic;
                d. will generate a new list with every element.action()'s return value;
"""

def main():
    yell("This is cs 50")
    # yell(["This", "is", "cs50"])

def upper_func(v):
    return v.upper()

def yell(*words):
    # print(phrase.upper())

    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())
    # # print("word", end="") # wordwordwordword%
    # print(uppercased) # ['THIS', 'IS', 'CS50']
    # print(*uppercased) # print(*uppercased) => print("This", "is", "cs50") => THIS IS CS50

    # uppercased = map(lambda word:word.upper(), words)
    # uppercased = map(str.upper, words)

    uppercased = [word.upper() for word in words]
    print(uppercased) # ['THIS', 'IS', 'CS50']
    print(*uppercased) # print(*uppercased) => print("This", "is", "cs50") => THIS IS CS50

if __name__ == "__main__":
    main()