print()
print("What word do you see?") # Ask user for input (word)
word = input()

print()
print("Reversing...")
print("The phrase is: ", end="")

for position in range(len(word) -1, -1, -1): #Finds the position of each character in the phrase, back one step at a time
    print(word[position], end="")