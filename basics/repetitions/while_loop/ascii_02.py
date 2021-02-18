print("How many bars should be charged?")
bars = int(input())
bars_charged = 0

print()
while bars_charged < bars:
    bars_charged += 1
    print("Charging: ", end ="")
    print(f"█ " * bars_charged)

print("\nThe battery is fully charged")