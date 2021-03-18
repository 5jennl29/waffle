def short_pattern():
    pattern = {"sequence": "101", "occurences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    print("Analysing patterns...")
    all_patterns = {"short sequence": short_pattern(), "medium sequence": medium_pattern(), "long sequence": long_pattern()}

    for key, value in all_patterns.items():                             # This 'unpacks' the tuple 'items'
        print(f"{key}: {value}")
    print()


if __name__ == "__main__":
    run()