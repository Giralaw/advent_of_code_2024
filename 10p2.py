#! /usr/bin/env python3

# Advent of Code 2024 Day 10

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]

# neighbor directions ordered to go clockwise start from right in a
# list-of-lists grid (i.e. (0,0) is top left corner)
adj8 = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

import sys, string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

sys.setrecursionlimit(10000000)

infile = sys.argv[1] if len(sys.argv)>=2 else '10.in'

data = open(infile).read().strip()

G = data.split('\n')

G = [[int(r) for r in c] for c in G]


R = len(G)
C = len(G[0])

p1 = 0
p2 = 0

def score_p2(sr,sc, val):
    #print(sr,sc)
    tot = 0
    if val == 9:
        return 1
    for (dr,dc) in dirs2:
        #print(val,"moving",sr+dr,sc+dc)
        if (0 <= sr+dr < R) and (0 <= sc + dc < C):
            if G[sr+dr][sc+dc] == val + 1:
                #print("newpos:", val, sr+dr,sc+dc)
                tot += score(sr+dr,sc+dc, val+1)
                #print(tot)
    return tot

for rr in range(R):
    for cc in range(C):
        if G[rr][cc] == 0:
            add = score(rr,cc, 0)
            print(rr,cc,add)
            p1 += add


print('p1 is ', p1)
print('p2 is ', p2)