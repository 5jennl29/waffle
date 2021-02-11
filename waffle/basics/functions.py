# A script to repeat lyrics using a function.
print("")

# This part defines the lyrics.
def print_lyrics():
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")

# This part defines the 'repeat' of the lyrics, i.e. calls it twice.
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()