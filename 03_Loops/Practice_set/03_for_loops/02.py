# 2) Print the multiplication table of a number (entered by user).
user = int(input("Enter a number : "))
for i in range (1, 11):
    print(user,"*",i,"=" ,user * i)