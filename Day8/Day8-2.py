# Day8-2.py - Seven Segement Search

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

def countMatching(string, match):
    return sum(d in string for d in sorted(match))

def contains(string, match):
    return countMatching(string, match) == len(match)

class Segment:
    digits = {}
    def __init__(self, signals):
        # Work through the signals to extract the digit
        
        # Work out 1,4,7,8 first
        for signal in signals:
            s = "".join(sorted(signal))
            
            if len(signal) == 2:
                self.digits[1] = s
            elif len(signal) == 4:
                self.digits[4] = s
            elif len(signal) == 3:
                self.digits[7] = s
            elif len(signal) == 7:
                self.digits[8] = s
        
        # Work out 0,6,9
        for signal in signals:
            s = "".join(sorted(signal))
            
            if len(signal) == 6:
                # nine must contain 4
                if contains(s, self.digits[4]):
                    self.digits[9] = s
                # zero must contain 1 but not 4
                elif contains(s, self.digits[1]) and not contains(s, self.digits[4]):
                    self.digits[0] = s
                # otherwise it's a six
                elif not contains(s, self.digits[1]) and not contains(s, self.digits[4]):
                    self.digits[6] = s
                else:
                    raise ValueError("Unexpected 6 segment digit: "+signal)
                    
        # Work out 2,3,5
        for signal in signals:
            s = "".join(sorted(signal))
            
            if len(signal) == 5:
                # three must contain 7
                if contains(s, self.digits[7]):
                    self.digits[3] = s
                # two must match four of the segments found in 6
                elif countMatching(s, self.digits[6]) == 4:
                    self.digits[2] = s
                # five must match 5 of the segments found in 6
                elif countMatching(s, self.digits[6]) == 5:
                    self.digits[5] = s
                else:
                    raise ValueError("Unexpected 5 segment digit: "+signal)
        
        # Throw if all 10 digits weren't found
        if len(self.digits) != 10:
            raise ValueError("Only found "+len(self.digits)+" digits")
        
    # Decode a signal into a digit
    def decode(self, string):
        s = "".join(sorted(string))
        
        # Go through the digits and find a match
        for i in self.digits:
            if self.digits[i] == s:
                return i
        return None
    
    
try:
    fishes = None
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    counter = 0
    
    # Go through each line in the input file
    for line in lines:
        parts = line.split("|")
        if len(parts) == 2:
            signals = parts[0].split()
            outputs = parts[1].split()
            
            # Create a segment object
            segment = Segment(signals)
            
            value = ""
            for output in outputs:
                # Decode each output
                value += str(segment.decode(output))
                
            #print(f"{signals} : {value}")
            counter += int(value)
    
    print(f"Output values add up to: {counter}")
    
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()