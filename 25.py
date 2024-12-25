#! /usr/bin/env python3

# Advent of Code 2024 Day 25

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]
# neighbor directions ordered to go clockwise start from right in a
# list-of-lists grid (i.e. (0,0) is top left corner)
adj8 = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

import sys, string, math, time, re, itertools, numpy as np
from sympy import Matrix
from copy import deepcopy
import heapq
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode
sys.setrecursionlimit(10**6)

infile = sys.argv[1] if len(sys.argv)>=2 else '25.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
grids = S.split('\n\n')
#R,C = len(G),len(G[0])
#G = [[G[r][c] for c in range(C)] for r in range(R)]
a = grids[0].split('\n')
R = len(a)
C = len(a[0])
print(R,C)

keys = []
locks = []
for line in grids:
    line = line.split('\n')
    if "." in line[R-1]:
        locks.append(line)
    elif "." in line[0]:
        keys.append(line)

for lock in locks:
    lockt = [list(r) for r in zip(*lock)]
    for key in keys:
        keyt = [list(r) for r in zip(*key)]
        fit = True
        for row in range(C):
            if lockt[row].count('#') + keyt[row].count('#') > R:
                fit = False
                break
        if fit:
            p1 += 1


print('p1 is ', p1)
print('p2 is ', p2)
