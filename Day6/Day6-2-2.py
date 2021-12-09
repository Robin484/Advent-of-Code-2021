# Day6.py - Lanternfish

import array
from datetime import datetime

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

def timestamp():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

try:
    fishes = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    # Go through each line in the input file
    for line in lines:
        if fishes is None:
            fishes = array.array('b')
            for fish in line.split(","):
                fishes.append(int(fish.strip()))
    
    # Work out fish population growth in set period of days
    period = 64
    populations = {}
    
    # Go through each starting fish state working out the lifecycles
    timestamp()
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
    timestamp()
    
    counters = {}
    
    days = 256
    for i in range(min(fishes), max(fishes)+1):
        tmpfishes = array.array('b')
        tmpfishes.append(i)
        timestamp()
        print(f"Working out population for starting fish {i}")
        for j in range(int(days/period)):
            newfishes = array.array('b')
            # For each fish work out the population after the period of days
            for fish in tmpfishes:
                newfishes.extend(populations[fish])
            tmpfishes = newfishes
            print(f"{j*period}/{days} days")
        print(f"Fish {i} population {len(tmpfishes)}")
        print()
        counters[i] = len(tmpfishes)
    timestamp()
    
    # Hardcoded values to save time processing 256 days all over again
    #counters[1] = 6206821033
    #counters[2] = 5617089148
    #counters[3] = 5217223242
    #counters[4] = 4726100874
    #counters[5] = 4368232009
    
    total = 0
    for fish in fishes:
        total += counters[fish]
    
    # Finally, how many fish are there
    print(f"After {days} there are {total} fish")
                           
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()