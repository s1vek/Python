import math
from sys import excepthook

try:
    r = float(input("Enter radius "))
    if r <= 0:
        raise ArithmeticError("Enter number higher than 0")
    else:
        print("Valid")
    s = math.pi * (r * r)
    print(s)
except ValueError as error:
    print(error)