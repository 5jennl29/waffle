# Ask user for sequence and marker
print("Please enter a pattern:")
pattern = input()

print("Please enter the character for the first marker:")
marker01 = input()

print("Please enter the character for the second marker:")
marker02 = input()

# Find markers
is_counting = False
count = 0

for character in pattern:
    if (is_counting == False) and (character == marker01):
      print("Found first marker")
      is_counting = True
    elif (is_counting == True) and (character == marker02):
      print("Found last marker")
      is_counting = False
    elif is_counting:
      count += 1

# Display result
print(f"The distance between the markers is {count}")