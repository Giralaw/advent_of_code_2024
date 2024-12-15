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

for r in range(R):
    for c in range(C):
        if G[r][c] == "@":
            px, py = r,c
print(px,py)

cd = {">": (0,1), "v": (1,0), "<": (0,-1), "^": (-1,0)}
rls = ''.join(rls.split('\n'))

def is_valid(G,px,py,dx,dy):
    #print(len(G),len(G[0]))
    #print(px,py)
    if dx == -1:
        for i in range(px-1,0,dx):
            M[py][i] = G[py][i+1]
            a = G[py][i]
            if a == '.':
                return True
            if a == '#':
                return False
    if dy == -1:
        for i in range(py-1,0,dy):
            M[i][px] = G[i+1][px]
            a = G[i][px]
            if a == '.':
                return True
            if a == '#':
                return False
    if dx == 1:
        for i in range(px+1,C-1,dx):
            M[py][i] = G[py][i-1]
            a = G[py][i]
            if a == '.':
                return True
            if a == '#':
                return False
    if dy == 1:
        for i in range(py+1,R-1,dy):
            #print(len(G),len(G[0]))
            #print(px,i)
            M[i][px] = G[i-1][px]
            a = G[i][px]
            if a == '.':
                return True
            if a == "#":
                return False
    return False

def pr(G):
    print('\n'.join(''.join(sub) for sub in G))
    print('')

#let's try to construct our map for part 2:
ref = deepcopy(G)

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
bg = [list(s) for s in bg]

pr(bg)
#pr(G)
ref = deepcopy(G)

for rl in rls:
    #print(rl)
    #print(px,py)
    dy,dx = cd[rl]
    # want to march down from p_i to 0 if neg, up from p_i to R or C if pos
    #really need to change this deepcopy thing to be more efficient
    M = deepcopy(G)
    #print(G)
    if is_valid(G,px,py,dx,dy):
        G= deepcopy(M)
        G[py+dy][px+dx] = "@"
        G[py][px] = "."
        py += dy
        px += dx
    #pr(G)
    
    # part 2: bigger everything!
    # I'm realizing we need a recursive is_valid function...
    if is_valid(G,px,py,dx,dy
    

for r in range(R):
    for c in range(C):
        if G[r][c] == "O":
            p1 += 100*r+c

print('p1 is ', p1)
print('p2 is ', p2)
