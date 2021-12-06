# Day1-2.py

# read through the input file, working out a sliding window and
# counting how many times the window increases

windowSize = 3

try:
    file = open ('input.txt', 'r')
    depths = file.readlines()

    increases = 0
    window = []
    previousSum = None

    # for each line
    for depth in depths:
        window.append(int(depth))

        # if we have more than three entries remove the oldest
        if len(window) > windowSize:
            window.pop(0)

        # When we have enough depths for the window, work out the sum for
        # the sliding window
        if len(window) >= windowSize:
            currentSum = sum(window)
            # check if it is deeper than the previous
            if previousSum != None and currentSum > previousSum:
                increases += 1
            previousSum = currentSum
    print(f"The depth increases {increases} times")
except Exception as e:
    print("An error occurred working out the depths")
    print(e)
finally:
    file.close()
