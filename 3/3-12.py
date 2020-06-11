import os
import sys

class Point:
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps


def load_file():
    f = open("C:\\Users\\Igor\\github\\advent-of-code-2019\\3\\input.txt", "r")
    lines = f.readlines()

    for path in lines[0].split(","):
        first_wire.append(path)

    for path in lines[1].split(","):
        second_wire.append(path)


def get_all_points_from_wire(wire):
    points = []
    pos_x = 0
    pos_y = 0
    steps = 0

    for point in wire:
        count = int(point[1:])
        
        if point[0] == 'R':
            for i in range(count):
                pos_x += 1
                steps += 1
                points.append(Point(pos_x, pos_y, steps))
        elif point[0] == 'L':
            for i in range(count):
                pos_x -= 1
                steps += 1
                points.append(Point(pos_x, pos_y, steps))
        elif point[0] == 'U':
            for i in range(count):
                pos_y += 1
                steps += 1
                points.append(Point(pos_x, pos_y, steps))
        elif point[0] == 'D':
            for i in range(count):
                pos_y -= 1
                steps += 1
                points.append(Point(pos_x, pos_y, steps))

    for point in points:
        print("(%d,%d)" % (point.x, point.y))
    print("\n")
    return points


def get_common_points(first_wire_points, second_wire_points):
    common_points = []
    for first_point in first_wire_points:
        for second_point in second_wire_points:
            if first_point.x == second_point.x and first_point.y == second_point.y:
                common_points.append(Point(first_point.x, first_point.y, first_point.steps + second_point.steps))
                print("(%d,%d)" % (first_point.x, first_point.y))

    print("common")
    for point in common_points:
        print("(%d,%d, steps = %d)" % (point.x, point.y, point.steps))

    return common_points


def get_closest(points):
    min_sum = sys.maxsize

    for point in points:
        if abs(point.x) + abs(point.y) < min_sum:
            min_sum = abs(point.x) + abs(point.y)

    print(min_sum)


first_wire = []
second_wire = []

load_file()

first_wire_points = get_all_points_from_wire(first_wire)
second_wire_points = get_all_points_from_wire(second_wire)

common_points = get_common_points(first_wire_points, second_wire_points)

get_closest(common_points)
