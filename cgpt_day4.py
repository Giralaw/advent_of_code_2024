#! /usr/bin/env python3

# Advent of Code 2024 Day 4 CGPT solution (part 1 only)

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import sys, string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('4.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

m = len(lines)
n = len(lines[0])


rev = lines[::-1]
for i in range(len(rev)):
    rev[i] = rev[i][::-1]

lines1 = lines
ords = [lines1, rev]

# chatgpt generated solution for comparison--using directions here would've probably been more
# elegant, need to get reacclimated to that approach

word = "XMAS"

# Define a function to check if "XMAS" exists in a specific direction
def check_direction(x, y, dx, dy):
    for k in range(4):  # Length of "XMAS"
        nx, ny = x + k * dx, y + k * dy
        if not (0 <= nx < m and 0 <= ny < n) or lines[nx][ny] != word[k]:
            return False
    return True

# Iterate through the grid and check all directions
directions = [
    (0, 1),   # Horizontal (right)
    (1, 0),   # Vertical (down)
    (1, 1),   # Diagonal down-right
    (-1, 1),  # Diagonal up-right
]
for lines in ords:
    for x in range(m):
        for y in range(n):
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    p1 += 1
                    print(f"Found 'XMAS' starting at ({x}, {y}) in direction ({dx}, {dy})")

print('p1 is ', p1)
print('p2 is ', p2)