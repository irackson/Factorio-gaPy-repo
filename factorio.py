## blueprints and their jsons can be found at: https://factorioprints.com/
## custom blueprints made in game for testing purposes can be decoded at: https://burnysc2.github.io/Factorio/Tools/DecodeBlueprint/

# import necessary modules
import os.path
import json
import matplotlib.pyplot as plt
import numpy
import math

# identify the location where json blueprint files are saved
bp_json_save_path = '/home/ianrackson/Desktop/Project/Blueprints/'

# prompt user for the name of the blueprint to be analized and the accuracy with which the program should run
bp_name = input("Enter blueprint name: ")
accuracy = int(input("Enter accuracy: "))

# join the file path with the inputed blueprint name
complete_name = os.path.join(bp_json_save_path, bp_name + ".json")

# open and read the contents of the blueprint file as "bp", then close the file
bp_file = open(complete_name, "r")
bp = json.loads(bp_file.read())
bp_file.close()

# extract the x and y coordinates of each entity in the bp 
xs = []
ys = []
for i in range (0, len(bp["blueprint"]["entities"])):
    xs.append(bp["blueprint"]["entities"][i]["position"]["x"])
    ys.append(bp["blueprint"]["entities"][i]["position"]["y"])

# find the corners of the blueprint
    # lower left = min_x, min_y
    # lower right = max_x, min_y
    # upper left = min_x, max_y
    # upper right = max_x, max_y
min_x = min(xs)
min_y = min(ys)
max_x = max(xs)
max_y = max(ys)


# defines a function that, given an x and y coordinate, finds the total distance from each entity to that point and back
def totalDistance(point_x, point_y):
    total_distance = 0
    for x in xs:
        for y in ys:
            total_distance += int(2*math.sqrt((x - point_x)*(x - point_x) + (y - point_y)*(y - point_y)))
    return total_distance

# create an array of each possible location within the area of the blueprint
points_x = []
points_y = []
for x in range(int(min_x), int(max_x)):
    for y in range(int(min_y), int(max_y)):
        points_x.append(x)
        points_y.append(y)


# loop through all possible locations within the area of the blueprint, given the user inputted accuracy, and calculate the totalDistance for each point.
# then, select "min_distance" and it's respective x and y coordinates to be the smallest of all calculated totalDistances
min_distance = 1000000000000000
best_x = 0
best_y = 0

for x in range(0, len(points_x) - 1, accuracy):
    for y in range(0, len(points_y) - 1, accuracy):
        distance = totalDistance(points_x[x], points_y[y])
        if distance < min_distance:
            min_distance = distance
            best_x = points_x[x]
            best_y = points_y[y]

# plot all entities in the blueprint
# plot the point of minimum distance to each entity
plt.plot(xs, ys, linewidth = 0, marker='o', markerfacecolor='blue', markersize=12) 
plt.plot(best_x, best_y, color='red', marker='o', markerfacecolor='red', markersize=24)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title(bp_name)
plt.show()