#Uloha 3
while True:
    print("Ahoj, jak se jmenuješ?")
    name = input()

    print("Opravdu se jmenuješ:" + name)
    name_check = input()

    if name_check == 'yes':
        print("dik za odpoved")
        break
    else:
        print("Druhy pokus")