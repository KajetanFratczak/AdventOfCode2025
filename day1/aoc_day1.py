# Advent of Code 2025 - task 1 of day 1
# We have a safe to unlock
# We can move Left and Right to change the digit at the current position
# Numbers on the safe are from 0 to 99
# If for example we are on digit 5: rotation L10 would move us to 95, a rotation R5 would move us to 0
# We have a sequence of rotations to perform - starting from digit 50 
# We need to calculate number of times we land on 0 

# Reading the file 
file = open("input.txt", "r")
sequence = file.read().splitlines()
# The splitlines() method splits a string into a list. The splitting is done at line breaks.
# print(sequence)
# print(sequence[0]) - due to splitlines I now can access each line by its index

# Solving the main task 
number_of_zeros = 0
starting_pos = 50
pom_cnt = 0

for change in sequence:
    # number to move
    change_number = int(change[1:])
    
    # direction to move
    change_dir = change[0]

    # flag for starting configuration
    if pom_cnt == 0:
        new_pos = starting_pos

    # calculating new position
    if change_dir == "L":
        new_pos -= change_number
        if new_pos < 0:
            new_pos += (int((abs(new_pos)+100)/100) * 100)
        pom_cnt += 1
        if new_pos == 100:
            new_pos -= 100
        #print(new_pos)
    elif change_dir == "R":
        new_pos += change_number
        if new_pos > 99:
            new_pos -= (int(new_pos/100) * 100)  
        pom_cnt += 1
        #if new_pos < 0:
            #print("Error in R !!!")
            #print(change_number)
        #print(new_pos)

    if new_pos == 0:
        number_of_zeros += 1

print("Number of zeros: ", number_of_zeros)

# 905 - too low 
# sometimes I encounter negative numbers - why?
# Error in R - sometimes subtracts too much and I get negative result

# edge case in L : 
# pos = 34, L534, result is 100 and not 0 - why?
# substracting 100 in such a case
# 1055 is correct

# little stupid solution, next one using mod 
# 2 solution

# Solving the main task using modulo operation 
number_of_zeros = 0
starting_pos = 50
pom_cnt = 0

for change in sequence:
    # number to move
    change_number = int(change[1:])
    
    # direction to move
    change_dir = change[0]

    # flag for starting configuration
    if pom_cnt == 0:
        new_pos = starting_pos

    # calculating new position
    if change_dir == "L":
        new_pos -= change_number
        new_pos = new_pos % 100  
        # print(new_pos)
        pom_cnt += 1
    elif change_dir == "R":
        new_pos += change_number
        new_pos = new_pos % 100 
        # print(new_pos)
        pom_cnt += 1

    if new_pos == 0:
        number_of_zeros += 1

print("Number of zeros (using modulo): ", number_of_zeros)

# -----------------------------------------------------------------------
# Task 2 - day 1
# Now we wanna calculate each time when lock goes to 0 
# So we count even 0 when for example we do whole cycles like:
# L535 will spin 5 times over a 0 so we will count this for 5 zeros

# Solving the main task using modulo operation 
number_of_zeros = 0
starting_pos = 50
pom_cnt = 0

for change in sequence:
    # number to move
    change_number = int(change[1:])
    
    # direction to move
    change_dir = change[0]

    # flag for starting configuration
    if pom_cnt == 0:
        new_pos = starting_pos

    # calculating new position
    if change_dir == "L":
        old_pos = new_pos
        new_pos -= change_number
        new_pos = new_pos % 100  
        # full cycles as zeros
        number_of_zeros += change_number // 100
        # we have to resolve the edge case 
        if (old_pos - (change_number%100) < 0 and old_pos != 0 and new_pos != 0):
            number_of_zeros += 1
            #print(old_pos - change_number)
        pom_cnt += 1
    elif change_dir == "R":
        old_pos = new_pos
        new_pos += change_number
        new_pos = new_pos % 100 
        # full cycles as zeros
        number_of_zeros += change_number // 100
        # we have to resolve the edge case 
        if (old_pos + (change_number%100) > 100 and old_pos != 0 and new_pos != 0):
            number_of_zeros += 1
            #print(old_pos + change_number)
        pom_cnt += 1

    if new_pos == 0:
        number_of_zeros += 1

print("Number of zeros (using modulo): ", number_of_zeros)

# 6937 is not correct

# 6797 is not correct 

# 6386 is correct - finally