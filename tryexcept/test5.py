

try:
    year = int(input("Enter year:"))
    month = int(input("Enter month:"))
    day = int(input("Enter day:"))

    current_year = 2024
    current_age = current_year - year

    if current_age < 0 or current_age > 112:
        raise Exception("Invalid age")

    if month < 1 or month > 12:
        raise Exception("Invalid month")

    if month == 1 or month == 3 or month == 5 or month == 10 or month == 12:
        if day < 1 or day > 31:
            raise Exception("Invalid day")
    elif month == 2:
        if day < 1 or day > 28:
            raise Exception("Invalid day")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 1 or day > 31:
            raise Exception("Invalid day")

    if month == 7 or month == 8:
        raise Exception("Invalid month")

    print(day, month, year)

except Exception as e:
    print(e)

