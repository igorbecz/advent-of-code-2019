import os
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def load_file():
    f = open("C:\\Users\\Igor\\github\\advent-of-code-2019\\3\\input.txt", "r")
    lines = f.readlines()

    for path in lines[0].split(","):
        first_wire.append(path)

    for path in lines[1].split(","):
        second_wire.append(path)

def get_points_from_wire(wire):
    points = []
    points.append(Point(0,0))

    for point in wire:
        if point[0] == 'R':
            points.append(Point(points[-1].x + int(point[1:]), points[-1].y))
        elif point[0] == 'L':
            points.append(Point(points[-1].x - int(point[1:]), points[-1].y))
        elif point[0] == 'U':
            points.append(Point(points[-1].x, points[-1].y - int(point[1:])))
        elif point[0] == 'D':
            points.append(Point(points[-1].x, points[-1].y + int(point[1:])))

    for point in points:
        print("(%d,%d)" % (point.x, point.y))

    print("\n")
    return points

def get_size(wire_one_points, wire_two_points):
    all_points = wire_one_points + wire_two_points

    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = -sys.maxsize
    max_y = -sys.maxsize

    for point in all_points:
        if point.x < min_x:
            min_x = point.x
        if point.y < min_y:
            min_y = point.y
        if point.y > max_x:
            max_x = point.x
        if point.y > max_y:
            max_y = point.y

    
    print("min_x = %d\nmin_y = %d\nmax_x = %d\nmax_y = %d\n" % (min_x, min_y, max_x, max_y))
    print("x = %d, y = %d" % (abs(min_x)+abs(max_x), abs(min_y)+abs(max_y)))
    

first_wire = []
second_wire = []

load_file()



first_wire_points = get_points_from_wire(first_wire)
second_wire_points = get_points_from_wire(second_wire)

get_size(first_wire_points, second_wire_points)
