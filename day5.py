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

def load_test():
    return "dabAcCaCBAcCcaDA"

def solve_for_list(inputs):
    # print inputs
    sub_list = []

    list_dirty = True

    while list_dirty:
        list_dirty = False

        for elem in inputs:
            if not sub_list:
                sub_list.append(elem)
            else:
                if sub_list[-1].isupper() != elem.isupper() and sub_list[-1].upper() == elem.upper():
                    sub_list.pop()
                    list_dirty = True
                else:
                    sub_list.append(elem)

        inputs = sub_list
        sub_list = []

    return len(inputs)

def solve_part1(start):
    inputs = load_inputs(5)[0]
    # inputs = load_test()
    print solve_for_list(inputs)


def solve_part2(start):
    inputs = load_inputs(5)[0]

    char_list = inputs.upper()
    char_list = sorted(list(set(char_list)))

    print char_list

    # char, size
    min_val = (None, None)
    for char in char_list:
        trial_list = filter(lambda x: x.upper() != char, inputs)
        size = solve_for_list(trial_list)
        # print char, size
        if not min_val[1] or size < min_val[1]:
            min_val = (char, size)

    print min_val


def run():

    start_time = time.time()

    print "Part 1:"
    solve_part1(0)
    print "Part 2:"
    solve_part2(0)

    print "Runtime: {} seconds".format(time.time() - start_time)

run()
