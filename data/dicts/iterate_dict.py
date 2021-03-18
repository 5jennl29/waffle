def pattern():
    data = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    print()
    return data


def display_keys(data):
    print("The keys are:")
    for key in data.keys():
        print(key)
    print()



def display_values(data):
    print("The values are:")
    for values in data.values():
        print(values)
    print()


def display_items(data):
    print("The key-value pairs are:")
    for key, value in data.items():
        print(f"{key} : {value}")
    print()



def run():
    data = pattern()
    print(f"Dictionary: {data}")
    display_keys(data)
    display_values(data)
    display_items(data)


if __name__ == "__main__":
    run()