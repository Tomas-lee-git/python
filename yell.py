"""
    1.
        
    2.
"""

def main():
    # yell("This is cs 50")
    yell(["This", "is", "cs50"])

def yell(words):
    # print(phrase.upper())

    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    
    # print("word", end="") # wordwordwordword%
    print(uppercased) # ['THIS', 'IS', 'CS50']
    print(*uppercased) # print(*uppercased) => print("This", "is", "cs50") => THIS IS CS50

if __name__ == "__main__":
    main()