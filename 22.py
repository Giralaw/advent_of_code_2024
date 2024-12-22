#! /usr/bin/env python3

# Advent of Code 2024 Day 22

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

infile = sys.argv[1] if len(sys.argv)>=2 else '22.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions

DP = {}

def evolve(num):
    if num in DP.keys():
        return DP[num]
    a = num*64
    a = ((a ^ num) % 16777216)
    a = (a//32 ^ a)% 16777216
    a = (a*2048 ^ a) % 16777216
    DP[num] = a
    return a

prices = []
dprices = []

# list of DP's storing banana sale for each quadruple change in each buyer
DP2 = []
#storing ch, val pairs
DP3 = defaultdict(int)
for _ in range(len(S.split('\n'))):
    DP2.append(defaultdict(int))

for i,line in enumerate(S.split('\n')):
    print(i)
    a = nums(line)[0]
    prices.append([a])
    dprices.append([])
    for j in range(2000):
        a = evolve(a)
        prices[i].append(a% 10)
        if j > 0:
            dprices[i].append(prices[i][j]-prices[i][j-1])
        if j > 3:
            chs = ()
            for k in range(j-4,j):
                chs = (*chs, dprices[i][k])
            if chs not in DP2[i].keys():
                DP2[i][chs] = prices[i][j]
                DP3[chs] = DP3[chs] + prices[i][j]
    p1 += a

# part 2; store ones place of each buyer
# need to find seq of dw,dx,dy,dz that maximizes bananas
# have dprices and prices to work with
# I want to brute force but feels like a bad idea
# range for each change is -9 to +9
# search space is 19**4 =~ 1,600,000
# should store result of each combo on each buyer. that'll be
# 1.6 mill * 2000
# but if a number shows up then we already know its changes
# so for each number we can store the associated number of bananas with memo
# make DP where the key is the number, and the item is (4 changes, # bananas after 4 more)

# or maybe we want to store things earlier...
all_keys = {key for d in DP2 for key in d.keys()}
best = 0

# length is 40000
print(len(all_keys))

for k,v in DP3.items():
    best = max(best,v)
p2 = best

# bulk of the time is spent in this loop, runs in ~90 sec
# maybe we can store a dict of ch,val in the first loop
#for j,key in enumerate(all_keys):
#    if j % 10000 == 0:
#        print(j)
#    opt = 0
#    for i in range(len(prices)):
#        opt += DP2[i][key]
#    best = max(opt,best)

#p2 = best

#for i,line in enumerate(S.split('\n')):
#    for j in range(4,2000):
#        pass



print('p1 is ', p1)
print('p2 is ', p2)
