count_intersections = 0
count_any_overlap = 0

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        ranges = line.split(',')

        elf1_range = ranges[0].split('-')
        elf2_range = ranges[1].split('-')
        elf1 = set(range(int(elf1_range[0]), int(elf1_range[1]) + 1))
        elf2 = set(range(int(elf2_range[0]), int(elf2_range[1]) + 1))
        
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            count_intersections = count_intersections + 1
            print(f'Yes - {elf1} {elf2}')
        else:
            print(f'No - {elf1} {elf2}')

        if len(elf1.intersection(elf2)) > 0:
            count_any_overlap = count_any_overlap + 1
            
print(count_intersections)
print(count_any_overlap)