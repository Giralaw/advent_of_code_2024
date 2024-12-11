#! /usr/bin/env python3

# Advent of Code 2024 Day 11

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]
# neighbor directions ordered to go clockwise start from right in a
# list-of-lists grid (i.e. (0,0) is top left corner)
adj8 = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

import sys, string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools # gives us @cache
from aoc_tools import *
from statistics import mode, multimode
sys.setrecursionlimit(10**6)

infile = sys.argv[1] if len(sys.argv)>=2 else '11.in'
p1 = 0
p2 = 0

data = open(infile).read().strip()
G = data.split('\n')
G = [int(s) for s in G[0].split()]

st = G

ref = {}
def solve(x,t):
    if (x,t) in ref:
        return ref[(x,t)]
    if t == 0:
        ret = 1
    elif x == 0:
        ret = solve(1, t-1)
    elif len(str(x)) % 2 == 0:
        spl = str(x)
        l = int(spl[0:len(spl)//2])
        r = int(spl[len(spl)//2:])
        ret = solve(l,t-1) + solve(r,t-1)
    else:
        ret = solve(2024*x,t-1)
        
    ref[(x,t)] = ret
    return ret


for i in st:
    p1 += solve(i,25)
    p2 += solve(i, 75)

print('p1 is ', p1)
print('p2 is ', p2)

# yeah the trick is just DP + store every
# (x,75) value as 1

# I knew what I needed roughly, but doubted how
# powerful it was and thought there needed
# to be some math trick as well. I'll call this a partial success.