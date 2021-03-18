def observed():
    observations = {"Flying Car", "Sky Scraper", "Sky Scraper", "Laser", "Dome", "Dome"}   # Function adds items to set 'observations'
    return observations


def run():
    observations = observed()      # Calls the function and stores the returned value
    print(observations)             # Prints the set

if __name__ == "__main__":
    run()
