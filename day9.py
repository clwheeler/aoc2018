import collections
import time
import re
import sys
from itertools import cycle


def load_inputs(day):
    return "493 players; last marble is worth 71863 points"

def solve_part1(inputs):
    scores = collections.defaultdict(int)
    circle = collections.deque([0])

    player_list = [x for x in range(inputs[0])]
    player_cycler = cycle(player_list)


    for marble in range(1, inputs[1] + 1):
        player = player_cycler.next()
        if marble % 23 == 0:
            circle.rotate(7)
            scores[player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0



def solve_part2(start):
    pass


def run():

    start_time = time.time()
    print "Part 1:"
    print solve_part1((493, 71863))
    print "Runtime: {} seconds".format(time.time() - start_time)

    start_time = time.time()
    print "Part 2:"
    print solve_part1((493, 7186300))
    print "Runtime: {} seconds".format(time.time() - start_time)


run()
