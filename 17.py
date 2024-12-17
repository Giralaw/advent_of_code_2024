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
# less than 8**16

# got p2 working on a streamlined version,
# now will try to do it here
guess = 8**15

p1_solved = False
while guess < 8**16:
    A,B,C = vals
    A = guess
    i = 0
    out = []
    
    if not(p1_solved):
        A = vals[0]
    while True:
        
        if i > len(prog)-1:
            break
        
        opc = prog[i]
        inp = prog[i+1]
        
        if inp == 4:
            arg = A
        elif inp == 5:
            arg = B
        elif inp == 6:
            arg = c
        else:
            arg = inp
        
        if opc == 0:
            A = A//(2**(arg))
        # int second arg gives base
        if opc == 1:
            B = int(bin(B),2) ^ int(bin(inp),2)
        if opc == 2:
            B = arg % 8
        if opc == 3:
            if A == 0:
                pass
            else:
                i = inp
                continue
        if opc == 4:
            B = int(bin(B),2) ^ int(bin(C),2)
        if opc == 5:
            out.append(arg % 8)
        if opc == 6:
            B = A//(2**(arg))
        if opc == 7:
            C = A//(2**(arg))
        i += 2

    if not(p1_solved):
        p1 = ','.join(str(a) for a in out)
        p1_solved = True

    if p1_solved:
        if out == prog:
            print(out)
            print('found a solution:',guess,'\n')
            p2 = guess
            break

        match = 0
        for i,ch in enumerate(out):
            if out[i:] == prog[i:]:
                match += 1
        if match >= 12:
            dx = 1
        #print('guess:', guess, match)
        #print(out)
        
        if match < 13:
            # originally had a +1 in dx terms in case of patterns
            # to make "less" composite, but
            # due to the nature of descending significance of digits,
            # I think that was unnecessary
            dx = 8**(12-match)
        guess += dx

if guess >= 8**16:
    print('failed! Try smaller dx rule.')


print('p1 is ', p1)
print('p2 is ', p2)
