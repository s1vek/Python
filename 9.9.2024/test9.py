#Uloha 9

for x in range (3):
    print("Enter code: ")
    user_input = int(input())
    correct_code = 1234

    if user_input == correct_code:
        print("Correct!")
        break
    else:
        print("Wrong!")
        continue


