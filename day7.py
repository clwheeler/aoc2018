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

    input_list = []
    for line in inputs:
        matches = re.match(r'Step ([a-zA-Z]) must be finished before step ([a-zA-Z]) can begin.', line)
        input_list.append((matches.group(1), matches.group(2)))
    return input_list


def load_test():
    inputs = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""".split('\n')

    input_list = []
    for line in inputs:
        matches = re.match(r'Step ([a-zA-Z]) must be finished before step ([a-zA-Z]) can begin.', line)
        input_list.append((matches.group(1), matches.group(2)))
    return input_list


def solve_part1(start):
    dependencies = load_inputs(7)
    # dependencies = load_test()
    all_options = []
    for x in dependencies:
        all_options.append(x[0])
        all_options.append(x[1])
    all_options = list(set(all_options))

    final_order = []

    while len(all_options):
        this_round = []
        for step in all_options:
            my_blockers = [elem for elem in dependencies if elem[1] == step]
            if not my_blockers:
                this_round.append(step)

        this_round = sorted(this_round)
        this_round = this_round[0]
        all_options = [x for x in all_options if x != this_round]
        dependencies = [x for x in dependencies if x[0] != this_round]
        final_order.append(this_round)

    return "".join(final_order)


class Worker(object):
    task = None
    duration = 0

    def set_task(self, char):
        self.task = char
        self.duration = (ord(char) - 64) + 60

    def do_work(self):
        if(self.task):
            self.duration = self.duration - 1

    def has_task(self):
        return self.task is not None

    def get_task(self):
        return self.task

    def is_done(self):
        return self.has_task() and (self.duration == 0)

    def clear_task(self):
        task = self.task
        self.task = None
        self.duration = 0
        return task


def get_pending_tasks(dependencies, unassigned_tasks):
    if not dependencies:
        return unassigned_tasks

    all_options = []
    for x in dependencies:
        all_options.append(x[0])
        all_options.append(x[1])
    all_options = list(set(all_options))

    this_round = []
    for step in all_options:
        my_blockers = [elem for elem in dependencies if elem[1] == step]
        if not my_blockers:
            this_round.append(step)

    this_round = sorted(this_round)

    return this_round


def solve_part2(start):
    dependencies = load_inputs(7)
    # dependencies = load_test()

    working = []
    unassigned_tasks = []
    for x in dependencies:
        unassigned_tasks.append(x[0])
        unassigned_tasks.append(x[1])
    all_tasks = list(set(unassigned_tasks))
    unassigned_tasks = list(set(unassigned_tasks))

    workers = [Worker() for x in range(5)]
    ticks = 0

    while unassigned_tasks or list(filter(lambda x: x is not None, working)):
        # try to assign all available tasks
        for pending_task in get_pending_tasks(dependencies, unassigned_tasks):
            for worker in workers:
                if pending_task in unassigned_tasks and not worker.has_task():
                    worker.set_task(pending_task)
                    unassigned_tasks.remove(pending_task)

        working = [w.get_task() for w in workers]
        working_format = [w if w else '#' for w in working]
        print('{:03d} | working: {}'.format(ticks, working_format))

        # do work
        for worker in workers:
            worker.do_work()

        # mark finished tasks
        for worker in workers:
            if worker.is_done():
                task = worker.clear_task()
                dependencies = [x for x in dependencies if x[0] != task]

        ticks += 1

    print ticks - 1


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
