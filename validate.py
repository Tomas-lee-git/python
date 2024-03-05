"""
    1. regexes(regular expression):
        1). just a pattern and use patterns to [match] on some kind of data;
        2). validate the user input, such as: email, phone number and etc;
        3). filter data;

    2. list("str"): 
        will split a word into a list:
            return ["s","t","r"]

    3. in:
        1). check if a element exists in a list => element in list;
        2). check if a sub str exists in a str => str in str;

    4. connect bool expression:
        1). or  连接多个条件，符合其中一个条件，都会进入相关的逻辑;
        2). and 连接多个条件，符合其中所有的条件，才会进入相关的逻辑;

    5. str:
        1). str.startswith();
        2). str.endswith();
        3). ❕ s;
    
    6. re: https://docs.python.org/3/library/re.html
        1). re.search(pattern, string, flags=0)
    
    7. pattern:
        1). r"regular expression";
        2). any thing:
            ., any character except a newline;
        3). receptions:
            *, 0 or more repetitions;
            +, 1 or more repetitions;
            ?, 0 or 1 repetitions;
            {m}, m repetitions ;
            {m,n}, from m to n repetitions;
        4). escape character:
            . is any character;
            ❌ wrong:
                \. is literally . :
                    SyntaxWarning: invalid escape sequence '\.'
            ✅ right: r"\."

    8. special str:
        1). format string:
            f"str{variable}";
        1). row string:
            r"regular expression \.";
"""

# version 1
"""
while True: # continue asking for input from the user until get a valid email address
    email = input("What's your email? ").strip()
    username, domain = email.split("@")
    # if @ in email: SyntaxError: invalid syntax
    if username and "." in email: # search through the entire string
        print(f"Yes, you input a valid email address: {email}")
        break
    else:
        print("No, you input a invalid email address. Please check and input again.")
"""

# version 2
import re

while True:
    email = input("What's your email? ").strip()
    # mul@gmail.com
    if re.search(r".+@.+\.edu", email):
        print(f"Yes, you input a valid email address: {email}")
        break
    else:
        print("No, you input a invalid email address. Please check and input again.")
