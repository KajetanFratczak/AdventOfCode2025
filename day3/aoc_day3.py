# Advent of Code 2025 - task 1 of day 3

# we have banks of batteries
# we need to turn on exactly two of them from each bank
# we need to find biggest possible two-digit sequence in each bank (number may not be close to each other)
# but they have to be from left to right

# Reading the file 
file = open("day3/input3.txt", "r")
sequence = file.read().splitlines()

def best_two_digit(bank):
    # from 0 to n-1 pos in a number we look for the biggest one
    # we mark the place in a bank and then search for right digit in the right side from found digit
    max_left_digit = 1
    max_right_digit = 1
    mark_left_found = 0
    bank_size = len(bank)

    # left digit
    for i in range(0,bank_size-1):
        if int(bank[i]) > max_left_digit:
            max_left_digit = int(bank[i])
            mark_left_found = i
    
    # right digit
    for j in range(mark_left_found+1, bank_size):
        if int(bank[j]) > max_right_digit:
            max_right_digit = int(bank[j])

    # our final number 
    result = 10*max_left_digit + max_right_digit

    return result

# Solving the main task
total_joltage = 0

for bank in sequence:
    best_joltage = best_two_digit(bank)
    total_joltage += best_joltage
print("Total joltage: ", total_joltage)

# -------------------------------------------------------------
# Advent of Code 2025 - task 2 of day 3

# the twist is that now we have to find 12-digit number from the sequence
# Subsequence problem
def best_twelve_digit(bank):
    # from 0 to n-1 pos in a number we look for the biggest one
    # we mark the place in a bank and then search for right digit in the right side from found digit
    # and we do this couple of times...
    # Strategy: we find max number, mark where we found it and go to find the next one ...
    bank_size = len(bank)
    digits_needed = 12
    result = 0
    
    if bank_size < 12:
        return 0
    
    max_digits = []
    current_search_idx = 0

    for k in range(digits_needed):
        remaining_needed = digits_needed - 1 - k
        search_limit = bank_size - remaining_needed # beacause we have to find 12 digits (we can't if we won't have enough)

        best_digit = 0
        best_digit_idx = 0

        for i in range(current_search_idx, search_limit):
            if (int(bank[i]) > best_digit):
                best_digit = int(bank[i])
                best_digit_idx = i

        max_digits.append(best_digit)

        current_search_idx = best_digit_idx + 1  

    # our final number
    i=0
    for digit in max_digits:
        i+=1
        result += 10**(digits_needed-i) * digit

    return result

# Solving the main task
total_joltage = 0

for bank in sequence:
    best_joltage = best_twelve_digit(bank)
    total_joltage += best_joltage
    #print(best_joltage)
print("Total joltage: ", total_joltage)