"""
    1. str:
        1). str.lower();
        2). str.upper();

    2. regular expression:
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
            [_]: underscore symbol;

        6). short notation:
            \d, [0-9]:
                decimal digit;
            \D, [^0-9]:
                not a decimal digit;

            \s, [   ]:
                whitespace character, space、tab and other white spaces;
            \S, [^   ]:
                not a whitespace character;

            \w, [a-zA-Z0-9_]:
                word characters, as well as numbers and the underscore;
            \W, [^a-zA-Z0-9_]:
                not a word character;
        
        7). [] vs () specific:
            []: one character
                [abcdef], select only one character;
            (): group
                (edu|com|cn), more characters can be selected, such as domains;

        8). re.search(pattern, string, flags = 0):
            flags:
                re.IGNORECASE, ignore case, uppercase or lowercase;
                re.MULTILINE, match different lines of that text;
                re.DOTALL, match any characters(.) including a newline;

        9). group ideas:
            A|B:
            (...):
            (?:...):

        10.validate email address by regular expression:
            https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression?page=1&tab=createdasc#tab-top

        11. re.match(pattern, string, flag):
            1. very similar to re.search except don't have to specify the carrot symbol at the begin(^);


"""
import re

while True: 
    email = input("What's your email? ").strip()
    # mul@gmail.com
    # if re.search(r".+@.+\.edu", email): No limit on start and end
        # Yes, you input a valid email address: my email address is abc@def.edu

    pattern = r"^\w+@\w+\.(edu|com|cn|gov|net|org)$"
    pattern1 = r"^\w+@[\w\.]+\.(edu|com|cn|gov|net|org)$"
    pattern2 = r"^\w+@(\w|\.)+\.(edu|com|cn|gov|net|org)$"



    if re.search(pattern2, email, re.IGNORECASE): # add ^ and $ to limit start and end
        print(f"Yes, you input a valid email address: {email}")
        break
    else:
        print("No, you input a invalid email address. Please check and input again.")