elves = []

with open('input', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    elf = 0

    running_total = 0
    for line in lines:
        if line == '\n':
            elves.append(running_total)
            elf = elf + 1
            running_total = 0
        else:
            running_total = running_total + int(line)

elves.sort(reverse=True)
print(elves[0])
print(elves[0] + elves[1] + elves[2])
