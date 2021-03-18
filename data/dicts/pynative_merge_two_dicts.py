
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print("\nDictionaries before changes:")
print(dict1)
print(dict2)

# Create new dictionary (dict3) as a copy of dict1
dict3 = dict1.copy()
# Update dict3 with the items from dict2
dict3.update(dict2)
# Print dict3 (the new, combined, dictionary)
print("\nCombined dictionary:")
print(dict3)