print("Please enter a phrase")
phrase = input()

num_char = len(phrase)
num_displayed = 0

while num_displayed < num_char:
    num_displayed += 1
    print("Bop ", end="")