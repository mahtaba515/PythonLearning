# 2) Write a program using match case that simulates a simple calculator
#     i) Ask the user for two numbers and an operations (+,-,*,/).
#     ii) Perform the operation using match case.



num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operation = input("Enter operation : ")
match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Invalid operation")