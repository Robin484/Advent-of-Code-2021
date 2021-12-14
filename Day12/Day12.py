# Day12.py - Passage Pathing

def add(a, b):
    # We only want to add paths from start
    if b != "start" and a != "end":
        # Add a path from A to B
        if a not in paths:
            paths[a] = [b]
        elif b not in paths[a]:
            paths[a].append(b)
    
    # Add the return B to A
    if b not in paths or a not in paths[b]:
        add(b,a)
        
def findPaths(path, nextCave):
    # If we have reached the end, return the path
    if nextCave == "end":
        return [path]
    
    # If the next cave is a small a cave we have already visited, this is an invalid path. Stop!
    if nextCave.islower() and nextCave in path:
        return None
    
    # If we can't find the next cave. Stop!
    if nextCave not in paths:
        return None
    
    newPaths = []
    for cave in paths[nextCave]:
        newPath = findPaths(path+[nextCave], cave)
        if newPath is not None:
            newPaths += newPath
            
    return newPaths

try:
    filename = 'input.txt'
    file = open (filename, 'r')
    lines = file.readlines()
    
    paths = {}
    # Go through each line in the input file
    for line in lines:
        parts = line.strip().split("-")
        if len(parts) == 2:
            add(parts[0], parts[1])
    
    # Debug, print out all the possible paths
    #for a in paths:
    #    for i, b in enumerate(paths[a]):
    #        print(f"{a} - {b}")
            
    # Begin at the start
    completedPaths = None
    if paths["start"] is not None:
        completedPaths = findPaths([], "start")
        
    print(f"{filename} contains {len(completedPaths)} possible routes")
    
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()