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
    pass


def solve_part1(count):
    # inputs = load_inputs(14)
    # dependencies = load_test()
    recipes = [3,7]
    elf1 = 0
    elf2 = 1

    for step in xrange(100000000):
        r1 = recipes[elf1]
        r2 = recipes[elf2]
        # print elf1, elf2, recipes
        value = r1 + r2
        value_list = [int(x) for x in [c for c in str(value)]]
        for elem in value_list:
            recipes.append(elem)
        elf1 = (elf1 + (r1 + 1)) % len(recipes)
        elf2 = (elf2 + (r2 + 1)) % len(recipes)

        if len(recipes) > (count + 10):
            print recipes[count:count+10]
            return

def solve_part2(val):
    # inputs = load_inputs(14)
    # dependencies = load_test()
    recipes = "37"
    val_str = str(val)
    elf1 = 0
    elf2 = 1

    for step in xrange(100000000):
        r1 = int(recipes[elf1])
        r2 = int(recipes[elf2])
        # print elf1, elf2, recipes
        value = r1 + r2
        recipes += str(value)
        elf1 = (elf1 + (r1 + 1)) % len(recipes)
        elf2 = (elf2 + (r2 + 1)) % len(recipes)

        if step % 10000 == 0:
            sys.stdout.write('{}...'.format(step))
            sys.stdout.write('\r')
            sys.stdout.flush()

        if val_str in recipes[-12:]:
            print ""
            print recipes.index(val_str)
            return


def run():

    start_time = time.time()
    print "Part 1:"
    # print solve_part1(846021)
    print "Runtime: {} seconds".format(time.time() - start_time)

    start_time = time.time()
    print "Part 2:"
    solve_part2(846021)
    print "Runtime: {} seconds".format(time.time() - start_time)


run()
