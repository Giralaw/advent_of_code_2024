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
            sr,sc = r,c
        if G[r][c] == 'E':
            er,ec = r,c

# maze nav, need modified BFS (djikstra's somehow?)
# we'll have to weight our bfs by the number of turns, so partial sort of DFS
seen = set()
path = deque()
path.append((sr,sc))

nds = defaultdict()

#print((sr,sc),(er,ec))
while path:
    found = False
    rr,cc = path.popleft()

    if (rr,cc) == (er,ec):
        found = True
        break

    seen.add((rr,cc))
   
   
    # now we add intersections that aren't necessarily T's or L's in lower priority
    for (dr,dc) in dirs2:
        r2,c2 = rr, cc
        r3,c3 = rr,cc
        while G[r2][c2] != '#':
            
            r2 += dr
            c2 += dc
            for (rrr,ccc) in ((r2-dc,c2-dr),(r2+dc,c2+dr)):
                if G[rrr][ccc] == "." and (r2,c2) not in seen:
                    #print('opt 3: adding',(r2,c2))
                    path.append((r2,c2))
                    seen.add((r2,c2))
                    nds[(r2,c2)] = (rr,cc)
    for (dr,dc) in dirs2:
        while G[r3][c3] != "#":
            r3 -= dr
            c3 -= dc
            for (rrr,ccc) in ((r3-dc,c3-dr),(r3+dc,c3+dr)):
                if G[rrr][ccc] == "." and (r3,c3) not in seen:
                    #print('opt 4: adding',(r3,c3))
                    path.append((r3,c3))                       
                    seen.add((r3,c3))
                    nds[(r3,c3)] = (rr,cc)

    for (dr,dc) in dirs2:
        #print(rr,cc,(dr,dc))
        r2,c2 = rr,cc

        # need to account for intersections
        while G[r2][c2] !=  "#":
            r2 += dr
            c2 += dc
        if (r2-dr,c2-dc) not in seen:
            #print('opt 1: adding',(r2-dr,c2-dc))
            path.append((r2-dr,c2-dc))
            seen.add((r2-dr,c2-dc))
            nds[(r2-dr,c2-dc)] = (rr,cc)
     
    for (dr,dc) in dirs2:
        #print(rr,cc,(dr,dc))
        r2,c2 = rr,cc

        # need to account for intersections
        while G[r2][c2] !=  "#":
            r2 -= dr
            c2 -= dc
        if (r2+dr,c2+dc) not in seen:
            #print('opt 2: adding',(r2+dr,c2+dc))
            path.append((r2+dr,c2+dc))
            seen.add((r2+dr,c2+dc))
            nds[(r2+dr,c2+dc)] = (rr,cc)
            
    if found:
        break
# 
# for r in range(R):
#     for c in range(C):
#         if (r,c) in seen:
#             print('O',end='')
#         else:
#             print(G[r][c],end='')
#     print('')
# # now need to retrieve path and number of turns
pos = (er,ec)

corr = []
corr.append((er,ec))
sz = 1

while pos != (sr,sc):
    #print(pos, nds[pos])
    posnew = nds[pos]
    corr.append(posnew)
    diff = abs(posnew[1]-pos[1]) +abs(posnew[0] - pos[0])
    p1 += diff
    p1 += 1000
    sz += 1
    pos = posnew
#print(sz)
#for r in range(R):
#    for c in range(C):
#        if (r,c) in corr:
#            print('O',end='')
#        else:
#            print(G[r][c],end='')
#    print('')


print('p1 is ', p1)
print('p2 is ', p2)
