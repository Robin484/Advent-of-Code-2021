# Day5.py - Hydrothermal Venture

import re
import numpy as np

vents = []
try:
    fishes = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    maxX = 0
    maxY = 0
    
    coords = []
    # Go through each line in the input file
    for line in lines:
        # Split the line into an co-ordinates
        match = re.search("(\d+),(\d+)\s*->\s*(\d+),(\d+)", line)
        if match:
            x1 = int(match.group(1))
            y1 = int(match.group(2))
            x2 = int(match.group(3))
            y2 = int(match.group(4))
            
            coords.append([x1,y1,x2,y2])
            
            maxX = max(maxX, x1, x2)
            maxY = max(maxY, y1, y2)
            
    # Create the vents
    vents = np.zeros((maxX+1, maxY+1))
    
    # Go through the co-ordinates, incrememnting where the vents are
    for coord in coords:
        if coord[0] == coord[2]:
            #print(f"Co-ordinates: {coord} horizontal x={coord[0]} y {min(coord[1], coord[3])} to {max(coord[1], coord[3])}")
            for y in range(min(coord[1], coord[3]), max(coord[1], coord[3])+1):
                vents[coord[0]][y] += 1
        elif coord[1] == coord[3]:
            #print(f"Co-ordinates: {coord} vertical y={coord[1]} x {min(coord[0], coord[2])} to {max(coord[0], coord[2])}")
            for x in range(min(coord[0], coord[2]), max(coord[0], coord[2])+1):
                vents[x][coord[1]] += 1
        #else:
            #print(f"Co-ordinates: {coord}")
    
    # Work out how many vent's overlap at least once
    overlaps = 0
    for cols in vents:
        for row in cols:
            if row >= 2:
                overlaps += 1
                
    print(f"Number of overlaps: {overlaps}")
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()