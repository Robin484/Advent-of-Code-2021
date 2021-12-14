# Day11.py - Dumbo Octopus

class Octopus:
    energy = 0
    flashed = False
    
    def __init__(self, start):
        self.energy = start
        
    def increment(self):
        if self.flashed == False:
            self.energy += 1
            if self.energy > 9:
                self.flashed = True
                self.energy = 0
    
    def reset(self):
        self.flashed = False
        
        

def getOctopus(x, y):
    if y >= 0 and y < len(rows):
        if x >= 0 and x < len(rows[y]):
            return rows[y][x]
    return None

def increase(x, y):
    flashes = 0
        
    octopus = getOctopus(x, y)
    if octopus is not None:
        flashed = octopus.flashed
        octopus.increment()
        
        # If the octopus flashed, increment all it's neighbours
        if octopus.flashed != flashed:
            flashes += 1
            flashes += increase(x-1, y-1)
            flashes += increase(x,   y-1)
            flashes += increase(x+1, y-1)

            flashes += increase(x-1, y)
            flashes += increase(x+1, y)

            flashes += increase(x-1, y+1)
            flashes += increase(x,   y+1)
            flashes += increase(x+1, y+1)
            
    return flashes

try:
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    rows = []
    # Go through each line in the input file
    for line in lines:
        row = []
        for c in line.strip():
            row.append(Octopus(int(c)))
        rows.append(row)
        
    totalflashes = 0
    
    # Go through a set number of steps
    steps = 100
    for step in range(steps):
        # Go through each octopus and increment it's energy
        for y, row in enumerate(rows):
            for x, row in enumerate(rows[y]):
                totalflashes += increase(x, y)
        
        # Reset all the flashes
        for y, row in enumerate(rows):
            for x, row in enumerate(rows[y]):
                octopus = rows[y][x]
                octopus.reset()
    
    print(f"{totalflashes} total flashes after {steps} steps")
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()