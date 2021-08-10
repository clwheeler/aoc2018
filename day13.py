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

def load_test_file():
    inputs = []
    # parse input data
    with open('day{}_testinput.txt'.format(13), 'r') as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs


FACING = ["<", "^", ">", "v"]
TURN = ["L", "S", "R"]

class Cart(object):
    xpos = 0
    ypos = 0
    facing = 0
    turn = 0

    def __init__(self, x, y, facing):
        self.xpos = x
        self.ypos = y
        self.facing = FACING[facing]
        self.turn = 0

    def __str__(self):
        return "[{}, {}, {}, {}]".format(self.xpos, self.ypos, self.facing, TURN[self.turn])

    def pos(self):
        return (self.xpos, self.ypos)

    def tick(self, grid):
        next_loc = (0, 0)
        if self.facing == "<":
            next_loc = (self.xpos - 1, self.ypos)
        elif self.facing == "^":
            next_loc = (self.xpos, self.ypos - 1)
        elif self.facing == ">":
            next_loc = (self.xpos + 1, self.ypos)
        else:
            next_loc = (self.xpos, self.ypos + 1)

        next_pt = grid.get_at(next_loc[0], next_loc[1])

        if (self.facing == "^" and next_pt == "\\") or (self.facing == "v" and next_pt == "/"):
            self.facing = "<"
        elif (self.facing == "^" and next_pt == "/") or (self.facing == "v" and next_pt == "\\"):
            self.facing = ">"
        elif (self.facing == ">" and next_pt == "\\") or (self.facing == "<" and next_pt == "/"):
            self.facing = "v"
        elif (self.facing == ">" and next_pt == "/") or (self.facing == "<" and next_pt == "\\"):
            self.facing = "^"
        elif next_pt == "+":
            if self.turn == 0:
                self.facing = FACING[(FACING.index(self.facing) - 1) % 4]
            elif self.turn == 2:
                self.facing = FACING[(FACING.index(self.facing) + 1) % 4]

            self.turn = (self.turn + 1) % 3
        # else, just move

        # update own location
        self.xpos = next_loc[0]
        self.ypos = next_loc[1]


class Grid(object):

    grid = []
    carts = []
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_at(self, x, y, char):
        self.grid[y][x] = char

    def get_at(self, x, y):
        return self.grid[y][x]

    def load_grid(self, grid):
        self.grid = [[" " for x in range(self.width)] for y in range(self.height)]

        for xpos in range(self.width):
            for ypos in range(self.height):
                try:
                    self.grid[ypos][xpos] = grid[ypos][xpos]
                except:
                    pass

        for xpos in range(self.width):
            for ypos in range(self.height):
                if self.get_at(xpos, ypos) == ">":
                    self.set_at(xpos, ypos, "-")
                    self.carts.append(Cart(xpos, ypos, 2))
                elif self.get_at(xpos, ypos) == "<":
                    self.set_at(xpos, ypos, "-")
                    self.carts.append(Cart(xpos, ypos, 0))
                elif self.get_at(xpos, ypos) == "v":
                    self.set_at(xpos, ypos, "|")
                    self.carts.append(Cart(xpos, ypos, 3))
                elif self.get_at(xpos, ypos) == "^":
                    self.set_at(xpos, ypos, "|")
                    self.carts.append(Cart(xpos, ypos, 1))

    def print_grid(self):
        disp_grid = [[p for p in r] for r in self.grid]

        for cart in self.carts:
            disp_grid[cart.pos()[1]][cart.pos()[0]] = "*"

        for y in disp_grid:
            print "".join(y)

    def halt_tick(self):
        # sort carts by y.x
        sorted_carts = sorted(self.carts, key=lambda x: float("{}.{}".format(x.pos()[1], x.pos()[0])))

        for cart in sorted_carts:
            cart.tick(self)

            collision_carts = [cart for cart in sorted_carts]
            while collision_carts:
                cart = collision_carts.pop(-1)
                for cart_2 in collision_carts:
                    if cart_2.pos() == cart.pos():
                        self.print_grid()
                        raise Exception("Collide: {}".format(cart.pos()))

    def remover_tick(self, ct):
        if len(self.carts) == 1:
            raise Exception("Last cart: {}".format(str(self.carts[0])))

        # sort carts by y.x
        sorted_carts = sorted(self.carts, key=lambda x: float("{}.{}".format(x.pos()[1], x.pos()[0])))
        remove_carts = []

        for cart in sorted_carts:
            cart.tick(self)

            collision_carts = [cart for cart in sorted_carts]
            while collision_carts:
                cart_1 = collision_carts.pop(-1)
                for cart_2 in collision_carts:
                    if cart_2.pos() == cart_1.pos():
                        remove_carts.append(cart_1)
                        remove_carts.append(cart_2)

        self.carts = [cart for cart in self.carts if cart not in remove_carts]

        if len(remove_carts):
            print "removing at {}:".format(ct)
            print self.carts



def solve_part1(start):
    inputs = load_inputs(13)
    # inputs = load_test_file()
    # print inputs
    width = max([len(row) for row in inputs])
    height = len(inputs)

    print width, height

    grid = Grid(width, height)
    grid.load_grid(inputs)
    grid.print_grid()

    for x in range(10000):
        grid.halt_tick()
        # grid.print_grid()


def solve_part2(start):
    inputs = load_inputs(13)
    # inputs = load_test_file()
    # print inputs
    width = max([len(row) for row in inputs])
    height = len(inputs)

    print width, height

    grid = Grid(width, height)
    grid.load_grid(inputs)
    grid.print_grid()

    for x in range(1000000):
        grid.remover_tick(x)
        # grid.print_grid()

def run():

    start_time = time.time()
    print "Part 1:"
    # print solve_part1(0)
    print "Runtime: {} seconds".format(time.time() - start_time)

    start_time = time.time()
    print "Part 2:"
    solve_part2(0)
    print "Runtime: {} seconds".format(time.time() - start_time)


run()
