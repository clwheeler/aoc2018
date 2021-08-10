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


class ScanGrid(object):

    droppers = set()
    grid = []
    min_x = min_y = max_x = max_y = None

    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x - 1
        self.min_y = min_y
        self.max_x = max_x + 2
        self.max_y = max_y + 1
        pass

    def set_at(self, x, y, char):
        adjusted_x = x - self.min_x
        adjusted_y = y - self.min_y
        try:
            self.grid[adjusted_y][adjusted_x] = char
        except:
            print "Panic: {}, {}".format(adjusted_x, adjusted_y)
            return None

    def get_at(self, x, y):
        adjusted_x = x - self.min_x
        adjusted_y = y - self.min_y
        if adjusted_y < self.min_y or adjusted_y >= self.max_y:
            return None
        try:
            return self.grid[adjusted_y][adjusted_x]
        except:
            print "Panic: {}, {}".format(adjusted_x, adjusted_y)
            return None

    def load_grid(self, x_list, y_list):
        self.grid = [[" " for x in range(self.min_x, self.max_x)] for y in range(self.min_y, self.max_y)]

        for group in x_list:
            fixed_x = group[0] - self.min_x
            for y in range(group[1][0], group[1][1] + 1):
                self.grid[y - self.min_y][fixed_x] = '#'

        for group in y_list:
            fixed_y = group[0] - self.min_y
            for x in range(group[1][0], group[1][1] + 1):
                self.grid[fixed_y][x - self.min_x] = '#'

    def add_dropper(self, pos):
        self.droppers.add(pos)

    def tick_droppers(self):
        # print list(self.droppers)
        for drop in list(self.droppers):
            # print "drop at: ", drop[0], drop[1]
            self.drop(drop[0], drop[1])

    def drop(self, x, y):
        # create drop at x, y
        drop_x = x
        drop_y = y
        this_set = []

        # go as far down as possible
        while(self.get_at(drop_x, drop_y + 1) not in ["#", "-"] and self.get_at(drop_x, drop_y + 1) is not None):
            self.set_at(drop_x, drop_y + 1, '|')
            drop_y += 1

        # fill left and right
        stable = True

        if self.get_at(drop_x, drop_y + 1) is not None:
            this_set.append((drop_x, drop_y))

        while(self.get_at(drop_x - 1, drop_y) not in ["#", "-"] and self.get_at(drop_x, drop_y + 1) is not None):
            this_set.append((drop_x - 1, drop_y))
            if self.get_at(drop_x - 1, drop_y + 1) in ["#", "-"]:
                drop_x -= 1
            else:
                self.add_dropper((drop_x - 1, drop_y))
                stable = False
                break

        while(self.get_at(drop_x + 1, drop_y) not in ["#", "-"] and self.get_at(drop_x, drop_y + 1) is not None):
            this_set.append((drop_x + 1, drop_y))

            if self.get_at(drop_x + 1, drop_y + 1) in ["#", "-"]:
                drop_x += 1
            else:
                self.add_dropper((drop_x + 1, drop_y))
                stable = False
                break

        if stable:
            for elem in this_set:
                self.set_at(elem[0], elem[1], "-")
        else:
            for elem in this_set:
                self.set_at(elem[0], elem[1], "~")


    def print_grid(self):
        count_stable = 0
        count = 0
        for y in self.grid:
            print "".join(y)
            count += y.count("~")
            count += y.count("|")
            count += y.count("-")
            count_stable += y.count("-")
        return count, count_stable


def load_test():
    return """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504""".splitlines()


def solve_part1(start):
    inputs = load_inputs(17)
    # inputs = load_test()
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0
    x_group = []
    y_group = []

    for group in inputs:
        parsed = re.match(r"[xy]=(\d+), [xy]=(\d+)\.\.(\d+)", group)
        parsed_group = (int(parsed.group(1)), (int(parsed.group(2)), int(parsed.group(3))))
        if group[0] == "x":
            min_x = min(parsed_group[0], min_x)
            min_y = min(parsed_group[1][0], min_y)
            max_x = max(parsed_group[0], max_x)
            max_y = max(parsed_group[1][1], max_y)
            x_group.append(parsed_group)
        else:
            min_y = min(parsed_group[0], min_y)
            min_x = min(parsed_group[1][0], min_x)
            max_y = max(parsed_group[0], max_y)
            max_x = max(parsed_group[1][1], max_x)
            y_group.append(parsed_group)

    grid = ScanGrid(min_x, min_y, max_x, max_y)
    grid.load_grid(x_group, y_group)

    # grid.seek(500, 1)

    grid.add_dropper((500, 0))
    for x in range(999):
        grid.tick_droppers()
    count, stable = grid.print_grid()
    print count
    print stable


def solve_part2(start):
    pass


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
