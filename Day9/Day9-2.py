# Day9-2.py - Smoke Basin (part 2)

def getPoint(x, y):
    if y >= 0 and y < len(rows):
        if x >= 0 and x < len(rows[y]):
            return rows[y][x]
    return None

def isLowPoint(x, y):
    point = getPoint(x,y)
    
    left = getPoint(x-1,y)
    right = getPoint(x+1,y)
    up = getPoint(x,y-1)
    down = getPoint(x,y+1)
    
    # If left is lower
    if left is not None and left <= point:
        return False
    # If right is lower
    if right is not None and right <= point:
        return False
    # If up is lower
    if up is not None and up <= point:
        return False
    # If down if lower
    if down is not None and down <= point:
        return False
    # Point is a low point
    #print(f"point {x},{y} = {rows[y][x]}  (l={left} r={right} u={up} d={down})")
    return True

def getBasin(points, x,y):
    point = getPoint(x,y)
    
    if point == 9:
        return 0
    
    key = str(x)+","+str(y)
    # Stop if we already checked this point
    if key in points:
        return 0
    
    # Add this point to the basin
    points.append(key)
    
    left = getPoint(x-1,y)
    right = getPoint(x+1,y)
    up = getPoint(x,y-1)
    down = getPoint(x,y+1)
    
    # Check if the adjacent points are in the basin
    if left is not None and left < 9:
        getBasin(points, x-1,y)
    if right is not None and right < 9:
        getBasin(points, x+1,y)
    if up is not None and up < 9:
        getBasin(points, x,y-1)
    if down is not None and down < 9:
        getBasin(points, x,y+1)
        

try:
    fishes = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    rows = []
    # Go through each line in the input file
    for line in lines:
        row = []
        for c in line.strip():
            row.append(int(c))
        rows.append(row)
    
    # Calculate the risk by adding 1 plus the hight of each low point
    risk = 0
    basins = []
    for y, row in enumerate(rows):
        for x, row in enumerate(rows[y]):
            if isLowPoint(x, y):
                risk += 1+rows[y][x]
                
                # calculate the size of the basin
                basin = []
                getBasin(basin, x, y)
                basins.append(len(basin))
                
    print(f"Risk: {risk}")
    
    # Only use the three largest
    basins.sort()
    basins = basins[-3:]
    print(f"Three largest basins: {basins}")
    size = 0
    for basin in basins:
        if size == 0:
            size = basin
        else:
            size = size * basin
    print(f"Multiplied basins: {size}")
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()