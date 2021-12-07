# Day4.py - Giant Squid

class BingoCard:
    numbers = []
    def __init__(self, numbers):
        # Validation to make sure it is a 5x5 grid
        if len(numbers) != 5:
            raise Exception(f"Unexpected input: {len(numbers)} rows found, expected 5")
        for row in numbers:
            if len(row) != 5:
                raise Exception(f"Unexpected input: {len(row)} columns found, expected 5")
        self.numbers = numbers
        
    def check(self, draws):
        score = 0
        cols = [0,0,0,0,0]
        rows = [0,0,0,0,0]
        
        for i, ball in enumerate(draws):
            for col in range(5):
                for row in range(5):
                    if self.numbers[col][row] == ball:
                        cols[col] += 1
                        rows[row] += 1
                        
                        self.numbers[col][row] = None
                        
                        # The board wins when 5 numbers are found in either a
                        # column or row
                        if cols[col] >= 5 or rows[row] >= 5:
                            score = 0
                            # Work out the score by counting up the remaining numbers
                            for c in self.numbers:
                                for r in c:
                                    if r is not None:
                                        score += r;
                            return Result(i+1, score*ball)
        return None
        
class Result:
    draws = 0
    score = 0
    def __init__(self, draws, score):
        self.draws = draws
        self.score = score

try:
    draws = None
    cards = []
    card = []
    file = open ('input.txt', 'r')
    lines = file.readlines()
    
    # Go through each line in the input file
    for line in lines:
        # First line should be the numbers drawn
        if draws is None:
            draws = []
            for draw in line.split(","):
                draws.append(int(draw.strip()))
            continue
    
        # If a blank line is found, create a new bingo card
        if len(line.split()) == 0:
            if len(card) > 0:
                cards.append(BingoCard(card))
            card = []
            continue
        
        # Parse the line as a new row of the card
        row = []
        for number in line.split():
            row.append(int(number))
        card.append(row)
        
    # Add the final card
    if len(card) > 0:
        cards.append(BingoCard(card))
        
    draw = None
    score = 0
    for i, card in enumerate(cards):
        result = card.check(draws)
        if result is not None:
            print(f"{i} draw:{result.draws} draw:{result.score}")
            if draw is None or result.draws < draw:
                draw = result.draws
                score = result.score
                
    print(f"Final score is {score}")
        
                           
except Exception as e:
    print("An error occurred")
    print(e)
finally:
    file.close()