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

guard_id_global = 0

def parse_event(event_str):
    global guard_id_global

    re_match = re.match('\[\d+-\d+-\d+ (\d+):(\d+)] (Guard #\d+ begins shift|wakes up|falls asleep)', event_str)
    hour = re_match.group(1)
    if hour == '00':
        hour = '24'
    hour = "{}".format(int(hour) - 23)
    minute = re_match.group(2)
    type_data = re_match.group(3)
    guard_id = re.match('Guard #(\d+) begins shift', type_data)
    if guard_id:
        guard_id = guard_id.group(1)
    else:
        guard_id = guard_id_global
    guard_id_global = guard_id
    e_type = re.search('(begins shift|wakes up|falls asleep)', type_data).group(1)
    p_e = dict(e_type=e_type, hour=hour, minute=minute, guard_id=guard_id)
    return p_e

def load_test():
    return """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split('\n')

def solve_part1(start):
    inputs = load_inputs(4)
    # inputs = load_test()

    # just sort inputs as strings.
    sorted_input = sorted(inputs)

    # guard[id].minute = num_times_asleep
    guards = collections.defaultdict(lambda: [0 for x in range(2*60)])

    guard_id = 0
    sleep_from = (0, 0)
    for event in sorted_input:
        # parse event
        event_data = parse_event(event)
        # print event_data
        # handle guard ID
        if event_data["e_type"] == 'begins shift':
            guard_id = event_data["guard_id"]
        if event_data["e_type"] == 'falls asleep':
            sleep_from = (int(event_data["hour"]), int(event_data["minute"]))
        if event_data["e_type"] == 'wakes up':
            guard_state = guards[guard_id]
            sleep_till = (int(event_data["hour"]), int(event_data["minute"]))
            from_index = sleep_from[0] * 60 + sleep_from[1]
            till_index = sleep_till[0] * 60 + sleep_till[1]
            # for minute in range(event_data["hour"] * 60 + event_data["minute"]):
            for x in range(0, len(guard_state)):
                if x >= from_index and x < till_index:
                    guard_state[x] = guard_state[x] + 1

            guards[guard_id] = guard_state

    total_sleep = 0
    max_guard = 0
    for k, v in guards.iteritems():
        this_sleep = sum(v)
        if this_sleep > total_sleep:
            total_sleep = this_sleep
            max_guard = k

    # print guards[max_guard]
    # print max_guard, total_sleep

    sleep_minute = max(guards[max_guard])
    sleep_minute = guards[max_guard].index(sleep_minute) - 60

    # print sleep_minute, max_guard
    print sleep_minute * int(max_guard)

def solve_part2(start):
    inputs = load_inputs(4)
    # inputs = load_test()

    # just sort inputs as strings.
    sorted_input = sorted(inputs)

    # guard[id].minute = num_times_asleep
    guards = collections.defaultdict(lambda: [0 for x in range(2*60)])

    guard_id = 0
    sleep_from = (0, 0)
    for event in sorted_input:
        # parse event
        event_data = parse_event(event)
        # print event_data
        # handle guard ID
        if event_data["e_type"] == 'begins shift':
            guard_id = event_data["guard_id"]
        if event_data["e_type"] == 'falls asleep':
            sleep_from = (int(event_data["hour"]), int(event_data["minute"]))
        if event_data["e_type"] == 'wakes up':
            guard_state = guards[guard_id]
            sleep_till = (int(event_data["hour"]), int(event_data["minute"]))
            from_index = sleep_from[0] * 60 + sleep_from[1]
            till_index = sleep_till[0] * 60 + sleep_till[1]
            # for minute in range(event_data["hour"] * 60 + event_data["minute"]):
            for x in range(0, len(guard_state)):
                if x >= from_index and x < till_index:
                    guard_state[x] = guard_state[x] + 1

            guards[guard_id] = guard_state

    sleep_max = 0
    max_guard = 0
    for k, v in guards.iteritems():
        this_sleep = max(v)
        if this_sleep > sleep_max:
            sleep_max = this_sleep
            max_guard = k

    # print guards[max_guard]
    # print guards[max_guard].index(sleep_max) - 60, max_guard, sleep_max
    print (guards[max_guard].index(sleep_max) - 60) * int(max_guard)

def run():

    start_time = time.time()

    print "Part 1:"
    solve_part1(0)
    print "Part 2:"
    solve_part2(0)

    print "Runtime: {} seconds".format(time.time() - start_time)

run()
