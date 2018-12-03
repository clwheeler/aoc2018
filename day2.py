import sys
import collections
import time
from itertools import cycle

def load_inputs():

    inputs = []

    # parse input data
    with open('day2_input.txt', 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs

def test_inputs():
    return ["abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"]

# check if the input has a letter that occurs exactly n times
def has_letter_occurs(my_str, num):
    letter_count = {}
    for letter in my_str:
        this_letter = letter_count.get(letter, 0)
        letter_count[letter] = this_letter + 1

    return num in letter_count.values()

def solve_part1(start):
    inputs = load_inputs()
    all_counts = {}

    for row in inputs:
        if has_letter_occurs(row, 2):
            all_counts[2] = all_counts.get(2, 0) + 1
        if has_letter_occurs(row, 3):
            all_counts[3] = all_counts.get(3, 0) + 1

    print all_counts[2] * all_counts[3]


def solve_part2(start):
    # inputs = test_inputs()
    inputs = load_inputs()

    for x in range(len(inputs)):
        val = inputs[x]

        for inner_val in inputs[x+1:]:
            # find num letters that differ
            diffs = []
            for a in zip(val, inner_val):
                if a[0] != a[1]:
                    diffs.append(a)

            if len(diffs) == 1:
                print "{}, {}".format(val, inner_val)
                print diffs
                # letter_set = set()
                # for letter in val:
                #     if letter not in diffs[0]:
                #         letter_set.add(letter)
                # print "{}".format("".join(list(letter_set)))

start_time = time.time()

# print "Part 1:"
# solve_part1(0)
print "Part 2:"
solve_part2(0)

print "Runtime: {} seconds".format(time.time() - start_time)
