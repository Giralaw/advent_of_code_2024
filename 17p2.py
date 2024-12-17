#! /usr/bin/env python3

# Advent of Code 2024 Day 17

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

infile = sys.argv[1] if len(sys.argv)>=2 else '17.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
G = S.split('\n')
R,C = len(G),len(G[0])

reg,prog = S.split('\n\n')
vals = nums(reg)
A,B,C = vals
prog = nums(prog)

i = 0

# A must be greater than or equal to 8**15
# and less than 8**16
# by manual inspection (each term in program correlates
# to an additional digit in the base 8 
# representation--16 instrs in program)

#8**15=  35184372088832
# need to go from this to soln in reasonable timeframe

guess = 8**15

while guess < 8**16:
    A = guess
    out = []
    
    #hardcoded instances of the general computer design
    #because I thought that might lead to a notable speedup.
    # it doesn't; that's not how time complexity works
    # both programs take ~2 seconds
    while A != 0:
        B = A % 8
        B = int(bin(B),2) ^ int(bin(2),2)
        C = A//(2**B)
        B = int(bin(B),2) ^ int(bin(C),2)
        A = A//8
        B = int(bin(B),2) ^ int(bin(7),2)
        out.append(B % 8)
    
    if out == prog:
        print('found!')
        print(guess,'\n')
        break
    
    match = 0
    for i,ch in enumerate(out):
        if out[i:] == prog[i:]:
            match += 1
    if match >= 12:
        dx = 1
    #print('guess:',guess, match)
    #print(out)
    
    # this works for range of options: setting top
    # power at 11,12 ,or 13
    # (and adjusting match accordingly)
    if match < 13:
        dx = 8**(12-match)
    guess += dx

if guess >= 8**16:
    print('failed! Try smaller dx')
else:
    p2 = guess
print('p2 is ', p2)
