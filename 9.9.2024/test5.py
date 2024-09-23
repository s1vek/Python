#Uloha 5

while True:
    try:
        input_day = int(input("Enter a day number: "))
        if 1 <= input_day <= 31:
            break
        else:
            print("Spatne rozmezi")
    except ValueError:
        print("Enter correct date")


while True:
    try:
        input_month = int(input("Enter a month number: "))
        if 1 <= input_month <= 12:
            break
        else:
            print("Spatne rozmezi")
    except ValueError:
        print("Enter correct date")



while True:
    try:
        input_year = int(input("Enter a year number: "))
        if input_year <= 2024:
            break
        else:
            print("Spatne rozmezi")
    except ValueError:
        print("Enter correct date")


print(input_day, input_month, input_year)



