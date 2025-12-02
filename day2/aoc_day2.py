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


# --------------------------------------------
# task 2 of day 2 - sequence must be repeated AT LEAST twice
# for example 111 has 1 repeated three times
# i will do a function which takes a string and check every prefix to the half if it creates a sequence
# brute force but it will work - I hope...

# Solving the main task 
result = 0

def number_is_id_v2(id):
    result = False
    id_len = len(id)
    # we have to go only to the half (after that sequence to repeat would be too long)
    for i in range(1,id_len//2 + 1):
        cnt = 0
        prefix = id[:i]
        # we check if it's a sequence if we can divide it into equal segments
        if id_len % i == 0:
            parts_number = id_len // i
            for part in range(parts_number):
                #print(part*i, (part+1)*i)
                if prefix == id[part*i : (part+1)*i]:
                    cnt += 1
            if cnt == parts_number:
                result = True
    return result

# example: id = "1010"
# we want to check 1 and 10 as prefixes and then check if it's 1 1 ... or 10 10 ...
# so prefix = id[0:i] for i from 1 to len(id)//2 
# then we check if prefix == id[part*i : (part+1)*i], where part = 0,1,2,...,len(id)//2
# i know that i check prefix with prefix , but it allows me to check cnt == parts_number and not cnt == parts_number -1

#print(number_is_id_v2("1010"))

for id_ranges in sequence:
    left,right = id_ranges.rsplit("-")
    left = int(left)
    right = int(right)

    for id in range (left, right+1):
        id = str(id)
        if (number_is_id_v2(id) == True):
            result += int(id)
print(result)