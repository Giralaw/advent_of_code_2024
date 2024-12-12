#! /usr/bin/env python3

# Advent of Code 2024 Day 12

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

infile = sys.argv[1] if len(sys.argv)>=2 else '12.in'
p1 = 0
p2 = 0

data = open(infile).read().strip()
G = data.split('\n')

R = len(G)
C = len(G[0])

seen = set()
plots = {}
for r in range(R):
    for c in range(C):
        if (r,c) not in seen:
            # should find all members of a plot before moving on
            plots[(r,c)] = [(r,c)]
            curr = set([(r,c)])

            while curr:
                (rr,cc) = curr.pop()
                seen.add((rr,cc))
                if rr > 0:
                    if G[rr-1][cc] == G[rr][cc] and (rr-1,cc) not in seen:
                        seen.add((rr-1,cc))
                        curr.add((rr-1,cc))
                        plots[(r,c)].append((rr-1,cc))
                if cc > 0:
                    if G[rr][cc-1] == G[rr][cc] and (rr,cc-1) not in seen:
                        seen.add((rr,cc-1))
                        curr.add((rr,cc-1))
                        plots[(r,c)].append((rr,cc-1))
                if rr < R-1:
                    if G[rr+1][cc] == G[rr][cc] and (rr+1,cc) not in seen:
                        seen.add((rr+1,cc))
                        curr.add((rr+1,cc))
                        plots[(r,c)].append((rr+1,cc))
                if cc < C-1:
                    if G[rr][cc+1] == G[rr][cc] and (rr,cc+1) not in seen:
                        seen.add((rr,cc+1))
                        curr.add((rr,cc+1))
                        plots[(r,c)].append((rr,cc+1))
    pass

# part 1 calc now we have the regions
# part 2 involves number of sides instead of perimeter

def side(r,c,grp):
    # for convex corners: check if there's a border across one axis, then if the point clockwise from that isn't in the group, add a side
    # for concave corners: check if border across a dimension, then if BOTH points
    # so there is sort of a symmetry here, just the diagonal term point doesn't matter if the adjacent one isn't in the group

    side = 0
    if (r-1,c) not in grp and (r,c+1) not in grp:
        side += 1
    if (r,c+1) not in grp and (r+1,c) not in grp:
        side += 1
    if (r+1,c) not in grp and (r,c-1) not in grp:
        side += 1
    if (r,c-1) not in grp and (r-1,c) not in grp:
        side += 1

    if (r-1,c) not in grp and (r,c+1) in grp and (r-1,c+1) in grp:
        side += 1
    if (r,c+1) not in grp and (r+1,c) in grp and (r+1,c+1)  in grp:
        side += 1
    if (r+1,c) not in grp and (r,c-1) in grp and (r+1,c-1) in grp:
        side += 1
    if (r,c-1) not in grp and (r-1,c) in grp and (r+-1,c-1) in grp:
        side += 1
    return side


for k,v in plots.items():
    per = 0
    sides = 0
    for (r,c) in v:
        if (r-1,c) not in v:
            per += 1
        if (r, c-1) not in v:
            per += 1
        if (r+1,c) not in v:
            per += 1
        if (r,c+1) not in v:
            per += 1

        a = side(r,c,v)
        if a > 0:
            #print(f"{r=},{c=},{a=}")
            pass
        sides += a

    p1 += per*len(v)
    p2 += sides*len(v)

print('p1 is ', p1)
print('p2 is ', p2)