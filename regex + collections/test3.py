rivers = [
    {
        "name": "Vltava",
        "source": "Černá hora",
        "join": "Labe",
        "continues": True
    },
    {
        "name": "Labe",
        "source": "Krkonošsko",
        "join": "Morava",
        "continues": "Dyje"
    },
    {
        "name": "Morava",
        "source": "Králíky",
        "join": "Dyje",
        "continues": True
    },
    {
        "name": "Dyje",
        "source": "Novohradsko",
        "join": "Morava",
        "continues": "More"
    },
    {
        "name": "Sázava",
        "source": "Sázavské hory",
        "join": "Vltava",
        "continues": True
    },
    {
        "name": "Ohře",
        "source": "Klínovec",
        "join": "Labe",
        "continues": True
    },
]
#
#user_river = str(input("Enter river: "))
#frivers = []
#fcontinues = []

#for x in rivers:
#   if user_river == x["name"]:
#       frivers.append(x["join"])
#       fcontinues.append(x["continues"])

#print(frivers, fcontinues)
#

start = input()
end = input()

way = []

for point in rivers:
    if start == point["name"]:
        way.append(point["join"])
    elif end == point["name"]:
        way.append(point["continues"])

print(way)




