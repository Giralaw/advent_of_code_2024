#! /usr/bin/env python3

# Advent of Code 2024 Day 21

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

infile = sys.argv[1] if len(sys.argv)>=2 else '21.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
# control a robot controlling a robot controlling a robot pressing keypad
#+---+---+---+
#| 7 | 8 | 9 |
#+---+---+---+
#| 4 | 5 | 6 |
#+---+---+---+
#| 1 | 2 | 3 |
#+---+---+---+
#    | 0 | A |
#    +---+---+


#    +---+---+
#    | ^ | A |
#+---+---+---+
#| < | v | > |
#+---+---+---+
# hand always starts at the A button, so bottom right in first case
# top right in the other two(/three)
# recursive outward; get first robot button presses, then next
# and so on
# so for 029A, best options are
# L pr U pr UUR pr DDD pr
# or L pr U pr RUU pr DDD pr
# after the first layer, since you have to go to the A every time
# order doesn't really matter, just have to avoid the corners
G1 = [[7,8,9],[4,5,6],[1,2,3],["B",0,"A"]]
G2 = [["B","^","A"],["<","v",">"]]

R1 = len(G1)
C1 = len(G1[0])
R2 = len(G2)
C2 = len(G2[0])
locs1 = defaultdict()
for r in range(R1):
    for c in range(C1):
        locs1[str(G1[r][c])] = (r,c)
locs2 = defaultdict()
for r in range(R2):
    for c in range(C2):
        locs2[str(G2[r][c])] = (r,c)

# make a function that travels each path on that board
# i really want to bfs
# let's first assume we're dealing with the first case

# order does matter!

#270422 too high
def get_seq1(seq):
    seq = "A"+seq
    #print(seq)
    ref = locs1
    out = ""
    for i in range(len(seq)-1):
        s = seq[i]
        f = seq[i+1]
        dr = ref[f][0]-ref[s][0]
        dc = ref[f][1]-ref[s][1]

        #match s+f:
        #    case 'A1':

        #print(dr,dc)
        if ref[s][0] == 3 and ref[f][1] == 0:
            out += "^"
            dr += 1
            if dr < 0:
                out += "^"*abs(dr)
            if dc < 0:
                out += "<"*abs(dc)
        elif ref[f][0] == 3 and ref[s][1] == 0:
            out += ">"
            dc -= 1
            if dc > 0:
                out += ">"*dc
            if dr > 0:
                out += "v"*dr
        else:
            if dr > 0:
                out += "v"*dr
            if dc > 0:
                out += ">"*dc
            if dc < 0:
                out += "<"*abs(dc)
            if dr < 0:
                out += "^"*abs(dr)
        out += "A"
        #print(out)
    return out

# maybe need a third version for outermost keypad?
def get_seq2(seq):
    #print(seq)
    #print(locs1["3"])
    seq = "A"+seq
    #print(seq)
    ref = locs2
    out = ""
    for i in range(len(seq)-1):
        s = seq[i]
        f = seq[i+1]
        dr = ref[f][0]-ref[s][0]
        dc = ref[f][1]-ref[s][1]
        match s+f:
            case 'A<':
                out += "v<<"
            case '<A':
                out +=  ">>^"
            case 'Av':
                out += "<v"
            case 'vA':
                out += ">^"
            case '^<':
                out += "v<"
            case '<^':
                out += ">^"
            case '^>':
                out += "v>"
            case '>^':
                out += "<^"
            case _:
                if dc > 0:
                    out += ">"*dc
                if dr > 0:
                    out += "v"*dr
                if dc < 0:
                    out += "<"*abs(dc)
                if dr < 0:
                    out += "^"*abs(dr)
        out += "A"
    return out

# this function may be obsolete, looks like get_seq2 works just as well
def get_seq3(seq):
    seq = "A"+seq
    ref = locs2
    out = ""
    for i in range(len(seq)-1):
        s = seq[i]
        f = seq[i+1]
        dr = ref[f][0]-ref[s][0]
        dc = ref[f][1]-ref[s][1]
        match s+f:
            case 'A<':
                out += "<v<"
            case '<A':
                out +=  ">^>"
            case 'Av':
                out += "<v"
            case 'vA':
                out += ">^"
            case '^<':
                out += "v<"
            case '<^':
                out += ">^"
            case '^>':
                out += "v>"
            case '>^':
                out += "<^"
            case _:
                if dc > 0:
                    out += ">"*dc
                if dr > 0:
                    out += "v"*dr
                if dc < 0:
                    out += "<"*abs(dc)
                if dr < 0:
                    out += "^"*abs(dr)
        out += "A"
    return out


mvs = {"<" : (0,-1), "v" : (1,0), ">" : (0,1), "^" : (-1,0)}
def backsolve(code):
    # start at A
    r,c = 0,2
    out = ""
    ref = locs2
    
    for e in code:
        if e == "A":
            out += G2[r][c]
        else:
            dr = mvs[e][0]
            dc = mvs[e][1]
            r += dr
            c += dc
    return out

DP = {}
def cost(pair,chn):
    if (pair,chn) in DP.keys():
        return DP[pair,chn]
    
    add = len(

# backsolving jpaul solutions to compare output
#query = "<v<A>^>AAA<vA<A>^>AAvAA^<A>A<vA^>A<A>A<vA^>A<A>A<v<A>A^>AAA<Av>A^A"
#query = "<AAAv<AA>>^AvA^AvA^A<vAAA^>A"

S = S.split('\n')

numpads = 12

# too slow for np = 25, need to come up with a method to cache/DP this up
for line in S:
    a = get_seq1(line)
    for _ in range(numpads):
        a = get_seq2(a)
    code = int(nums(line)[0])
    
    print(code)
    print(len(a))
    p1 += len(a)*code
    #print('\n')
    #a2 = backsolve(query)
    #a1 = backsolve(a2)
    #print(f"compiling\n{query} gives\n{a2}")
    #print(f"compiling\n{a2} gives\n{a1}")

    pass

print('p1 is ', p1)
print('p2 is ', p2)
