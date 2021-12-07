# Day6.py - Lanternfish

import array

class Fish:
    counter = 0
    def __init__(self, life):
        self.counter = life
    
    def age(self):
        self.counter -= 1
        if self.counter < 0:
            self.counter = 6
            return Fish(8)
        return None
    
def getAges(fishes):
    ages = []
    for fish in fishes:
        ages.append(fish.counter)
    return ages

def fishLifecycle(life, days):
    fishes = array.array('b')
    fishes.append(life)
    # Start with just one fish
    for i in range(days):
        children = []
        for n, fish in enumerate(fishes):
            fishes[n] -= 1
            if fishes[n] < 0:
                fishes[n] = 6
                children.append(8)
        fishes.extend(children)
    return fishes
    
try:
    fishes = None
    file = open ('test.txt', 'r')
    lines = file.readlines()
    
    # Go through each line in the input file
    for line in lines:
        if fishes is None:
            fishes = array.array('b')
            for fish in line.split(","):
                fishes.append(int(fish.strip()))
                
    #print(f"Initial state: {getAges(fishes)}")
                
    # Work out fish population in 8 days
    populations = {}
    
    period = 16
    
    # Go through each day
    print("Working out lifecycles")
    populations[0] = fishLifecycle(0, period)
    populations[1] = fishLifecycle(1, period)
    populations[2] = fishLifecycle(2, period)
    populations[3] = fishLifecycle(3, period)
    populations[4] = fishLifecycle(4, period)
    populations[5] = fishLifecycle(5, period)
    populations[6] = fishLifecycle(6, period)
    populations[7] = fishLifecycle(7, period)
    populations[8] = fishLifecycle(8, period)
    print("Found lifecycles")
    
    days = 256
    for i in range(int(days/period)):
        newfishes = array.array('b')
        # For each fish work out the population after the period of days
        for fish in fishes:
            newfishes.extend(populations[fish])
        fishes = newfishes
        print(f"{i*period}/{days} days")
    
    # Finally, how many fish are there
    print(f"After {days} there are {len(fishes)} fish")
                           
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()