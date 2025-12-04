# Advent of Code 2025 - task 1 of day 4

# @ - rolls of paper
# forklift can access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions
# we have to figure out which rolls we can access
# we go through all of the input symbol by getting 8 adjacent symbols and mark paper rolls to access
# In other words: we check 8 symbols around every symbol !

# Reading the file to a 2d list
file = open("day4/input4.txt", "r")
lines = file.read().splitlines() 

rows = len(lines)
cols = len(lines[0])

row = -1
col = -1
grid = [[0 for _ in range(cols)] for _ in range(rows)]

for line in lines:
    row += 1
    for i in range(len(line)):
        col = i
        grid[row][col] = line[i]
    col = 0

# could have done this by appending lines to an array 

# Solving the main task
result = 0
for row in range(rows):
    for col in range(cols):
        # we want to check every symbol '@' and then all 8 symbols around it

        if grid[row][col] == '@':
            paper_rolls = 0
            # up-left
            if 0 <= row-1 < rows and 0 <= col-1 < cols and grid[row-1][col-1] == '@':
                paper_rolls += 1

            # up
            if 0 <= row-1 < rows and 0 <= col < cols and grid[row-1][col] == '@':
                paper_rolls += 1

            # up-right
            if 0 <= row-1 < rows and 0 <= col+1 < cols and grid[row-1][col+1] == '@':
                paper_rolls += 1

            # left
            if 0 <= row < rows and 0 <= col-1 < cols and grid[row][col-1] == '@':
                paper_rolls += 1

            # right
            if 0 <= row < rows and 0 <= col+1 < cols and grid[row][col+1] == '@':
                paper_rolls += 1

            # down
            if 0 <= row+1 < rows and 0 <= col < cols and grid[row+1][col] == '@':
                paper_rolls += 1

            # down-right
            if 0 <= row+1 < rows and 0 <= col+1 < cols and grid[row+1][col+1] == '@':
                paper_rolls += 1

            # down-left
            if 0 <= row+1 < rows and 0 <= col-1 < cols and grid[row+1][col-1] == '@':
                paper_rolls += 1

            if (paper_rolls < 4):
                result += 1
print("Result: ", result)