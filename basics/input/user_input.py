print("\nWhat is your name?")
name = input()
print(f"\nHow old are you {name}?")
age = int(input())

year = 2021
years_to_go = 100 - age
cent_age = years_to_go + 2021

print(f"Hi {name}, you will be 100 years old in {cent_age}\n")
print("Please enter a number:")
number = int(input())

print(f"Hi {name}, you will be 100 years old in {cent_age}\n" * number)
