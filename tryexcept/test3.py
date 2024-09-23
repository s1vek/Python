import math
from dbm import error

while True:
    try:

        while True:
            try:
                L = float(input("Zadej indukcnost [H]:"))
                break
            except ValueError:
                print(ValueError)

        while True:
            try:
                C = float(input("Zadej kapacitu [F]:"))
                break
            except ValueError:
                print(ValueError)

        F = 1 / (2 * 3.14 * math.sqrt(L * C))
        print(F)
        break

    except ValueError as error:
        print(error)



