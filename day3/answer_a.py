
TOTAL = 0

LOOKUP = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def score(shared):
    total = 0
    for elem in shared:
        total = LOOKUP.index(elem) + 1
    return total

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        length_of_input = len(line)
        num_items = int(length_of_input/2)

        compartment_1 = line[0:num_items]
        compartment_2 = line[num_items:]
        shared = [value for value in compartment_1 if value in compartment_2]
        unique_shared = list(dict.fromkeys(shared))
        TOTAL = TOTAL + score(unique_shared)

        print(f'{line} - {compartment_1} - {compartment_2} - {unique_shared}')

print(TOTAL)