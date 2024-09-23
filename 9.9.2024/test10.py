#Uloha 10

print("Enter height: ")
user_height = int(input())
print("Enter weight: ")
user_weight = int(input())

bmi_result = user_weight / (user_height * user_height)

if bmi_result < 18.5:
    print("Underweight")
elif bmi_result > 18.5 and bmi_result < 25:
    print("Normal")
elif bmi_result > 25 and bmi_result < 29.9:
    print("Overweight")
else:
    print("Obese")