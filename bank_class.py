"""
    1. class:
        1). ❕ notice the keyword is __init__ , not __int__;
        2). instance variables are by definition accessible to all of the methods in that class,
            because the parameter "self" is a inference link to the instance object;
        3). @property(getter) and @attribute_name.setter(setter) allow programer some finer grain can control;
        
"""
class Bank:
    def __init__(self):
        self._balance = 0

    def __str__(self):
        return f"Your account balance is {self._balance}"

    @property # getter
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    lee_account = Bank()
    print(lee_account.balance)
    
    lee_account.deposit(100)
    lee_account.withdraw(50)

    print(lee_account.balance)
    print(lee_account)


if __name__ == "__main__":
    main()