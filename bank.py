"""
    1. global variables:
        1). global variables: variables defined outside any function;
            i.  ✅ global variables can be read(access) it and print it;
            ii. ❌ global variables can't be write(assign new value), otherwise:
                UnboundLocalError: 
                    cannot access local variable 'balance' where it is not associated with a value
            iii. ❕ if you want to change global variables, you need to tell python using the keyword global, for example:
                global balance
                balance += n
        2). local variables: exists in the context of a function;
            i.  ✅ local variables can only be read(access) and written(change) within the function in which they are defined;
            ii. ❌ if read(access) or write(change) local variables outside of the function in which they are defined:
                UnboundLocalError:
                    cannot access local variable 'balance' where it is not associated with a value
        3). don't define variables with the same name in locally and globally;
        4). if you pass in a variable to each of functions and then change it within that function:
            i. it's only going to be changing in effect a local copy;
            ii. it's not going to be changing what's outside of those functions;

    2. if global is not a variable but a dict:
        1). when you pass it in function, pass a reference with this dict, so we can change it's value;

    3. class:

"""

balance = 0
balance_new = {
    "value": 0
}

def main():
    print(f"balance is {balance}")
    print(f"balance_new is {balance_new["value"]}")
    deposit(100)
    withdraw(50)
    print(f"balance is {balance}")
    print(f"balance_new is {balance_new["value"]}")

def deposit(n):
    global balance
    balance += n

    balance_new["value"] += n


def withdraw(n):
    global balance
    balance -= n

    balance_new["value"] += n

if __name__ == "__main__":
    main()
