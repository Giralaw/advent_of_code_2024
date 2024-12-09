#! /usr/bin/env python3

# Advent of Code 2024 Day 8

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
#from aoc_tools import * # regex module doesn't work with pypy
from statistics import mode, multimode

data = open('8.in').read().strip()
G = data.split('\n')

p1 = 0
p2 = 0

# this option assumes each line should be treated separately

# we want to make a dictionary, where each character type corresponds to a list of
# doublets--that is, each location of that frequency

freq = defaultdict(list)

R = len(G)
C = len(G[0])
nds = set()

for r in range(R):
    for c in range(C):
        a = G[r][c]
        if a != '.':
            freq[a].append((r,c))
    pass

# now we find all the antinodes and if they're within confines, add them to the set
# missing (7,0) in example set


for k,v in freq.items():
    sz = len(v)
    for i, pt1 in enumerate(v):
        for pt2 in v[i+1:]:
            # get slope given two points
            dy = (pt2[1] - pt1[1])
            dx = (pt2[0]-pt1[0])

            # two possible points for each pair
            x = pt2[0]+dx
            y = pt2[1]+dy
            loc = (x,y)
            if 0 <= x < C and 0 <= y < R:
                nds.add(loc)

            x = pt1[0]-dx
            y = pt1[1]-dy
            loc = (x,y)
            if 0 <= x < C and 0 <= y < R:
                nds.add(loc)

p1 = len(nds)

# part 2 - any point exactly in line with a pair of nodes
# need to divide each dx,dy pair by its greatest common factor, then
# step by that amount until out of bounds

for k,v in freq.items():
    sz = len(v)
    for i, pt1 in enumerate(v):
        for pt2 in v[i+1:]:

            # get slope given two points
            dy = (pt2[1] - pt1[1])
            dx = (pt2[0]-pt1[0])

            # # find minimal dx, dy
            # # sooo, it turns out this was totally unnecessary, the two nodes were always
            # # as close together as they could be
            # if dy == 0:
            #     dx = 1
            # elif dx == 0:
            #     dy = 1
            # else:
            #     fac = math.gcd(dy,dx)
            #     dy = dy/fac
            #     dx = dx/fac

            x = pt1[0]
            y = pt1[1]
            loc = (x,y)
            
            while 0 <= x < C and 0 <= y < R:

                nds.add(loc)
                x = loc[0]-dx
                y = loc[1]-dy
                loc = (x,y)

            x = pt1[0]
            y = pt1[1]
            loc = (x,y)
            while 0 <= x < C and 0 <= y < R:

                nds.add(loc)
                x = loc[0]+dx
                y = loc[1]+dy
                loc = (x,y)

p2 = len(nds)

G = [list(s) for s in G]
for r in range(R):
    for c in range(C):
        a = G[r][c]
        if (r,c) in nds and a == '.':
            G[r][c] = "#"
for r in G:
    print("".join(map(str, r)))



    
# print(freq)
#print("locations are", nds)

print('p1 is ', p1)
print('p2 is ', p2)