with open('input', 'r') as f:
    lines = f.readlines()

MAGIC_NUMBER = 14

line = lines[0]
for i in range(MAGIC_NUMBER, len(line) - 1):
    window = line[i-MAGIC_NUMBER:i]
    unique_letters = list(dict.fromkeys(window))
    print(unique_letters)
    if len(unique_letters) == MAGIC_NUMBER:
        print(i)
        break