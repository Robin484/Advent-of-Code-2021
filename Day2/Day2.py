# Day2.py - Dive!

# Calculate the position of the submarine based on the planned course

import re

horizontal = 0
depth = 0

try:
    file = open ('input.txt', 'r')
    instructions = file.readlines()

    # for each line
    for line in instructions:
        # Split the line into an instruction followed by a unit
        match = re.search("(\w+)\s+(\d)", line)
        if match:
            instruction = match.group(1).lower()
            unit = int(match.group(2))

            # Follow the instruction to work out the new position
            if instruction == "forward":
                horizontal += unit
            elif instruction == "up":
                depth -= unit
            elif instruction == "down":
                depth += unit
            else:
                print(f"Unexpected instruction '{instruction}'");
        
    print(f"The horizontal position is: {horizontal}")
    print(f"The vertical position is: {depth}")
    print(f"Multiplied position: {(horizontal*depth)}")
except Exception as e:
    print("An error occurred working out the position")
    print(e)
finally:
    file.close()
