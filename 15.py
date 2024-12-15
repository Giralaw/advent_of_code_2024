#! /usr/bin/env python3

# Advent of Code 2024 Day 15

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]
# neighbor directions ordered to go clockwise start from right in a
# list-of-lists grid (i.e. (0,0) is top left corner)
adj8 = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

import sys, string, math, time, re, itertools, numpy as np
from sympy import Matrix
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode
sys.setrecursionlimit(10**6)

infile = sys.argv[1] if len(sys.argv)>=2 else '15.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
G,rls = S.split('\n\n')
G= G.split('\n')
G = [list(s) for s in G]
R,C = len(G), len(G[0])

cd = {">": (0,1), "v": (1,0), "<": (0,-1), "^": (-1,0)}
rls = ''.join(rls.split('\n'))

def solve(A,part2):
    G = deepcopy(A)
    ans = 0
    R, C = len(G), len(G[0])

    # make big grid, adjust C
    if part2:
        bg = deepcopy(G)
        for r in range(R):
            bg[r] = []
            for c in range(C):
                if G[r][c] == "#":
                    bg[r].append("##")
                if G[r][c] == "O":
                    bg[r].append("[]")
                if G[r][c] == "@":
                    bg[r].append("@.")
                if G[r][c] == ".":
                    bg[r].append("..")
        C *= 2 
        bg = [''.join(row) for row in bg]
        bg = [[bg[i][j] for j in range(C)] for i in range(R)]
        G = bg
    
    # find robot initial position
    for r in range(R):
        for c in range(C):
            if G[r][c] == "@":
                sr,sc = r,c
    
    # iterate through motions
    for rl in rls:
        ok = True
        dr,dc = cd[rl]
        
        seen = deque()

        gp = deque()
        gp.append((sr,sc))

        # BFS to find all boxes that will be moved
        while gp:
            rr,cc = gp.popleft()
            if (rr,cc) in seen:
                continue
            seen.append((rr,cc))
            
            r2,c2= rr+dr,cc+dc
            new = G[r2][c2]
            if new == "O":
                gp.append((r2,c2))
            if new == "[":
                gp.append((r2,c2))
                gp.append((r2,c2+1))
            if new == "]":
                gp.append((r2,c2))
                gp.append((r2,c2-1))
            if new == "#":
                ok = False
                break
            if new == ".":
                continue
        
        # if ok action, move all boxes appropriately
        if ok == True:
            # need to do it in reverse fashion to avoid double stepping
            #soln: change to deque
            for (r2,c2) in reversed(seen):
                G[r2+dr][c2+dc] = G[r2][c2]
                G[r2][c2] = '.'
            sr,sc = sr+dr,sc+dc
        
    for r in range(R):
        for c in range(C):
            if G[r][c] == "O" or G[r][c] == "[":
                ans += 100*r+c
    return ans

def viz(G):
    print('\n'.join(''.join(sub) for sub in G))

p1 = solve(G,False)
p2 = solve(G,True)

print('p1 is ', p1)
print('p2 is ', p2)
