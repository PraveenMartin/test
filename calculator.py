# using the If- Else condition

operator = input("enter the operator (+ - * /): ")
num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))

if operator == "+": #no spaces(" + ")
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
