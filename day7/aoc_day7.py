# Advent of Code 2025 - task 1 of day 7

# We go from point 'S' down with a symbol '|' and if we encounter splitter '^', we go by left and right of this splitter
# We want to know how many times the beam splits

# Reading the file
file = open("day7/input7.txt", "r")
lines = file.read().splitlines()

# Assigning input data to a 2D list 
symbols = [list(line) for line in lines]
#print(symbols)

# Solving the main task
total_times = 0

# we go through every row through and then through every column
for i in range(len(symbols)):
    for j in range(len(symbols[i])):
        if symbols[i][j] == 'S':
            symbols[i+1][j] = '|'
        if (j-1>=0 and i+1<len(symbols) and j+1<len(symbols[i]) and symbols[i+1][j] == '^' and symbols[i][j] == '|'):
            #split 
            symbols[i+1][j+1] = '|'
            symbols[i+1][j-1] = '|'
            total_times += 1
        # propagation without splitting
        if (i+1<len(symbols) and symbols[i][j] == '|' and symbols[i+1][j] != '^'):
            symbols[i+1][j] = '|'
   
print("Total times the bean will be split: ", total_times)