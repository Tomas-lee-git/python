"""
    1. str.replace(A, B): 
        find A and replace A with B;
    
    2. str.removeprefix(A): 
        remove str's prefix A;

    3. re.sub(pattern, repl, string, count=0, flags=0):
        1). sub is substitute, will find and replace;

    4. (?:...), non-capturing:
            ?: use the parentheses but don't capture the result;


"""

# extract username from user Twitter profile url: https://twitter.com/tomas_lee_x

import re
url = input("What's your Twitter profile url? ").strip()

# print(f"url is {url}")

# version 1, user str.replace()
# username = url.replace("https://twitter.com/", "")

# version 2, use str.split()
# username = url.split("/")[-1]

# version 3 use re.sub()
# pattern1 = r".*/"
# username = re.sub(pattern1, "", url)

# print(f"username is {username}")

# version 4 use re.search()
pattern = r".*/(.+)"
# [username] = matches.groups()
if matches := re.search(pattern, url, re.IGNORECASE):
    username = matches.group(1)
    print(f"username is {username}")
else:
    print("please input your twitter username")
