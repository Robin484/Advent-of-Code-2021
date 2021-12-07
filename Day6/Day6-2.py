# Day6-2.py - Lanternfish (part 2)

# Part 2 process many many more fish. using an array of bytes reduces the memory usage but it is taking a long time. Could we paralize it?!
import array
from multiprocessing import Pool

def getDays():
    return 256

def f(life):
    days = getDays()
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
    return len(fishes)

if __name__ == '__main__':
    try:
        fishes = None
        file = open ('test.txt', 'r')
        lines = file.readlines()
        
        # Go through each line in the input file
        for line in lines:
            if fishes is None:
                fishes = array.array('b')
                for fish in line.split(","):
                    fishes.append(int(fish.strip()))
                    
        print(f"Initial fish count {len(fishes)}")
        
        # Process 10 fish at a time
        fishCount = 0
        total = len(fishes)
        batch = []
        for i, fish in enumerate(fishes):
            fishCount += f(fish)
            print(f"Processed {i}/{total}  =  {fishCount}")
            #batch.append(fish)
            #if i != 0 and i % 5 == 0:
            #    print(f"Processed {i}/{total}  =  {fishCount}")
            #    with Pool(3) as p:
            #        result = p.map(f, batch)
            #    fishCount += sum(result)
            
        
        #with Pool(20) as p:
        #    result = p.map(f, fishes)
        
        print(f"After {getDays()} there are {fishCount} fish")
                               
    except Exception as e:
        print("An error occurred")
        print(e)
    finally:
        file.close()
