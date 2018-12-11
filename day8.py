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
    return "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")

metadata_total = []

def process_node(inputs):
    global metadata_total

    # # print "".join(inputs)
    # print inputs


    num_nodes = inputs[0]
    num_metadata = inputs[1]
    remaining = inputs[2:]

    for node in range(num_nodes):
        # process node
        remaining = process_node(remaining)

    if num_metadata:
        metadata_list = remaining[0:num_metadata]
        metadata_total.append(metadata_list)
        remaining = remaining[num_metadata:]

    return remaining

def solve_part1(start):
    sys.setrecursionlimit(99999)
    inputs = load_inputs(8)
    num_list = [int(x) for x in inputs[0].split()]

    # inputs = load_test()
    # num_list = [int(x) for x in inputs]

    partial = sum(process_node(num_list))
    print partial
    print sum([sum(x) for x in metadata_total])


def indexed_node(inputs):

    my_children_values = []
    my_value = 0

    num_nodes = inputs[0]
    num_metadata = inputs[1]
    remaining = inputs[2:]

    for node in range(num_nodes):
        remaining, value = indexed_node(remaining)
        my_children_values.append(value)

    if num_metadata:
        metadata_list = remaining[0:num_metadata]
        if not my_children_values:
            my_value = sum(metadata_list)
        else:
            for elem in metadata_list:
                ind = elem - 1
                if ind < len(my_children_values):
                    my_value += my_children_values[ind]

        metadata_total.append(metadata_list)
        remaining = remaining[num_metadata:]

    return remaining, my_value


def solve_part2(start):
    sys.setrecursionlimit(99999)
    inputs = load_inputs(8)
    num_list = [int(x) for x in inputs[0].split()]

    # inputs = load_test()
    # num_list = [int(x) for x in inputs]

    partial, value = indexed_node(num_list)
    print partial, value
    # print sum([sum(x) for x in metadata_total])


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
