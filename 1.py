#! /usr/bin/env python3

# Advent of Code 2024 Day 1

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('1.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

left = list()
right = list()

for line in lines:
    words = line.split()
    print(words)
    left.append(int(words[0]))
    right.append(int(words[1]))

left.sort()
right.sort()
for l,r in zip(left,right):
    p1 += (abs(r - l))


for elt in left:
    p2 += (right.count(elt)*elt)

print('p1 is ', p1)
print('p2 is ', p2)