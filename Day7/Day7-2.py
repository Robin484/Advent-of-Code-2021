# Day7-2.py - The Treachery of Whales (part 2)

import statistics
import math

# Calculate the fuel consumption, each time a crab moves
# the consumption increases by 1
def fuelConsumption(distance):
    return (distance * (distance + 1)) / 2

def reposition(crabs, position):
    fuel = 0
    # for each crab work out how much fuel it takes to move
    # to the desired position
    for crab in crabs:
        usage = fuelConsumption(abs(crab - position))
        fuel += usage
        
    return fuel
try:
    crabs = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    # Go through each line in the input file
    for line in lines:
        if crabs is None:
            crabs = []
            for crab in line.split(","):
                crabs.append(int(crab.strip()))
                
    print(f"Mode is {statistics.mode(crabs)}")
    print(f"Total fuel used: {reposition(crabs, statistics.mode(crabs))}")
    
    mean = statistics.mean(crabs)
    print(f"Mean is {mean}")
    print(f"Total fuel used: {reposition(crabs, mean)}")
    print(f"Total fuel used for {math.floor(mean)}: {reposition(crabs, math.floor(mean))}")
    print(f"Total fuel used for {math.ceil(mean)}: {reposition(crabs, math.ceil(mean))}")
    
    print(f"Median is {statistics.median(crabs)}")
    print(f"Total fuel used: {reposition(crabs, statistics.median(crabs))}")
    
    bestUsage = None
    position = 0
    for n in range(min(crabs), max(crabs)):
        usage = reposition(crabs, n)
        if bestUsage is None or usage < bestUsage:
            bestUsage = usage
            position = n
    
    print(f"Most efficient position is {position}")
    print(f"Total fuel used: {reposition(crabs, position)}")
        
                           
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()