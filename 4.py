#! /usr/bin/env python3

# Advent of Code 2024 Day 4

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import sys, string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('4.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

m = len(lines)
n = len(lines[0])


rev = lines[::-1]
for i in range(len(rev)):
    rev[i] = rev[i][::-1]

lines1 = lines
ords = [lines1, rev]

for lines in ords:
    for i, cc in enumerate(lines):
        for j,rr in enumerate(cc):
            if rr == 'X':
                if j < n-3:
                    if cc[j+1] == 'M' and cc[j+2] == 'A' and cc[j+3] == 'S':
                        p1 += 1
                        print("(0,1)", i, j)
                if i < n-3:
                    if lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
                        p1 += 1
                        print("(1,0)", i, j)
                    if j < n-3:
                        if lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                            p1 += 1
                            print("(1,1)", i, j)

                # main bug was off by one error here (originally did i > 3 smh)
                if i > 2 and j < n-3:
                    if lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
                        p1 += 1
                        print("(-1,1))", i, j)


# part 2: X-MAS
# won't bother with reverse chart here methinks
lines = ords[0]
for i, cc in enumerate(lines):
    for j,rr in enumerate(cc):

        if lines[i][j] == 'A' and (0 < i < n-1) and (0 < j < m-1):
            

            # horizontal vertical case - EDIT: apparently the verti-horiz equivalent didn't count.
            # I feel like that was a little ambiguous dueto rotation, but I guess they would have said it could be a t shape.
            # print(lines[i][j-1:j+2])
            # if lines[i][j-1:j+2] == 'MAS' or lines[i][j-1:j+2] == 'SAM':
            #     if (lines[i-1][j] == 'M' and lines[i+1][j] == 'S') or (lines[i-1][j] == 'S' and lines[i+1][j] == 'M'):
            #         p2 +=1

            # diagonal case
            if ((lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') or (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M')) \
            and ((lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S') or (lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M')):
                p2 +=1
    

print('p1 is ', p1)
print('p2 is ', p2)