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


def load_test():
    return "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"

DIRS = {'N': (0, 1),
        'E': (1, 0),
        'W': (-1, 0),
        'S': (0, -1)}

ROOMS = collections.defaultdict(int)

def compute_path(from_pos, path, init_length):
    global ROOMS
    this_path = path
    length = init_length
    pos = from_pos


    while this_path:
        this_char = this_path[0]
        this_path = this_path[1:]
        if this_char in ['N', 'E', 'W', 'S']:
            pos = tuple(map(sum, zip(pos, DIRS[this_path[0]])))
            length += 1
            ROOMS[pos] = min(ROOMS[pos], length) or length
            this_path = this_path[1:]
        if this_char in ["("]:
            this_path = compute_path(pos, this_path[1:], length)
        if this_char in ["|"]:
            length = init_length
            pos = from_pos
        if this_char in [")"]:
            this_path = this_path[1:]
            break

    print ROOMS

    return this_path

def solve_part1(start):
    ROOMS[(0, 0)] = 0
    # inputs = load_inputs(20)
    inputs = load_test()
    # chomp first char
    inputs = inputs[1:]
    compute_path((0, 0), inputs, 0)



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
