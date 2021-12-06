# Day3.py - Binary Diagnostic

# Calculate the gamma and epsilon rate
# The gama rate is the most common bit, the epsilon being the least common bit

bits = None
gamma = 0
epsilon = 0

try:
    file = open ('input.txt', 'r')
    lines = file.readlines()

    # for each line count the occurences of 1 and 0
    for line in lines:
        if bits is None:
            bits = []
            for i in enumerate(line.strip()):
                bits.append([0,0])
        
        for i, bit in enumerate(line):
            if bit == "1":
                bits[i][1] += 1
            elif bit == "0":
                bits[i][0] += 1

    # calculate the gamma rate, each bit is 1 if there were more 1s than 0s
    # calculate the epsilon rate, each bit is 1 if there were more 0s than 1s
    for bit in bits:
        gamma = (gamma << 1) | ((bit[1] > bit[0]))
        epsilon = (epsilon << 1) | ((bit[1] < bit[0]))

    print (f"Gamma rate: {gamma}")
    print (f"Epsilon rate: {epsilon}")
    print (f"Power consumption: {(gamma*epsilon)}")
except Exception as e:
    print("An error occurred working out the position")
    print(e)
finally:
    file.close()
