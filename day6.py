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
        matches = re.match(r'(\d+), (\d+)', line)
        input_list.append((matches.group(1), matches.group(2)))
    return input_list


def load_test():
    test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split('\n')

    input_list = []
    for line in test_input:
        matches = re.match(r'(\d+), (\d+)', line)
        input_list.append((matches.group(1), matches.group(2)))
    return input_list


def get_grid(inputs):
    max_x = max([int(pt[0]) for pt in inputs]) + 1
    max_y = max([int(pt[1]) for pt in inputs]) + 1

    # create grid at max-size
    grid = [{} for x in range(max_x * max_y)]

    # for each space in grid, compute distance to each elem
    for index, item in enumerate(grid):
        x_pos = index / max_y
        y_pos = index % max_y

        for elem in inputs:
            grid_dist = grid[index]
            grid_dist[elem] = abs(x_pos - int(elem[0])) + abs(y_pos - int(elem[1]))

    return grid


def solve_part1(start):
    inputs = load_inputs(6)

    max_x = max([int(pt[0]) for pt in inputs]) + 1
    max_y = max([int(pt[1]) for pt in inputs]) + 1
    grid = get_grid(inputs)

    # for each space, find closest point
    for index, item in enumerate(grid):
        x_pos = index / max_y
        y_pos = index % max_y

        min_key = None
        min_dist = None
        for key, value in item.iteritems():
            if not min_key:
                min_key = key
                min_dist = value
                continue

            # equidistant, invalid
            if value == min_dist:
                min_key = -1
                min_dist = value
            elif value < min_dist:
                min_key = key
                min_dist = value

        grid[index] = min_key

    for index, item in enumerate(grid):
        x_pos = index / max_y
        y_pos = index % max_y

    nearest = {}
    # aggregate on to closest point
    for point in inputs:
        nearest[point] = grid.count(point)

    # invalidate along boundaries
    for index, item in enumerate(grid):
        x_pos = index / max_y
        y_pos = index % max_y

        if x_pos == 0 or x_pos == max_x or y_pos == 0 or y_pos == max_y:
            if grid[index] in nearest:
                nearest.pop(grid[index])

    max_size = None
    for value in nearest.values():
        if not max_size or value > max_size:
            max_size = value

    print max_size

    # get max value point


def solve_part2(start):
    inputs = load_inputs(6)
    # inputs = load_test()

    max_x = max([int(pt[0]) for pt in inputs]) + 1
    max_y = max([int(pt[1]) for pt in inputs]) + 1
    grid = get_grid(inputs)

    for index, item in enumerate(grid):
        total_distance = sum(item.values())
        grid[index] = total_distance

    print len(filter(lambda x: x < 10000, grid))


def run():

    start_time = time.time()
    print "Part 1:"
    solve_part1(0)
    print "Runtime: {} seconds".format(time.time() - start_time)

    start_time = time.time()
    print "Part 2:"
    solve_part2(0)
    print "Runtime: {} seconds".format(time.time() - start_time)


run()

