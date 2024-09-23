#Uloha 4
is_rainy = True
is_windy = True
is_foggy = True

if not is_rainy and not is_windy and not is_foggy:
    print("weather is good, just go outside")
elif is_rainy or is_windy and not is_windy:
    print("umbrella is recommended")
elif is_windy and not is_rainy:
    print("cap is recommended")
elif is_foggy and is_rainy and is_windy:
    print("just dont go outside")