day = int(input("Enter day number(1-7) : "))

match day:
    case 1:
        print("it's Monday")
    case 2:
        print("it's Tuesday")
    case 3:
        print("it's Wednesday")
    case 4:
        print("it's Thursday")
    case 4:
        print("it's Friday")
    case 5:
        print("it's Saturday")
    case 6:
        print("it's Sunday")

    case _:
        print("please enter a valid day number")


