print("How many bars should be charged?")
bars = int(input())
bars_charged = 0

while bars_charged < bars:
    bars_charged += 1
    print(f"Charging: ", end ="")
    print("|" * bars_charged)

print("\nThe battery is fully charged")