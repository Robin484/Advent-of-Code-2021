# Day8.py - Seven Segement Search

# Digits have the following segments
#    0 - 6 segments
#    1 - 2 segments
#    2 - 5 segments
#    3 - 5 segments
#    4 - 4 segments
#    5 - 5 segments
#    6 - 6 segments
#    7 - 3 segments
#    8 - 7 segments
#    9 - 6 segments

try:
    fishes = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    counter = 0
    
    # Go through each line in the input file
    for line in lines:
        parts = line.split("|")
        if len(parts) == 2:
            signals = parts[0]
            digits = parts[1].split()
            
            for digit in digits:
                
                # We are looking for certain characters
                # 1 - must have two segments on
                # 4 - must have four segments on
                # 7 - must have three segments on
                # 8 - must have seven segments on
                if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                    counter += 1
    
    print(f"1,4,7 or 8 appear {counter} times")
        
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()