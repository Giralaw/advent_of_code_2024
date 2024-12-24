#! /usr/bin/env python3

# Advent of Code 2024 Day _

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

infile = sys.argv[1] if len(sys.argv)>=2 else '24.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
start,gates = S.split('\n\n')
#R,C = len(G),len(G[0])
#G = [[G[r][c] for c in range(C)] for r in range(R)]

ins = {}
for line in start.split('\n'):
    line = line.split(': ')
    in1 = line[0]
    val = int(line[1])
    ins[in1] = bool(val)

for line1 in gates.split('\n'):
    for line in gates.split('\n'):
        line = line.split(' ')
        in1 = line[0]
        op = line[1]
        in2 = line[2]
        out = line[4]
        if in1 in ins.keys() and in2 in ins.keys() and out not in ins.keys():
            in1 = ins[in1]
            in2 = ins[in2]
            match op:
                case "AND":
                    ret = in1 and in2
                case "OR":
                    ret = in1 or in2
                case "XOR":
                    ret = in1 ^ in2
            ins[out] = ret

for k,v in sorted(ins.items()):
    if k[0] == "z":
        sig = int(k[1:])
        p1 += v*(2**sig)

#p2: this set of wires should be able to add two binary numbers
# four pairs of gates have their output swapped
# find the four pairs such that when swapped, all binary addition works
# and return alphanumerically sorted comma separated
# list of the swapped output wires
# so need a function that given a set of wires, returns the output sum
# for a given pair of bool vals




print('p1 is ', p1)
print('p2 is ', p2)
