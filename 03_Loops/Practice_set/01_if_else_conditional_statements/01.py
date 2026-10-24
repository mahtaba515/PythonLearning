# 1) Write a program that asks the user for a number and prints whether it is positive, negative or zero

user = int(input("Enter a number: "))
if 0 < user:
     print("It's a Positive Number")
elif 0 == user:
     print("It's a zero")
else:
    print("It's a Negative Number")