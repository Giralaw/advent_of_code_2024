#! /usr/bin/env python3

# Advent of Code 2024 Day 18

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

infile = sys.argv[1] if len(sys.argv)>=2 else '18.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
#G = S.split('\n')
#R,C = len(G),len(G[0])
#G = [[G[r][c] for c in range(C)] for r in range(R)]

R = 71
C = 71

sr,sc = 0,0

er,ec = 70,70
i = 0
blocks = []

G = [['.' for c in range(C)] for r in range(R)]

i = 0
while True:
    br,bc = nums(S.split()[i])
    i += 1
    G[br][bc] = "#"
    path = deque()
    seen = set()

    path.append((sr,sc,0))
            
    while path:
        r,c,d = path.popleft()
        
        if (r,c) in seen:
            continue
        if not(0 <= r < R, 0 <= c < C):
            continue
        seen.add((r,c))
        if (r,c) == (er,ec):
            break
        
        for dr,dc in dirs2:
            rr,cc = r+dr,c+dc
            #print(r,c)
            if 0<= rr < R and 0 <= cc < C and G[rr][cc] == ".":
                path.append((rr,cc,d+1))
    if i == 1023:
        p1 = d

    if (er,ec) not in seen:
        break

p2 = (br,bc)

print('p1 is ', p1)
print(f'p2 is {br},{bc}')
