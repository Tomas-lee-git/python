# exceptions: 例外情况，也就是 bug

"""    
    SyntaxError: unterminated string literal (detected at line 6)
                未终止的字符串，也就是字符串没有的""没有正确的闭合

    SyntaxError must be fixed

    print(hello")

"""



""" 
    ValueError: invalid literal for int() with base 10: 'cat'

    defensively，设置防御性的代码来避免

   
"""
x = int(input("What's x ? "))
print(f"x is {x}")

print("continue")
