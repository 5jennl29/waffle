import random as rand


def dice_roll():
    is_looping = True

    while is_looping:
        print("Would you like to roll the dice? y/n")
        response = input()

        if response == "y":
            roll = rand.randint(1,6)
            print(f"You've rolled a {roll}\n")
        else:
            is_looping = False



dice_roll()