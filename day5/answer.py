
with open('example', 'r') as f:
    lines = f.readlines()

grid_definition = []
# load the starting grid
for line in lines:
    if line == '\n':
        break
    grid_definition.append(line)

number_stacks = grid_definition[len(grid_definition) - 1].replace('   ',',')
print(number_stacks)

#execute instructions
