def build_grid(lines):

    grid = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    row = 0
    for line in lines:
        col = 0
        for height in line:
            grid[row][col] = int(height)
            col += 1
        row += 1
    return grid


def visibile_left(grid, row, col):
    current_height = grid[row][col]
    for i in range(col-1, -1, -1):
        if current_height <= grid[row][i]:
            return False
    return True


def visible_right(grid, row, col):
    current_height = grid[row][col]
    for i in range(col+1, len(grid[row]), 1):
        if current_height <= grid[row][i]:
            return False
    return True


def visible_bottom(grid, row, col):
    current_height = grid[row][col]
    for i in range(row+1, len(grid), 1):
        if current_height <= grid[i][col]:
            return False
    return True


def visible_top(grid, row, col):
    current_height = grid[row][col]
    for i in range(row-1, -1, -1):
        if current_height <= grid[i][col]:
            return False
    return True


def count_visible(grid):
    num_visibile = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                # shortcut the check for edge trees
                num_visibile += 1
            else:
                if visibile_left(grid, i, j) or visible_right(grid, i, j) or visible_top(grid, i, j) or visible_bottom(grid, i, j):
                    num_visibile += 1

    return num_visibile


def scenic_scores(grid) ->list:
    scores = []
    

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            current_height = grid[row][col]
            left = 0
            right = 0
            top = 0
            bottom = 0

            for i in range(col-1, -1, -1):
                x = grid[row][i]
                if current_height > x:
                    left += 1
                else:
                    left += 1
                    break

            for i in range(col+1, len(grid[row]), 1):
                x = grid[row][i]
                if current_height > x:
                    right += 1
                else:
                    right += 1
                    break

            for i in range(row+1, len(grid), 1):
                x = grid[i][col]
                if current_height > x:
                    bottom += 1
                else:
                    bottom += 1
                    break
                    
            for i in range(row-1, -1, -1):
                x = grid[i][col]
                if current_height > x:
                    top += 1
                else:
                    top += 1
                    break

            score = (left * right * top * bottom)
            scores.append(score)
            
    return scores


with open('/workspaces/adventofcode2022/day8/input', 'r') as f:
    lines = f.read().splitlines()

grid = build_grid(lines)
print(count_visible(grid))
scores = scenic_scores(grid)
scores.sort(reverse=True)
print(scores[0])