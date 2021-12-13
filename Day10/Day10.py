# Day10.py - Syntax Scoring

def getScore(c):
    # convert the character into the corresponding score
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137
    
def getClosingChar(c):
    # convert the opening character into the corresponding closing character
    if c == '(':
        return ')'
    elif c == '[':
        return ']'
    elif c == '<':
        return '>'
    elif c == '{':
        return '}'
    
def processLine(line):
    seperator = []
    
    # Go through each character
    for i, c in enumerate(line):
        # opening chunk
        if c == '(' or c == '[' or c == '<' or c == '{':
            seperator.append(getClosingChar(c))
        # closing chunk
        if c == ')' or c == ']' or c == '>' or c == '}':
            # If the closing character is not the one we expected return the score
            if len(seperator) <= 0 or [c] != seperator[-1:]: #seperator[len(seperator)-1]:
                print(f"{line} - Expected {seperator[len(seperator)-1]}, but found {c} instead (scored {getScore(c)})")
                return getScore(c)
            
            # If the closing character matches, remove it from the seperators
            if [c] == seperator[-1:]:
                seperator.pop()
    
    return 0

try:
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    score = 0
    
    # Go through each line in the input file
    for line in lines:
        line = line.strip()
        score += processLine(line)
    
    print(f"Total syntax error score: {score}")
        
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()