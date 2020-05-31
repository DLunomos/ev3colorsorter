from math import sqrt
from collections import Counter
import csv
import random
import os

def find_distance(a, b):
    return sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2 + abs(a[2]-b[2])**(.5))

color_list = []

with open("color_list.csv", "r") as color_list_file:
    reader = csv.reader("color_list_file")
    next(color_list_file)
    for line in color_list_file:
        line = line.split(",")

        for x in range(3):
            line[x] = int(line[x])
        line[3] = line[3].strip()
        color_list.append(line)

data = color_list.copy()

test_set = []

for x in range(int(len(color_list) // (10/7))):
    random_choice = random.choice(color_list)
    test_set.append(random_choice)
    color_list.remove(random_choice)

distance_list = []
min_distance = []

def knn(color, set, k):
    distance_list = []
    min_distance = []
    min_distance_colors = []
    distance_colors = []
    for i in set:
        distance_colors.append(i[3])
        distance_list.append(find_distance(color, i))
    for a in range(k):
        min_distance_colors.append(distance_colors[distance_list.index(min(distance_list))])
        distance_list.remove(min(distance_list))
        distance_colors.pop(distance_list.index(min(distance_list)))
    c = Counter(min_distance_colors)
    return c.most_common(1)[0][0]

code = ""

with open(os.path.join("..", "main.py"), "r") as main:
    code = main.readlines()

code = code[:181]

with open(os.path.join("..", "main.py"), "w") as main:
    main.writelines(code)

with open(os.path.join("..", "main.py"), "a") as main:
    main.write("\n" + "data = " + str(data))