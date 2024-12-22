#! /usr/bin/env python3

# Advent of Code 2024 Day 22

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

infile = sys.argv[1] if len(sys.argv)>=2 else '22.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()

#DP was a total waste of time--still needed to find
# and reference all 2000 values for each entry
def evolve(num):
    a = num*64
    a = ((a ^ num) % 16777216)
    a = (a//32 ^ a)% 16777216
    a = (a*2048 ^ a) % 16777216
    return a

prices = []
dprices = []
#storing ch, val pairs
#named it DP3 at first, but it's not actually a memo
gains = defaultdict(int)

for i,line in enumerate(S.split('\n')):
    seen = set()
    a = nums(line)[0]
    prices.append([a])
    dprices.append([])
    for j in range(2000):
        a = evolve(a)
        prices[i].append(a% 10)
        if j > 0:
            dprices[i].append(prices[i][j]-prices[i][j-1])
        if j > 3:
            chs = ()
            for k in range(j-4,j):
                chs = (*chs, dprices[i][k])
            if chs not in seen:
                seen.add(chs)
                gains[chs] = gains[chs] + prices[i][j]
    p1 += a
# part 2; store ones place of each buyer
# make dict where the key is the ch seq, and val is bananas gained for that
# switching from a dict to a set cut us down from 10 sec to 6-8
best = 0
for k,v in gains.items():
    best = max(best,v)
p2 = best

print('p1 is ', p1)
print('p2 is ', p2)
