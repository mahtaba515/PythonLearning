# 3) Write a program that takes a number from the user and prints "Even" if it is even. otherwise "Odd"

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It's even")
else:
    print("It's odd")