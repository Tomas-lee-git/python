"""
    regular expression:
        1). r"regular expression";

        2). any thing:
            ., any character except a newline;

        3). receptions:
            *, 0 or more repetitions;
            +, 1 or more repetitions;
            ?, 0 or 1 repetitions;
            {m}, m repetitions ;
            {m,n}, from m to n repetitions;

        3). start and end:
            ^: start of the string;
            $: end of the string;

        4). escape character: \
                just allow you to tell the computer to:
                    not treat those symbols specially,
                    but to treat them literally instead;
        5).[]: ❕ only one character
            . : any thing;
            []: specific a set of characters
                only the specified symbol: such as [abc];
            [^]: complementing the set 
                anything except the specified symbol, such as [^@.*];
            [a-z]: 26 lowercase alphabet;
            [A-Z]: 26 uppercase alphabet;
            [a-zA-Z]: 26 alphabet, no matter lowercase or uppercase;
            [0-9]: all numbers;
            [-]: underscore symbol;





"""
import re

while True: 
    email = input("What's your email? ").strip()
    # mul@gmail.com
    # if re.search(r".+@.+\.edu", email): No limit on start and end
        # Yes, you input a valid email address: my email address is abc@def.edu
    if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9_]+\.[edu,gmail]$", email): # add ^ and $ to limit start and end
        print(f"Yes, you input a valid email address: {email}")
        break
    else:
        print("No, you input a invalid email address. Please check and input again.")