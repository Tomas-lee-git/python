def main():
    input_number()

def input_number():
    while True: # use while to ensure user input number value ultimately
        try: # use try except to catch the valueError
            x = int(input("What's x ? "))
            break # break the loop after x get value normally
        except ValueError:
            print("please input a number")

    print(f"s squared is {square(x)}")

def square(n):
    # return n * n
    return pow(n, 2)

"""
    👇这行代码的意思：只有在直接执行这个文件的时候，main() 才会被调用；
    想要避免的情况是：当本文件被其它文件作为 module/package import时，main() 不会“意外地”被执行；
"""
if __name__ == "__main__": 
    main()