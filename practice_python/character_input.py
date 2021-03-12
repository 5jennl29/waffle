
def age_100():
    name = ""
    age = current_year = year_born = 0

    print("Please enter your name:")
    name = input()

    print("Please enter your age:")
    age = int(input())

    print("What is the current year? (i.e. what year are we in now?)")
    current_year = int(input())

    year_born = current_year - age
    year_100 = year_born + 100

    print(f"Hello {name}. You were born in {year_born} and will be 100 years old in {year_100}.")


age_100()