def observed():
    observations = []                           # Creates empty list

    for _ in range(7):                          # For 7 'passes'
        print("Please enter an observation: ", end="")  # Print message to user
        obs = input()                                   # User input
        observations.append(obs)                        # Add that input to the list 'observations'

    return observations


def run():
    print("Counting observations...")
    observations_list = observed()                      # Creates a list in this function by calling the first function and storing the returned values

    things_observed = set()                             # Empty set created

    for observation in observations_list:                                               # For each observation in the list
        observation_tuple = (observation, observations_list.count(observation))         # Create a tuple with (the observation, and the count of it)
        things_observed.add(observation_tuple)                                          # Add the tuple to the set

    print(things_observed)                                                              # Print the set


if __name__ == "__main__":
    run()
