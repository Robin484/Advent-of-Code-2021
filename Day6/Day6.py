# Day6.py - Lanternfish

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
    
try:
    fishes = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    # Go through each line in the input file
    for line in lines:
        if fishes is None:
            fishes = []
            for fish in line.split(","):
                fishes.append(Fish(int(fish.strip())))
                
    #print(f"Initial state: {getAges(fishes)}")
    
    # Go through each day
    days = 256
    for i in range(days):
        if i % 20 == 0:
            print(f"Day {i}")
        children = []
        # Age each fish, is a child is created add it to the list
        for n, fish in enumerate(fishes):
            child = fish.age()
            if child is not None:
                children.append(child)
        fishes.extend(children)
        
        # Just for debugging, create the same output as the instructions
        #print(f"After {i+1} days: {getAges(fishes)}")
    
    # Finally, how many fish are there
    print(f"After {days} there are {len(fishes)} fish")
                           
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()