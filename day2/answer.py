
TOTAL_SCORE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

ME = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS
}

OPPONENT = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS
}

WIN = 6
DRAW = 3
LOSS = 0

def _game_points(opponent, me):
    if me == 'X':
        if opponent == 'A':
            return DRAW
        elif opponent == 'B':
            return LOSS
        else:
            return WIN
    elif me == 'Y':
        if opponent == 'A':
            return WIN
        elif opponent == 'B':
            return DRAW
        else:
            return LOSS
    elif me == 'Z':
        if opponent == 'A':
            return LOSS
        elif opponent == 'B':
            return WIN
        else:
            return DRAW

def result(opponent, me) -> int:
    return _game_points(opponent, me) + ME[me]

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        round = line.split(' ')
        TOTAL_SCORE = TOTAL_SCORE + result(round[0], round[1].replace('\n',''))

print(TOTAL_SCORE)
