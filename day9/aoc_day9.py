# Advent of Code 2025 - task 1 of day 9

# the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. 
# They even have a list of where the red tiles are located in the grid (your puzzle input) (col, row).

# Reading the file
file = open("day9/input9.txt", "r")
lines = file.read().splitlines()

#print(lines)

# Solving the main task
max_area = 0

for location1 in lines:
    x,y = location1.split(',')
    x_int, y_int = int(x), int(y)
    #print("x: ", x, "y: ", y)
    for location2 in lines:
        x_2,y_2 = location2.split(',')
        x_2_int, y_2_int = int(x_2), int(y_2)
        if (location1 != location2):
            curr_area = (abs(x_int-x_2_int)+1)*(abs(y_int-y_2_int)+1)
            if (curr_area > max_area):
                max_area = curr_area
print("Max possible area: ", max_area)