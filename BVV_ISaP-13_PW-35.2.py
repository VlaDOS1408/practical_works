#Practical Work 35
#2 Problem

import random

points = []

def find_distanse_midle_two_points(point1, point2):
    distanse = (( point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
    return distanse;

count_of_rnd_points = None;

while count_of_rnd_points == None:
    try:
        count_of_rnd_points = int(input("Enter count of random points: "))
    except:
        print("\nUncorrect input!\n")
    
for i in range(count_of_rnd_points):
    points += [[random.randint(-10, 10), random.randint(-10, 10)]]
    print(f"{i+1}: \t{points[i]}")
    
max_distanse = 0;
most_remote_points = [[],[]]

for i in points:
    for j in points:
        _distanse = find_distanse_midle_two_points(i, j)
        
        if _distanse > max_distanse:
            max_distanse = _distanse;
            most_remote_points[0] = i;
            most_remote_points[1] = j;
        
print(f'''
Max distanse between two points: {max_distanse}
Points: {most_remote_points}
      ''')

input()

        
