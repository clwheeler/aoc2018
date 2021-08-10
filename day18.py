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

    return inputs


class Grid(object):

    grid = []
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_at(self, x, y, char):
        self.grid[y][x] = char

    def get_at(self, x, y):
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return self.grid[y][x]
        else:
            return None

    def get_neighbors(self, x, y):
        neighbors = []
        for xs in range(-1, 2):
            for ys in range(-1, 2):
                if not xs == ys == 0:
                    neighbors.append(self.get_at(x + xs, y + ys))

        return [n for n in neighbors if n is not None]

    def load_grid(self, grid):
        self.grid = [[x for x in y] for y in grid]

    def print_grid(self):
        for y in self.grid:
            print "".join(y)
        print ""

    def tick(self):
        new_grid = [[x for x in row] for row in self.grid]
        for y in range(0, self.height):
            for x in range(0, self.width):
                neighbors = self.get_neighbors(x, y)
                if self.get_at(x, y) == '.':
                    if neighbors.count("|") > 2:
                        new_grid[y][x] = "|"
                elif self.get_at(x, y) == '|':
                    if neighbors.count("#") > 2:
                        new_grid[y][x] = "#"
                elif self.get_at(x, y) == '#':
                    if neighbors.count("|") > 0 and neighbors.count("#") > 0:
                        new_grid[y][x] = "#"
                    else:
                        new_grid[y][x] = "."
        self.grid = new_grid

    def get_value(self):
        trees = 0
        yards = 0

        for y in self.grid:
            trees += y.count("|")
            yards += y.count("#")

        return trees * yards



def load_test():
    return """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.""".splitlines()


def solve_part1(start):
    inputs = load_inputs(18)
    # inputs = load_test()
    width = len(inputs[0])
    height = len(inputs)

    grid = Grid(width, height)
    grid.load_grid(inputs)
    for x in range(10):
        grid.tick()

    print grid.get_value()


def solve_part2(start):
    inputs = load_inputs(18)
    # inputs = load_test()
    width = len(inputs[0])
    height = len(inputs)

    grid = Grid(width, height)
    grid.load_grid(inputs)

    past_values = []
    current_values = []
    for x in xrange(28 * 20 + 20):
        grid.tick()
    print 448 + 20
    print grid.get_value()

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
