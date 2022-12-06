import string

TOTAL_PARTA = 0
TOTAL_PARTB = 0

LOOKUP = (string.ascii_lowercase + string.ascii_uppercase)

def score(shared: list) -> int:
    ''' Handle scenario where there is more than 1 shared item'''
    print(shared)
    total = 0
    for elem in shared:
        total = LOOKUP.index(elem) + 1
    return total

line_count = 0
line_buffer = []

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_count += 1
        line_buffer.append(line.replace('\n',''))
        num_items_per_rucksack = int(len(line)/2)

        compartment_1 = line[0:num_items_per_rucksack] # first half
        compartment_2 = line[num_items_per_rucksack:] # second half
        shared = [value for value in compartment_1 if value in compartment_2] # intersection of two lists
        unique_shared = list(dict.fromkeys(shared)) # quick way to remove duplicates
        TOTAL_PARTA = TOTAL_PARTA + score(unique_shared)

        if line_count%3 == 0:
            badge  = [value for value in line_buffer[0] if value in line_buffer[1] if value in line_buffer[2]] # intersection of two lists
            unique_badge = list(dict.fromkeys(badge)) # quick way to remove duplicates
            TOTAL_PARTB = TOTAL_PARTB + score(unique_badge)
            line_buffer = []

print(TOTAL_PARTA)
print(TOTAL_PARTB)