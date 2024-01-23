# input
age = input("Введіть ваш вік : ")

# converting to int
age = int(age)

if age < 0:
    print("Dead")

elif age >= 0 and age <= 2:
    print("Baby")

elif age >= 2 and age <= 4:
    print("Kid")

elif age >= 4 and age <= 13:
    print("Child")

elif age >= 13 and age <= 20:
    print("Teenager")

elif age >= 20 and age <= 65:
    print("Grown Up")

elif age >= 65:
    print("Senior")

else:
    print("ІДІ НАХУЙ")