# Day1.py - Sonar Sweep

# read through the input file, counting how many times line increases


try:
    file = open ('input.txt', 'r')
    depths = file.readlines()

    increases = 0
    previousDepth = None

    # for each line
    for depth in depths:
        # check if it is deeper than the previous
        if previousDepth != None and int(depth) > previousDepth:
            increases += 1
        previousDepth = int(depth)
    print(f"The depth increases {increases} times")
except Exception as e:
    print("An error occurred working out the depths")
    print(e)
finally:
    file.close()
