
rivers = [
    {
        "nazev": "vltava",
        "pramen": "sever",
        "prutok": ["Praha","Plzen","Ceske Budejovice"]
    },

    {
        "nazev": "labe",
        "pramen": "jih",
        "prutok": ["Ostrava","Brno","Pardubice"]

    },

    {
        "nazev": "morava",
        "pramen": "vychod",
        "prutok": ["Jihlava","Trebic","Opava"]
    }

]

user_input = int(input("[1] - Enter city, [2] - Enter river"))

if user_input == 1:
    user_city = input("City: ")
    frivers = []

    for x in rivers:
        if user_city in x["nazev"]:
            frivers.append(x["prutok"])

    if frivers:
        print(frivers)
    else:
        print("not found")

if user_input == 2:
    user_river = input("River: ")
    cities =  []
    streams = []


    for x in rivers:
        if user_river in x["nazev"]:
            cities.append(x["prutok"])
            streams.append(x["pramen"])


    if cities and  streams:
        print(cities, streams)
    else:
        print("not found")