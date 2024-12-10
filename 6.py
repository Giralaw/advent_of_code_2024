#! /usr/bin/env python3

# Advent of Code 2024 Day 6

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
# from aoc_tools import *
from statistics import mode, multimode

data = open('6.in').read().strip()
grid = data.split('\n')
grid = [list(s) for s in grid]

p1 = 0
p2 = 0

# m rows, n columns (130 x 130)
m = len(grid)
n = len(grid[0])

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "^":
            pos = (i,j)

dir = dirs2[0]
dir_id = 0
start = (pos, dir)


while (0 <= pos[0] <= m-1) and (0 <= pos[1] <= n-1):
    prev = pos
    next = (pos[0] + dir[0], pos[1]+dir[1])
    
    # leaving the mapped area
    if not(0 <= next[0] <= m-1) or not(0 <= next[1] <= n-1):
        grid[prev[0]][prev[1]] = "X"
        pos = next

    # hitting obstacle
    elif grid[next[0]][next[1]] == "#":
        dir_id = dir_id + 1
        dir = dirs2[dir_id % 4]
        print("hit barrier at", next)

    #moving forward
    else:
        pos = next
        grid[prev[0]][prev[1]] = "X"

print(pos)

for row in grid:
    for col in row:
        if col == "X":
            p1 += 1


# part 2: find how many positions a new obstruction would make an infinite loop
# yeah, i brute forced it. took like 10 minutes to run. Sue me.
# (will check out others' solns and figure out what the more streamlined
# approaches were)

# check all X substitutions for a repeated pos, dir combo against a list of previous (pos,dir), that is, "ors"

print('part 2 start')

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col in ("X","^"):
            pos = start[0]
            dir = start[1]
            dir_id = 0
            grid[i][j] = "O"
            
            # list of quadruplets (pos, orientation) to search for repetition
            ors = []

            while (0 <= pos[0] <= m-1) and (0 <= pos[1] <= n-1):

                # if we have a repetition, we have a loop, so break and go to the next X
                if (pos,dir) in ors:
                    p2 += 1
                    print(p2)
                    print("obstacle placed at", (i,j))
                    print((pos,dir))
                    break

                ors.append((pos,dir))
                prev = pos
                next = (pos[0] + dir[0], pos[1]+dir[1])
                
                # leaving the mapped area
                if not(0 <= next[0] <= m-1) or not(0 <= next[1] <= n-1):
                    break

                # hitting obstacle
                elif grid[next[0]][next[1]] == "#" or grid[next[0]][next[1]] == "O":
                    dir_id = dir_id + 1
                    dir = dirs2[dir_id % 4]
                    # print("hit barrier at", next)

                #moving forward
                else:
                    pos = next

            grid[i][j] = "X"


# for row in grid:
#     print("".join(map(str, row)))

print('p1 is ', p1)
print('p2 is ', p2)