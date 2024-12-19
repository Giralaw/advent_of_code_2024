#! /usr/bin/env python3

# Advent of Code 2024 Day 16

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

infile = sys.argv[1] if len(sys.argv)>=2 else '16.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
G = S.split('\n')
R,C = len(G),len(G[0])
G = [list(s) for s in G]

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            ir,ic = r,c
        if G[r][c] == 'E':
            fr,fc = r,c

# maze nav, need modified BFS (djikstra's somehow?)
# we'll have to weight our bfs by the number of turns
# doing the whole search every time is expensive.
# can we cache our values a la DP for faster compute?

# three DP's for three source pos,dirs
DP1 = {}
DP2 = {}
DP3 = {}
def cost(sr,sc,dir,er,ec,DP):
    p = []
    heapq.heappush(p,(0,sr,sc,dir))
    while p:
        d,rr,cc,dir = heapq.heappop(p)
        
        if (rr,cc,dir) in DP.keys():
            continue
        
        DP[(rr,cc,dir)] = d
        dr,dc = dirs2[dir]
        r2,c2 = rr+dr,cc+dc
        
        if G[r2][c2] != "#":
            heapq.heappush(p,(d+1,r2,c2,dir))
        heapq.heappush(p,(d+1000,rr,cc,(dir+1)%4))
        heapq.heappush(p,(d+1000,rr,cc,(dir+3)%4))
    
    return 0

# part 2: for each point in the graph, we want to compute the best score
# to get there from start, add best score to get to fin,
# and if that's equal to the prev best from part 1 then we add that point

# we fill three dicts; we know S starts east,
# and because E is a corner we can specify it to be west or south

cost(ir,ic,1,fr,fc,DP1)
cost(fr,fc,2,ir,ic,DP2)
cost(fr,fc,3,ir,ic,DP3)

# we don't care what direction we reach E with
p1 = min(DP1[(fr,fc,dir)] for dir in range(4))

for r in range(R):
    for c in range(C):
        if G[r][c] != "#":
            for dir in range(4):
                # consider each path from the end going west or south,
                # take cheaper option
                # if that combined path is as cheap as p1,
                # that point is on a best path
                if DP1[(r,c,dir)] + min(DP2[(r,c,(dir+2)%4)],DP3[(r,c,(dir+2)%4)]) == p1:
                    p2 += 1
                    break

print('p1 is ', p1)
print('p2 is ', p2)
