TOTAL = 0

LOOKUP = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def score(shared: list) -> int:
    ''' Handle scenario where there is more than 1 shared item'''
    total = 0
    for elem in shared:
        total = LOOKUP.index(elem) + 1
    return total

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        num_items_per_rucksack = int(len(line)/2)

        compartment_1 = line[0:num_items_per_rucksack] # first half
        compartment_2 = line[num_items_per_rucksack:] # second half
        shared = [value for value in compartment_1 if value in compartment_2] # intersection of two lists
        unique_shared = list(dict.fromkeys(shared)) # quick way to remove duplicates
        TOTAL = TOTAL + score(unique_shared)

print(TOTAL)