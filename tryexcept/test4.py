import math
import cmath


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

try:
    d = (b * b) - 4 * (a * c)
    root= (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
except ValueError:
    print("Error")
    root = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b + cmath.sqrt(d)) / (2 * a)
else:
    print("Roots: ")
finally:
    print(root)
    print(root2)



