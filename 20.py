#! /usr/bin/env python3

# Advent of Code 2024 Day 20

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

infile = sys.argv[1] if len(sys.argv)>=2 else '20.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
G = S.split('\n')
R,C = len(G),len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]

for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            sr,sc = r,c
        if G[r][c] == "E":
            er,ec = r,c

#BFS to get distance of all other points from a point
def ref_vals(distdict,ir,ic):
    path = deque()
    path.append((ir,ic,0))
    while path:
        r,c,d = path.popleft()
        if (r,c) in distdict.keys():
            continue
        distdict[(r,c)]=d

        for dr,dc in dirs2:
            r2,c2 = r+dr,c+dc
            if G[r2][c2] in "ES.":
                path.append((r2,c2,d+1))


def solve(save,cheat):
    ans = 0
    ports = defaultdict(list)

    # first, for each point on the map, we make a list of all
    # the points on the map
    for r in range(1,R-1):
        for c in range(1,C-1):
            if G[r][c] in ".SE":
                for dr in range(-cheat,cheat+1):
                    for dc in range(-cheat+abs(dr),cheat+1-abs(dr)):
                        r2,c2 = r+dr,c+dc
                        if 0 < r2 < R-1 and 0 < c2 < C-1:
                            if G[r2][c2] in ".ES":
                                # surprisingly, doesn't seem to make a timing diff
                                # if we use seenvals vs seenvals_end here
                                if seenvals[(r2,c2)] >= seenvals[(r,c)] + save:
                                    ports[(r,c)].append((r2,c2))
    
    # now we go through every portal pair and see if the combined distance of
    # source->portal entrance, portaldist, and portal exit->goal
    # saves us at least the desired number of steps
    ref = seenvals[(er,ec)]
    for k,v in ports.items():
        cpr,cpc = k
        for (gr,gc) in v:
            tot = abs(gr-cpr) + abs(gc - cpc) + seenvals[(cpr,cpc)] + seenvals_end[(gr,gc)]
            if tot <= ref - save:
                ans += 1
    return ans

# first we make dictionaries of the distance of each point from start and from end
seenvals = defaultdict()
seenvals_end = defaultdict()

ref_vals(seenvals,sr,sc)
ref_vals(seenvals_end,er,ec)

p1 = solve(100,2)
p2 = solve(100,20)


print('p1 is ', p1)
print('p2 is ', p2)
