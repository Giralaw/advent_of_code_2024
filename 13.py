#! /usr/bin/env python3

# Advent of Code 2024 Day 13

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

infile = sys.argv[1] if len(sys.argv)>=2 else '13.in'
p1 = 0
p2 = 0

data = open(infile).read().strip()
G = data.split('\n\n')
    
def solve(ax,ay,bx,by,zx,zy):

    # sympy formulation
    # gl = Matrix([
    #     [zx],
    #     [zy]])
    # mat = Matrix([
    #     [ax,bx],
    #     [ay,by]
    # ])
    # sol = mat.LUsolve(gl)

    # if all(v.is_Integer for v in sol):
    #     return 3*sol[0]+sol[1]
    # else:
    #     return 0
    
    # numpy formulation; couldn't figure out how to get the accuracy
    # on the big scientific notation numbers good enough to check if they
    # were integers, so had to use sympy instead when first solving.
    # realized i needed to use round() and also add a tol check
    # so I'll put this as my final method since numpy stuff is more basic/ubiquitous

    gl2 = np.array([
    [zx],
    [zy]])
    mat2 = np.array([
        [ax,bx],
        [ay,by]
    ])
    inv = np.linalg.solve(mat2, gl2)

    tol = 1e-2
    dx = abs(inv[0,0]-round(inv[0,0]))
    dy = abs(inv[1,0] - round(inv[1,0]))

    if dx < tol and dy < tol:
        inp =(round(inv[0,0]),round(inv[1,0]))
        return 3*inp[0]+inp[1]
    else:
        return 0

for line in G:
    # should've used the nums() function from nthistle's aoc tools
    a,b,c = line.split('\n')
    a = a.split()
    b = b.split()
    c = c.split()
    ax,ay = int(a[2][2:-1]),int(a[3][2:])
    bx,by = int(b[2][2:-1]),int(b[3][2:])
    przx, przy = int(c[1][2:-1]),int(c[2][2:])

    tkn = 0
    for i in range(100):
        for j in range(100):
            if (i*ax+j*bx,i*ay+j*by) == (przx,przy):
                newtkn = 3*i + j
                if newtkn < tkn or tkn == 0:
                    tkn = newtkn
    p1 += tkn

    przx = przx + 10000000000000
    przy = przy + 10000000000000
    p2 += solve(ax,ay,bx,by,przx,przy)



print('p1 is ', p1)
print('p2 is ', p2)
