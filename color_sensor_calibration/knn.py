from math import sqrt
import csv

def find_distance(a, b):
    return sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2 + abs(a[2]-b[2]))

color_list = []

with open("color_list.csv", "r") as color_list_file:
    reader = csv.reader("color_list_file")
    next(color_list_file)
    for line in color_list_file:
        line = line.split(",")

        for x in range(3):
            line[x] = int(line[x])
        line[3] = line[3].replace("\n", "")
        color_list.append(line)


        
print(color_list)