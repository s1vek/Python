
try:
    index1= str(input("Enter a index (U,I,R)"))
    value1 = int(input("Enter a value: "))

    index2= str(input("Enter a index (U,I,R "))
    value2 = int(input("Enter another value: "))

    if index1 == index2:
        print("Enter 2 different values")

    if index1 == "U" and index2 == "R":
        I = value1 / value2
        print(I)

    elif index1 =="I" and index2 == "R":
        raise NotImplemented("not defined yet")
    elif index1 == "I" and index2 == "U":
        raise NotImplemented("not defined yet")
    elif index1 == "R" and index2 == "U":
        raise NotImplemented("not defined yet")
    elif index1 == "R" and index2 == "I":
        raise NotImplemented("not defined yet")

    else:
        raise ValueError("Invalid input")

except ValueError as ex:
    print(ex)
except NotImplemented as e:
    print(e)