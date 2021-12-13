# Day10-2.py - Syntax Scoring (part 2)
import math

def getCompletionScore(chars):
    # Get the completion score, preceeding score is multiplied and then the next score added
    score = 0
    for c in chars:
        score *= 5
        if c == ')':
            score += 1
        elif c == ']':
            score += 2
        elif c == '}':
            score += 3
        elif c == '>':
            score += 4
    return score

def getCorruptionScore(c):
    # convert the character into the corresponding score for a corrupt character
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
                #print(f"{line} - Expected {seperator[len(seperator)-1]}, but found {c} instead (scored {getScore(c)})")
                return getCorruptionScore(c)
            
            # If the closing character matches, remove it from the seperators
            if [c] == seperator[-1:]:
                seperator.pop()
    
    if len(seperator) > 0:
        #print(f"{''.join(reversed(seperator))} - {getCompletionScore(reversed(seperator))} total points.")
        scores.append(getCompletionScore(reversed(seperator)))
        return 0
    
    return 0

try:
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    scores = []
    total = 0
    
    # Go through each line in the input file
    for line in lines:
        line = line.strip()
        total += processLine(line)
    
    print(f"Total syntax error score: {total}")
    print(f"Middle score: {sorted(scores)[math.floor(len(scores)/2)]}")
        
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()
