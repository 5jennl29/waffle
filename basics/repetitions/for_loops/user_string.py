print("Please enter a word")
user_word = input()

for position in range(0, len(user_word), 1):
    print(f"{user_word[position]} is in index position {position}")