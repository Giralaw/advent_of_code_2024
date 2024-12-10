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

sys.setrecursionlimit(10**6)

infile = sys.argv[1] if len(sys.argv)>=2 else '10.in'
p1, p2 = 0

data = open(infile).read().strip()
G = data.split('\n')
G = [[int(r) for r in c] for c in G]
R = len(G)
C = len(G[0])

A = set()
def score_p1(sr,sc, val):
    global A
    if val == 0:
        A = set()

    if val == 9:
        A.add((sr,sc))

    for (dr,dc) in dirs2:
        if (0 <= sr+dr < R) and (0 <= sc + dc < C):
            if G[sr+dr][sc+dc] == val + 1:

                score_p1(sr+dr,sc+dc, val+1)

    if val == 0:
        return len(A)
    
# misread instructions and did the p2 problem instead, so had some ctrl-zing to figure out
# best way to get back to p2 soln without losing p1.
def score_p2(sr,sc, val):
    tot = 0
    if val == 9:
        return 1
    for (dr,dc) in dirs2:
        if (0 <= sr+dr < R) and (0 <= sc + dc < C):
            if G[sr+dr][sc+dc] == val + 1:
                tot += score_p2(sr+dr,sc+dc, val+1)
    return tot

for rr in range(R):
    for cc in range(C):
        if G[rr][cc] == 0:
            p1 += score_p1(rr,cc, 0)
            p2 += score_p2(rr,cc, 0)


print('p1 is ', p1)
print('p2 is ', p2)