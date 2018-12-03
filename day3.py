import collections
import time
import re
import sys
from itertools import cycle

def load_inputs():

    inputs = []

    # parse input data
    with open('day3_input.txt', 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs

def solve_part1(start):
    inputs = load_inputs()

    length = 1000
    grid = [[0 for x in range(length)] for y in range(length)]

    for elem in inputs:
        regex = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", elem)
        # parsed: [id, x, y, w, h]
        parsed = [int(regex.group(x)) for x in range(1, 6)]

        for y in range(parsed[1], parsed[1] + parsed[3]):
            for x in range(parsed[2], parsed[2] + parsed[4]):
                # print "{}, {}".format(x, y)
                grid[x][y] = grid[x][y] + 1

    count = 0
    for row in grid:
        for column in row:
            if column > 1:
                count += 1
    print count

def solve_part2(start):
    inputs = load_inputs()

    length = 1000
    grid = [[set() for x in range(length)] for y in range(length)]

    claims = []
    for elem in inputs:
        regex = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", elem)
        # parsed: [id, x, y, w, h]
        parsed = [int(regex.group(x)) for x in range(1, 6)]
        claims.append(parsed)

    for parsed in claims:
        for y in range(parsed[1], parsed[1] + parsed[3]):
            for x in range(parsed[2], parsed[2] + parsed[4]):
                grid[x][y].add(parsed[0])

    for claim in claims:
        clean = True
        for y in range(claim[1], claim[1] + claim[3]):
            for x in range(claim[2], claim[2] + claim[4]):
                if len(grid[x][y]) != 1:
                    clean = False
        if clean:
            print "clean: {}".format(claim)

def run():
    start_time = time.time()

    print "Part 1:"
    solve_part1(0)
    print "Part 2:"
    solve_part2(0)

    print "Runtime: {} seconds".format(time.time() - start_time)

run()
