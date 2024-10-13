
dict = {"Plzen":"Plzensky kraj", "Domazlice": "Plzensky kraj", "Tachov": "Plzensky kraj", "praha": "Hlavni mesto", "Liberec": "Liberecky kraj"}


user_input = int(input("[0] - exit, [1] - search by city, [2] - search by region"))

if user_input == 1:
    user_city = str(input("Enter city: "))
    if user_city in dict:
        print(dict[user_city])
    else:
        print("city not found")

elif user_input == 2:
    user_region = str(input("Enter region: "))
    list = []

    for city, x in dict.items():
        if x == user_region:
            list.append(city)

    if list:
        print(list)
    else:
        print("region not found")