# Advent of Code 2025 - task 1 of day 5

# database operates on ingredients IDs
# we have list of fresh ingredient ID ranges, blank line, and a list of available ingredient IDs
# we want to get 

# Reading the file
file = open("day5/input5.txt", "r")
lines = file.read().splitlines()
fresh_ingredients_IDs = []
availabie_ingredients_IDs = []
pom = 0

for line in lines:
    if (pom == 0 and line!=""):
        fresh_ingredients_IDs.append(line)
    if (pom == 1 and line!=""):
        availabie_ingredients_IDs.append(line)
    if (line == ""):
        pom = 1

# Solving the main task
# we want to check which of available ingredients are fresh
result = 0 
for ingredient in availabie_ingredients_IDs:
    ing_pom = 0
    for id_range in fresh_ingredients_IDs:
        # if our ingredient is in any of the ranges - we count it 
        id_numbers = id_range.split("-")
        left_id = id_numbers[0]
        right_id = id_numbers[1]
        #print(left_id, right_id)
        
        if (int(left_id) <= int(ingredient) <= int(right_id) and ing_pom != 1):
            result += 1
            # we don't want to count the same ingredient twice
            ing_pom = 1

    if (ing_pom == 1):
        continue

print("Result: ", result)

#print(fresh_ingredients_IDs)
#print(availabie_ingredients_IDs)