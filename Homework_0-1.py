#inputs 

number_1 = int(input("Enter fist number: "))
number_2 = int(input("Enter second number: "))


#debug 
# number_1 = 10
# number_2 = 5

while True: 
    operator = input("Enter math operator, + - * / ")
    if operator == "quit":
        break
    if operator == "+":
        result = number_1 + number_2
        break
    elif operator == "-":
        result = number_1 - number_2
        break
    elif operator == "*":
        result = number_1 * number_2
        break
    elif operator == "/":
        if number_2 != 0:
            result = number_1 / number_2
            break
        else:
            print("Divide by zero -  NO WAY")
            break
    else:
        result = "Use proper math operator"
        break
print(result)
