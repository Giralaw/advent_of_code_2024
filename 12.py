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
                (r2,c2) = curr.pop()
                seen.add((r2,c2))
                for (dr,dc) in dirs2:
                    rr = r2+dr
                    cc = c2+ dc
                    if 0 <= rr < R and 0 <= cc < C:
                        if G[r][c] == G[rr][cc] and (rr,cc) not in seen:
                            seen.add((rr,cc))
                            curr.add((rr,cc))
                            plots[(r,c)].append((rr,cc))
    pass

# part 1 calc now we have the regions
# part 2 involves number of sides instead of perimeter

def side(r,c,grp):
    # for convex corners: check if there's a border across one axis, then if the point clockwise from that isn't in the group, add a side
    # for concave corners: check if border across a dimension, then if BOTH points
    # so there is sort of a symmetry here, just the diagonal term point doesn't matter if the adjacent one isn't in the group

    side = 0
    for (dr,dc) in dirs1:
        if (r+dr,c) not in grp and (r,c+dc) not in grp:
            side += 1
        if (r+dr,c) not in grp and (r,c+dc) in grp and (r+dr,c+dc) in grp:
            side += 1
    return side

for k,v in plots.items():
    per = 0
    sides = 0
    for (r,c) in v:
        for (dr,dc) in dirs2:
            rr = r+dr
            cc = c+dc
            if (rr,cc) not in v:
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