# Day13.py - Transparent Origami
import numpy as np
import re

# NumPy has some useful methods

# Create a 3x3 array
#a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(a)
#print()

# Get the rows 0 and 1
#print(a[0:2])
#print()

# Get rows 1 and 2
#print(a[1:3])
#print()

#Get the first two columns by transposing, slicing and then transposing back
#print(a.transpose()[0:2].transpose())
#print()

# Flip a matrix on the X axis
#print(np.flipud(a))
#print()

# Flip a matrix on the Y axis
#print(np.fliplr(a))
#print()

def foldPaper(matrix, axis, n):
    if axis == "x":
        print(f"Fold along {axis} at {n}")
        m = matrix
        res = m[0:n] + np.flipud(m[n+1:len(m)])
        return res
    elif axis == "y":
        print(f"Fold along {axis} at {n}")
        m = matrix.transpose()
        res = m[0:n] + np.flipud(m[n+1:len(m)])
        return res.transpose()
        

try:
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    maxX = 0
    maxY = 0
    coords = []
    folds = []
    # Go through each line in the input file
    for line in lines:
        match = re.search("(\d+),(\d+)", line)
        fold = re.search("(fold along )+([yx])=(\d+)", line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            #print(f"x={match.group(1)} y={match.group(2)}")
            maxX = max(maxX, x)
            maxY = max(maxY, y)
            coords.append([x, y])
        elif fold:
            #print(f"Fold along {fold.group(2)} at {fold.group(3)}")
            folds.append([fold.group(2), int(fold.group(3))])
            
    print(f"{maxX} by {maxY} grid")
    print()
    
    # Create the paper
    paper = np.zeros([maxX+1, maxY+1])
    
    # Plot the co-ordinates
    for coord in coords:
        paper[coord[0], coord[1]] = 1
    
    for f in folds:
        paper = foldPaper(paper, f[0], f[1])
        # Only handle the first fold
        break
    
    print()
    print(f"{len(paper[paper > 0])} dots are visible")
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()