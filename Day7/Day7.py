# Day7.py - The Treachery of Whales

import statistics

def reposition(crabs, position):
    fuel = 0
    # for each crab work out how much fuel it takes to move
    # to the desired position
    for crab in crabs:
        usage = abs(crab - position)
        fuel += usage
        #print(f"Move from {crab} to {position}: {usage} fuel")
        
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
    
    print(f"Mean is {statistics.mean(crabs)}")
    print(f"Total fuel used: {reposition(crabs, statistics.mean(crabs))}")
    
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