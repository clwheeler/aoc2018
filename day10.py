import collections
import time
import re
import sys
from itertools import cycle


def load_inputs(day):
    inputs = []
    # parse input data
    with open('day{}_input.txt'.format(day), 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    input_list = []
    for line in inputs:
        matches = re.match(r'position=<([\s\d-]+),([\s\d-]+)> velocity=<([\s\d-]+),([\s\d-]+)>', line)
        input_list.append((int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))))
    return input_list


def load_test(day):
    inputs = []
    # parse input data
    with open('day{}_sample.txt'.format(day), 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    input_list = []
    for line in inputs:
        matches = re.match(r'position=<([\s\d-]+),([\s\d-]+)> velocity=<([\s\d-]+),([\s\d-]+)>', line)
        input_list.append((int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))))
    return input_list

def get_bounding_box(points):
    zipped = zip(*points)
    min_x = min(zipped[0])
    min_y = min(zipped[1])
    max_x = max(zipped[0])
    max_y = max(zipped[1])

    return (max_x - min_x) * (max_y - min_y)

def print_grid(points):
    zipped = zip(*points)
    min_x = min(zipped[0])
    min_y = min(zipped[1])
    max_x = max(zipped[0])
    max_y = max(zipped[1])

    for y in range(1 + max_y - min_y):
        row = []
        for x in range(1 + max_x - min_x):
            if (min_x + x, min_y + y) in points:
                row.append('#')
            else:
                row.append('.')
        print "".join(row)

def solve_part1(start):
    points = load_inputs(10)
    # points = load_test(10)
    # points = x, y, vx, vy
    last_points = []
    box = None
    last_box = None
    seconds = 0

    while last_box is None or box <= last_box:
        seconds += 1
        last_points = points
        points = map(lambda pt: (pt[0] + pt[2], pt[1] + pt[3], pt[2], pt[3]), points)
        last_box = box
        box = get_bounding_box(points)

    pts = [(pt[0], pt[1]) for pt in last_points]

    print_grid(pts)


def solve_part2(start):
    points = load_inputs(10)
    # points = load_test(10)
    # points = x, y, vx, vy
    last_points = []
    box = None
    last_box = None
    seconds = 0

    while last_box is None or box <= last_box:
        seconds += 1
        last_points = points
        points = map(lambda pt: (pt[0] + pt[2], pt[1] + pt[3], pt[2], pt[3]), points)
        last_box = box
        box = get_bounding_box(points)
    print seconds - 1

def run():

    start_time = time.time()
    print "Part 1:"
    print solve_part1(0)
    print "Runtime: {} seconds".format(time.time() - start_time)

    start_time = time.time()
    print "Part 2:"
    solve_part2(0)
    print "Runtime: {} seconds".format(time.time() - start_time)


run()
