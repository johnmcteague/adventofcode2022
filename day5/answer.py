import re

CARGO_REGEX = '[{A-Z}]'

class Move:
    def __init__(self, source, target, count, model=9000):
        self.source = source
        self.target = target
        self.count = count
        self.model = model


    def apply(self, crates):
        #self.debug_creates(crates)

        if self.model == 9000:
            for i in range (0, self.count):
                to_move = crates[self.source-1].pop()
                crates[self.target-1].append(to_move)
        elif self.model == 9001:
            to_move = []
            for i in range (0, self.count):
                to_move.append(crates[self.source-1].pop())
            to_move.reverse()
            crates[self.target-1].extend(to_move)
        else:
            raise ValueError("Invalid model")

    def debug_creates(self, crates):
        for stack in crates:
            print(stack, end=',')
        print('')

def load_data(file='input'):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines

def load_crates(data):
    crates = []
    num_crates = int((len(data[0]))/4)
    for i in range(0, num_crates):
        crates.append([])

    for line in data:
        matches = re.finditer(CARGO_REGEX, line)
        for m in matches:
            #print(m.start(), m.end(), m.group(0), m )
            bin = int(m.start()/4)
            crates[bin].insert(0,m.group())
        if line == '\n':
            break
    return crates

def process_moves(crates, data, model):
    for line in data:
        if line.startswith('move'):
            move = line.split(' ') # should probably be able to regex this
            Move(int(move[3]), int(move[5]), int(move[1]), model).apply(crates) 

data = load_data()
crates = load_crates(data)
process_moves(crates, data, 9001)
for stack in crates:
    print(stack[len(stack) - 1], end='')
