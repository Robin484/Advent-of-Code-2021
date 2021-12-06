# Day3-2.py - Binary Diagnostic (part 2)

# Calculate the gamma and epsilon rate
# The gama rate is the most common bit, the epsilon being the least common bit

def getMostCommonBit(values, bitmask):
    ones = 0
    for value in values:
        if value & bitmask:
            ones += 1
    if ones >= (len(values)/2):
        return True
    return False

bits = None
gamma = 0
epsilon = 0
diagnostics = []
numBits = None

try:
    file = open ('input.txt', 'r')
    lines = file.readlines()

    # Read the file into an array of numbers
    for line in lines:
        if numBits is None:
            numBits=len(line.strip())
        diagnostics.append(int(line, 2))
        
    # Work out the gamma/epsilon but finding the most common bit
    for i in range(numBits-1, -1, -1):
        mostCommonBit = getMostCommonBit(diagnostics, (1 << i))
        gamma = (gamma << 1) | mostCommonBit
        epsilon = (epsilon << 1) | (not mostCommonBit)
        
    print (f"Gamma rate: {gamma}")
    print (f"Epsilon rate: {epsilon}")
    print (f"Power consumption: {(gamma*epsilon)}")
        
    # Work out the oxygen rating
    oxygenRatings = diagnostics
    for bit in range(numBits-1, -1, -1):
        mostCommonBit = getMostCommonBit(oxygenRatings, (1 << bit))
        
        # Remove any entries that don't have the most common bit set
        tempArray = []
        for value in oxygenRatings:
            if (value & (1 << bit)) == (mostCommonBit << bit):
                tempArray.append(value)
        oxygenRatings = tempArray
        
        # Stop if there is only one result
        if len(oxygenRatings) == 1:
            break
        
    # Get the value for the oxygen rating
    if len(oxygenRatings) == 0:
        oxygenRating = 0
    else:
        oxygenRating = oxygenRatings[0]
    print(f"Oxygen Rating: {oxygenRating}")
    
    # Work out the C02 scrubber rating
    co2ratings = diagnostics
    for bit in range(numBits-1, -1, -1):
        leastCommonBit = not getMostCommonBit(co2ratings, (1 << bit))
        
        # Remove any entries that don't have the least common bit set
        tempArray = []
        for value in co2ratings:
            if (value & (1 << bit)) == (leastCommonBit << bit):
                tempArray.append(value)
        co2ratings = tempArray
        
        # Stop if there is only one result
        if len(co2ratings) == 1:
            break
        
    # Get the value for the C02 scrubber rating
    if len(co2ratings) == 0:
        c02rating = 0
    else:
        c02rating = co2ratings[0]
    print(f"C02 Scrubber rating: {c02rating}")
    
    print(f"Life support rating: {(oxygenRating*c02rating)}")
except Exception as e:
    print("An error occurred working out the position")
    print(e)
finally:
    file.close()
    
