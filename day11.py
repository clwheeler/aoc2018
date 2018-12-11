import collections
import time
import re
import sys
from itertools import cycle

SERIAL_NUMBER = 9995


def get_power_level(x, y):
    rack_id = x + 10
    power = rack_id * y
    power = power + SERIAL_NUMBER
    power = power * rack_id
    power = int(str(power)[-3]) - 5
    return power

GRID = []


def precompute_grid(grid_width):
    global GRID
    grid = []
    for sub_y in range(1, 1+grid_width):
        grid.append([get_power_level(sub_x, sub_y) for sub_x in range(1, 1+grid_width)])
    GRID = grid


def get_subgrid(x, y, width):
    subgrid = []

    for sub_y in range(y, y+width):
        # subgrid.append([get_power_level(sub_x, sub_y) for sub_x in range(x, x+width)])
        subgrid.append([GRID[sub_y-1][sub_x-1] for sub_x in range(x, x+width)])

    return subgrid


def solve_part1(start):

    grid_size = 300
    precompute_grid(300)

    max_value = None
    max_point = None

    for y in range(1, grid_size - 1):
        for x in range(1, grid_size - 1):
            subgrid = get_subgrid(x, y, 3)
            subgrid_value = sum([sum(g) for g in subgrid])
            if max_value is None or subgrid_value > max_value:
                max_value = subgrid_value
                max_point = (x, y)

    print max_point, max_value


def solve_part2(start):
    grid_size = 300

    max_value = None
    max_point = None
    max_width = None

    for y in range(1, grid_size - 1):
        for x in range(1, grid_size - 1):
            for width in range(50):
                if width + x < grid_size and width + y < grid_size:
                    subgrid = get_subgrid(x, y, width)
                    subgrid_value = sum([sum(g) for g in subgrid])
                    if max_value is None or subgrid_value > max_value:
                        max_value = subgrid_value
                        max_point = (x, y)
                        max_width = width

    print max_point, max_value, max_width


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
