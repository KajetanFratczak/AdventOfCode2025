# Advent of Code 2025 - task 1 of day 2
# We want to add up all of the "invalid" ID-s (based on some rules)

# sequences repeated twice - invalid
# for example 5555, 123123

# none of the numbers have leading zeros - 0101 isn't an ID at all

# Reading the file 
file = open("day2/input2.txt", "r")
sequence = file.read().rsplit(",")

# rsplit() - splits a string into a list, starting from the right.

# Solving the main task 
result = 0

def number_is_id(id):
    result = False
    half = len(id) // 2
    #print(half)
    left_side = id[:half]
    right_side = id[half:]
    #print(left_side)
    #print(right_side)
    if (left_side == right_side):
        result = True
    return result

#print(number_is_id("11"))

for id_ranges in sequence:
    left,right = id_ranges.rsplit("-")
    #print(left)
    left = int(left)
    right = int(right)

    for id in range (left, right+1):
        #print(id)
        # I check all numbers from left to right
        # for example from 11 to 22
        # then we check if there are some like 11 or 22 or 123123
        id = str(id)
        if (len(id)%2 == 0 and number_is_id(id) == True):
            #print(id)
            result += int(id)
print(result)