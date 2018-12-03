import sys
import collections
import time
from itertools import cycle

def load_inputs():

    inputs = []

    # parse input data
    with open('day1_input.txt', 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs

def solve_part1(start):
    value = start
    inputs = load_inputs()

    for row in inputs:
        num = float(row[1:])
        if row[0] == '+':
            value += num
        elif row[0] == "-":
            value -= num

    print value

def solve_part2(start):
    value = start
    inputs = load_inputs()
    visited_values = []
    visited_values.append(0)

    pool = cycle(inputs)

    for row in pool:
        num = float(row[1:])
        if row[0] == '+':
            value += num
        elif row[0] == "-":
            value -= num

        if value in visited_values:
            print value
            return
        else:
            visited_values.append(value)

start_time = time.time()

print "Part 1:"
solve_part1(0)
print "Part 2:"
solve_part2(0)

print "Runtime: {} seconds".format(time.time() - start_time)
