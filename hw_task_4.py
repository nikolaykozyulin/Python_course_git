#Function that return symbol

def hundredVerge(number):
    if number > 100:
        print(" + ")
    elif number < 100:
        print(" - ")
    else:
        print("Number = 100")
    print("End")

print("Please, Enter the number")
number = int(input())
hundredVerge(number)