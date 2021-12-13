# Day9.py - Smoke Basin

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
    for y, row in enumerate(rows):
        for x, row in enumerate(rows[y]):
            if isLowPoint(x, y):
                risk += 1+rows[y][x]
                
    print(f"Risk is {risk}")
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()