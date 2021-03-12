
def max_of_three():
    print("Please enter 3 numbers below...")
    one = int(input("Number one: "))
    two = int(input("Number two: "))
    three = int(input("Number three: "))


    if one > two and one > three:
        print(f"{one} is biggest!")
    elif two > one and two > three:
        print(f"{two} is biggest!")
    elif three > two and three > one:
        print(f"{three} is biggest!")
    else:
        print("There has been an error!")


max_of_three()
