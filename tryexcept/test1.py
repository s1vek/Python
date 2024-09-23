
while True:
    try:
        x = input("Enter number: ")
        y = int(x) + 1
        print(y)
        break
    except ValueError:
        print("Enter only integer")
