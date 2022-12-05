
TOTAL_SCORE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

ME = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS
}

WIN = 6
DRAW = 3
LOSS = 0

def _game_points(opponent, me):
    if me == 'A':
        if opponent == 'A':
            return DRAW
        elif opponent == 'B':
            return LOSS
        else:
            return WIN
    elif me == 'B':
        if opponent == 'A':
            return WIN
        elif opponent == 'B':
            return DRAW
        else:
            return LOSS
    elif me == 'C':
        if opponent == 'A':
            return LOSS
        elif opponent == 'B':
            return WIN
        else:
            return DRAW

def result(opponent, me) -> int:
    return _game_points(opponent, me) + ME[me]

def _pick_answer(strategy, opponent):
    if strategy == 'X':
        if opponent == 'A':
            return 'C'
        elif opponent == 'B':
            return 'A'
        else:
            return 'B'
    elif strategy == 'Y':
        return opponent
    else:
        if opponent == 'A':
            return 'B'
        elif opponent == 'B':
            return 'C'
        else:
            return 'A'

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    for line in lines:
        round = line.split(' ')
        TOTAL_SCORE = TOTAL_SCORE + result(round[0], _pick_answer(round[1].replace('\n',''), round[0]))

print(TOTAL_SCORE)
