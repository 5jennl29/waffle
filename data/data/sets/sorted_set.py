def observed():
    observations = []                           # Empty list of observations

    for _ in range(5):                                      # For 5 'passes'
        print("Please enter an observation: ", end="")
        obs = input()                                       # Variable 'obs'
        observations.append(obs)                            # Add 'obs' to the list 'observations'

    return observations                                     # Return observations


def remove_observations(observations):

    is_looping = True                                       # Loop variable

    while is_looping:                                               # While loop (we don't know how many iterations
        print("Do you wish to remove observations? y/n")
        response = input()                                          # Variable stores user response
        if response.lower() == "y":                                 # converts response to lowercase
            print("Please enter the observation to be removed")
            obs_rem = input()                                       # Variable stores user response (obs to be removed)
            observations.remove(obs_rem)                            # Removes it from the list 'observations'
        else:
            is_looping = False                                      # Ends the loop



def run():
    observations = observed()                                                   # Calls the function 'observed' and stores return value (list)
    remove_observations(observations)                                           # Calls the second function

    observations_set = set()                                                       # Creates empty set

    for observation in observations:                                               # For each observation in the list
        observation_tuple = (observation, observations.count(observation))         # Create a tuple with (the observation, and the count of it)
        observations_set.add(observation_tuple)

    print(sorted(observations_set))



if __name__ == "__main__":
    run()
