def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def run():
    sequence_dict = pattern()
    print(sequence_dict)


if __name__ == "__main__":
    run()