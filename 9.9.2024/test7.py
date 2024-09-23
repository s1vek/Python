#Uloha 7

while True:
    try:
        print("Zadejte nenuloveho kladneho mocnitele")
        power_input = int(input())
        if 1 <= power_input:
            break
        else:
            print("Cislo neni validni")
    except ValueError:
        print("Prosim zadejte spravne cislo")


while True:
    try:
        print("Zadejte zaklad mocniny")
        base_input = int(input())
        if 0 < base_input:
            break
        else:
            print("Cislo neni validni")
    except ValueError:
        print ("Prosim zadejte spravne cislo")


result = pow(base_input, power_input)
print(result)