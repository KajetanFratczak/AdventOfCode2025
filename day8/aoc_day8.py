# Advent of Code 2025 - task 1 of day 8

# Reading the file
file = open("day8/input8.txt", "r")
lines = file.read().splitlines()

# Assigning input data to a 2D list 
symbols = [list(line) for line in lines]
print(symbols)

# Solving the main task
total_times = 0