"""
    1. operator overloading:
        1). docs: https://docs.python.org/3/reference/datamodel.html#special-method-names;
        2). + is addition for number and + is concatenation for str;

    2. object.__add__(self, other):
        1). every object can use __add__ to overload + symbol operator's action;
        2). self is going to be referring to whatever's on the left hand side of a plus sign;
        3). other is going to be referring to whatever's on the right hand side of  a plus sign;
        4). By default, __add__ is not implemented and needs to be defined before calling, otherwise:
            TypeError: unsupported operand type(s) for +: 'Vault' and 'Vault'
        5). ❕ can call Class in itself's method;
"""

class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts "

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts

        return Vault(galleons, sickles, knuts)
    
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts
total = Vault(galleons, sickles, knuts)
print(total)

print(potter + weasley)

