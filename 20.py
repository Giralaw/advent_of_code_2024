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


# number of cheats that save 100 picoseconds
# get fastest valid time, then make a list of all possible ways
# and sum the number that have a cost < 100
# equal weights, can do bfs with a bool storage for cheat
# cuts are distinct by start and end, so should treat
# appropriately
# unclear whether you can break two walls or one
# could try simplifying by removing each grid point once
for r in G:
    print(''.join(r))

# want to get the reference path length
# but also get a full list of what distance each point on the path is from
# the beginning
ref = 0
seenvals = defaultdict()
path = deque()
path.append((sr,sc,0))
while path:
    r,c,d = path.popleft()
    if (r,c) in seenvals.keys():
        continue
    seenvals[(r,c)]=d

    if (r,c) == (er,ec) and ref == 0:
        ref = d

    for dr,dc in dirs2:
        r2,c2 = r+dr,c+dc
        if G[r2][c2] in "E.":
            path.append((r2,c2,d+1))
print(ref)
# now we also have seenvals, which lets us constrain
# the number of portals we make

seenvals_end = defaultdict()
path = deque()
path.append((er,ec,0))
while path:
    r,c,d = path.popleft()
    if (r,c) in seenvals.keys():
        continue
    seenvals_end[(r,c)]=d

    for dr,dc in dirs2:
        r2,c2 = r+dr,c+dc
        if G[r2][c2] in "E.":
            path.append((r2,c2,d+1))

##
## best should be (7,6)
cuts = defaultdict()
for rr in range(1,R-1):
    for cc in range(1,C-1):
        if G[rr][cc] == "#":
            G[rr][cc] = "."
            seen = set()
            path = deque()
            path.append((sr,sc,0))
            while path:
                r,c,d = path.popleft()

                if (r,c) in seen:
                    continue
                seen.add((r,c))

                if (r,c) == (er,ec):
                    break

                for dr,dc in dirs2:
                    r2,c2 = r+dr,c+dc
                    if G[r2][c2] in 'E.':
                        path.append((r2,c2,d+1))
            G[rr][cc] = "#"
            cuts[(rr,cc)] = d

improve = 2
for k,v in cuts.items():
    #print(k,v)
    if v <= ref - improve:
        p1 += 1

# part 2: one cheat, up to 20 moves, use or lose
# can't cheat out of part 1 proper solution now ig
# example only gives six seconds i guess

# oh shit this works,
# it takes time even when you're cheating
# but is it fast enough?
# how do we speed it up?
# first, we could drop any portal that takes us further away
# the fastest trick is probably to make it so portals are only added
# if they go from a point to another that is, from the original scheme
# at least 100 farther
# oh shit that would be smart
improve = 100
cheatlen = 20
ports = defaultdict(list)
# backsolve would actually be even better
# ok yes-- we want to
# A: store distance of each point from end to each point
# B for each sr,sc, we compute the dist from end to gr,gc, add the cost of the
# portal, and the dist from start to that point
# and if that sum is 100 or more less than the reference dist, then we
# add to output
for r in range(1,R-1):
    for c in range(1,C-1):
        if G[r][c] in ".SE":
            for dr in range(-cheatlen,cheatlen+1):
                for dc in range(-cheatlen+abs(dr),cheatlen+1-abs(dr)):
                    r2,c2 = r+dr,c+dc
                    if 0 < r2 < R-1 and 0 < c2 < C-1:
                        if G[r2][c2] in ".ES":
                            if seenvals[(r2,c2)] >= seenvals[(r,c)] + improve:
                                ports[(r,c)].append((r2,c2))
print("we have",ports[(7,7)])
# crap, do i need a heap for this
cuts2 = defaultdict()

seen = set()
# switching from deque to heap
p = []

# we now further ID a path by its
# start and end of cheat in addition - four more elts
# looking for (7,7) source and (7,5) goal
heapq.heappush(p,(0,sr,sc,0,0,0,0))
while p:
    d,r,c,csr,csc,cgr,cgc = heapq.heappop(p)
    if (csr,csc,cgr,cgc) in cuts2.keys():
        continue
    if (r,c,csr,csc,cgr,cgc) in seen:
        continue
    seen.add((r,c,csr,csc,cgr,cgc))

    # put something here if we already used a cheat
    if (r,c) == (er,ec):
        #print('found!', (csr,csc,cgr,cgc),d)
        #if cuts2[(csr,csc,cgr,cgc)] == 0:
        cuts2[(csr,csc,cgr,cgc)] = d
        #else:
        #    continue

    for dr,dc in dirs2:
        r2,c2 = r+dr,c+dc
        if G[r2][c2] in 'E.':
            heapq.heappush(p,(d+1,r2,c2,csr,csc,cgr,cgc))
    if csc == 0:
        for (cr,cg) in ports[(r,c)]:
            #if (r,c) == (7,7):
                #print((cr,cg))
            dist = abs(cr-r)+abs(cg-c)
            heapq.heappush(p,(d+dist,cr,cg,r,c,cr,cg))

#cuts2[(csr,csc,cgr,cgc)] = d

for k,v in cuts2.items():
    #print(k,v)
    if v <= ref - improve:
        #print(k,v)
        p2 += 1


print('p1 is ', p1)
print('p2 is ', p2)
