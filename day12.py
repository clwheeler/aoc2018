import collections
import time
import re
import sys
from itertools import cycle

INITIAL_STATE = ".#..##..#.....######.....#....####.##.#.#...#...##.#...###..####.##.##.####..######......#..##.##.##"

def load_inputs(day):
    inputs = []
    # parse input data
    with open('day{}_input.txt'.format(day), 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs

def load_test():
    return """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #""".splitlines()

def run_generation(init_state, rules):
    # Pot 0 is index 3
    new_state = "..."
    state = init_state

    for index, pot in enumerate(state):
        matched = False
        for rule in rules:
            if state[index:index + 5] == rule[0]:
                new_state += rule[1]
                matched = True
        if not matched:
            new_state += "."
            # print "PANIC: {}".format(index),  "".join(state[index:index + 5])

    return new_state

def solve_part1(start):
    inputs = load_inputs(12)
    init = INITIAL_STATE

    # inputs = load_test()
    # init = [x for x in "#..#.#..##......###...###"]

    inputs = [(re.match(r"([.#]+) => ([.#])", rule).group(1), re.match(r"([.#]+) => ([.#])", rule).group(2)) for rule in inputs]

    state = init
    state = "..." + state + "..."

    generations = 20
    for x in range(generations):
        state = run_generation(state, inputs)
        state = state[1:]

    count = 0
    for ind, x in enumerate(state):
        if x == '#':
            count += ind - (3)

    print count


def solve_part2(start):
    generations = 50000000000
    print "{}".format((((generations - 1) + 10) * 81) + 69)


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
