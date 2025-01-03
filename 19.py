#! /usr/bin/env python3

# Advent of Code 2024 Day 19

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
sys.setrecursionlimit(10**8)

infile = sys.argv[1] if len(sys.argv)>=2 else '19.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()

avail, des = S.split('\n\n')
avail = avail.split(', ')
des = des.split('\n')

#DP/caching -- check if a pattern exists, then reduce to previous problem
# each one should yield number of ways

# should've made a defaultdict with True and False here
good = set()
bad = set()

# p1 -- just check if there is *A* way to make each pattern
def is_valid(gl):
    if gl in good:
        return True
    elif gl in bad:
        return False
    if gl == "":
        return True
    
    for i in range(len(gl)+1):
        if gl[:i] in avail:
            if is_valid(gl[i:]):
                good.add(gl)
                return True
    bad.add(gl)
    return False

# need a dict to save the number of ways
# technically could solve part 1 with this
# but better to keep both here for posterity
# and as this is generated, it needs good and bad
# to be preconfigured before running num_ways()

# p2 -- count number of combinations for each option
# added some extra lines so this handles is_valid()'s
# functionality as well

goodways = defaultdict()
def num_ways(gl):
    tot = 0
    if gl in bad:
        return 0
    if gl in goodways.keys():
        return goodways[gl]
    else:
        if gl == '':
            return 1
        for i in range(len(gl)+1):
            if gl[:i] in avail:
                tot +=  num_ways(gl[i:])
        if tot > 0:
            good.add(gl)
            goodways[gl] = tot
        else:
            bad.add(gl)
        return tot


# these take like, the exact same amount of time
# this way computes the three datasets within num_ways()
way1 = True
if way1:    
    for opt in des:
        a = num_ways(opt)
        if opt in goodways.keys():
            p1 += 1
            p2 += a
else:
# this way uses the first function
    p1,p2 = 0,0
    for opt in des:
        if is_valid(opt):
            p1 += 1
        p2 += num_ways(opt)

print('p1 is ', p1)
print('p2 is ', p2)
