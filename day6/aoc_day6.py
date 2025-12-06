# Advent of Code 2025 - task 1 of day 6

# we have columns of numbers with + or * at the end - we have to add ot multiply these numbers to get results 
# we want to get the total
# problems are separated by a full column of only spaces

# Reading the file
file = open("day6/input6.txt", "r")
lines = file.read().splitlines()

# this equals our first line of numbers 
# print(lines[0])

# i will get a number of columns from this row and then go through every row, assigning numbers to the proper columns
number_of_columns = len(lines[0].split()) # automatically ignores whitespaces
# print(number_of_columns)

numbers = [[] for _ in range(number_of_columns)]

for line in lines:
    row = line.split()
    for i in range(number_of_columns):
        numbers[i].append(row[i])

# last "number" in each column is a math symbol '+' or '*'
#print(numbers)

# Solving the main task
grand_total = 0

for column in numbers:
    total = 0
    math_symbol = column[len(column)-1]
    if (math_symbol == '+'):
        total = 0
    else: 
        total = 1

    for i in range(len(column)):
        if (column[i] != '*' and column[i] != '+'):
            if (math_symbol == '+'):
                total += int(column[i])
            else:
                total *= int(column[i])
    grand_total += total
print("Grand total: ", grand_total)

# --------------------------------------------------------
# Advent of Code 2025 - task 2 of day 6

# numbers are made by going by columns from right to left

# i will get numbers b going through every column from right to left
number_of_columns = max(len(line) for line in lines) # now i don't want to ignore whitespaces
number_of_rows = len(lines)
grand_total = 1
pom = 1

# print (number_of_rows, number_of_columns) -i have every column and every row counted (even columns with whitespaces)

# now i wanna go through every column from right to left 
for i in range(number_of_columns-1, -1, -1):
    curr_column_chars = []
    numbers_in_column = []
    new_number_str = ""

    for j in range(number_of_rows):
        curr_row = lines[j]

        ch = curr_row[i] if i < len(curr_row) else ''
        curr_column_chars.append(ch)

        if ch not in [' ', '+', '*']:
            new_number_str += ch
        #print(curr_row[i])
    print(curr_column_chars)

    for sequence in curr_column_chars:
        math_symbol = None
        for ch in sequence:
            if ch != ' ':
                math_symbol = ch
                break

        if (math_symbol == '+' and new_number_str != ' '):
            grand_total += int(new_number_str)
            print(new_number_str)
            if pom == 1: grand_total -= 1
            else: pom = 0
        elif (math_symbol == '*' and new_number_str != ' '): 
            grand_total *= int(new_number_str) 
            print(new_number_str)

print("Grand total: ", grand_total)