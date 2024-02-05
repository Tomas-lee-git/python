"""
    1. regexes(regular expression):
        1). just a pattern and use patterns to [match] on some kind of data;
        2). validate the user input, such as: email, phone number and etc;

    2. list("str"): 
        will split a word into a list:
            return ["s","t","r"]

    3. in:
        1). check if a element exists in a list => element in list;
        2). check if a sub stir exists in a stir => stir in stir;
        
"""

while True: # continue asking for input from the user until get a valid email address
    email = input("What's your email? ")
    # if @ in email: SyntaxError: invalid syntax
    if "@" in email: # search through the entire string
        print(f"Yes, you input a valid email address: {email}.")
        break
    else:
        print("No, you input a invalid email address. Please check and input again.")