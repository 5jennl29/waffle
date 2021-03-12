print()
print("How many live cables must I avoid?")
cables_to_avoid = int(input())
live_cables = 0

while cables_to_avoid > live_cables:
    print("Avoiding...", end="")
    live_cables += 1
    print(f"...Done! {live_cables} avoided!")

print("\nAll live cables have been avoided.")