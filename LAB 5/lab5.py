# You are given a list of n points in a 2D coordinate plane. Your task is to find the pair of
# points that are closest to each other in terms of Euclidean distance. Your solution must
# use a divide-and-conquer strategy to achieve O(n log n) time complexity.


# read input from a file .txt


# Print the minimum distance and the coordinates of the closest pair to the terminal or
# console. Round the distance to 4 decimal places

import math

def closestPair(points_x, points_y = None):
    if points_y is None:
        points_y = sorted(points_x, key=lambda p: p[1])

    if len(points_x) <= 3:
        min_dist = float('inf')
        for i in range(len(points_x)):
            for j in range(i + 1, len(points_x)):
                dist = math.dist(points_x[i], points_x[j])
                closest_pair = points_x[i], points_x[j]
                if dist < min_dist:
                    min_dist = dist
        return min_dist , (closest_pair)


    mid = len(points_x) // 2
    midpoint = points_x[mid][0]
    left_points_x, right_points_x = points_x[:mid], points_x[mid:]

    left_points_y = [p for p in points_y if p in left_points_x]
    right_points_y = [p for p in points_y if p in right_points_x]

    distance_1, (closest_pair1) = closestPair(left_points_x, left_points_y)
    distance_2, (closest_pair2) = closestPair(right_points_x, right_points_y)



    if(distance_1 <= distance_2):
        closest_pair = (closest_pair1)
    elif (distance_2 < distance_1):
        closest_pair = (closest_pair2)
    min_distance = min(distance_1, distance_2)

    strip = [p for p in points_y if abs(p[0] - midpoint) < min_distance]


    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            dist = math.dist(strip[i], strip[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (strip[i], strip[j])

    return min_distance, closest_pair





all_points = []

with open("test.txt", 'r') as f:
    for line in f:
        point = [int(num) for num in line.strip().split()]
        all_points.append(point)


all_points = sorted(all_points, key=lambda x: x[0])

result = closestPair(all_points)

distance, (point1, point2) = result

print(f"Distance = {distance:.4f} and Closest pair = ({point1[0]},{point1[1]}) and ({point2[0]},{point2[1]})")



