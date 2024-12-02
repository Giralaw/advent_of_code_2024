#! /usr/bin/env python3

# Advent of Code 2024 Day 2

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('2.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

for line in lines:
    pass

print('p1 is ', p1)
print('p2 is ', p2)