#! /usr/bin/env python3

# Advent of Code 2024 Day 7

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
# from aoc_tools import *
from statistics import mode, multimode

data = open('7.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

for line in lines:
    G = line.split()
    test = int(G[0][:-1])
    vals = [int(s) for s in G[1:]]

    opts = len(vals)
    tots = deque()
    tots.append(vals[0])

    i = 1
    while i < len(vals):
        j = 0
        while j < 2**(i-1):
            curr = tots.popleft()
            tots.append(curr+vals[i])
            tots.append(curr*vals[i])
            j += 1
        i += 1

    if test in tots:
        p1 += test

    # part 2 - include concatenate operator
    # smooooth

    tots = deque()
    tots.append(vals[0])
    i = 1

    while i < len(vals):
        j = 0
        while j < 3**(i-1):

            #print(tots)

            curr = tots.popleft()
            tots.append(curr+vals[i])
            tots.append(curr*vals[i])
            digs = len(str(vals[i]))
            tots.append(curr*(10**digs)+vals[i])
            j += 1

        i += 1

    if test in tots:
        #print(test)
        p2 += test
    pass


print('p1 is ', p1)
print('p2 is ', p2)