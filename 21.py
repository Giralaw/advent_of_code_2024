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
def get_seq1(seq,orig):
    seq = "A"+seq
    #print(seq)
    if orig:
        ref = locs1
    else:
        ref = locs2
    out = ""
    for i in range(len(seq)-1):
        s = seq[i]
        f = seq[i+1]
        dr = ref[f][0]-ref[s][0]
        dc = ref[f][1]-ref[s][1]
        #print(dr,dc)
        if ref[s][0] == 3 and dr != 0:
            while dr < 0:
                out += "^"
                dr += 1
        if ref[f][0] == 3 and dr > 1:
            while dr > 1:
                out += "v"
                dr -= 1
        if dc > 0:
            out += ">"*dc
        if dr > 0:
            out += "v"*dr
        if dc < 0:
            out += "<"*abs(dc)
        if dr < 0:
            out += "^"*abs(dr)
        out += "A"
        #print(out)
    return out

# more compare
# ref: <vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A
# you: <vA<AA>>^AvAA<^A>Av<<A>>^AvA^A<vA>^Av<<A>^A>AAvA^Av<<A>A>^AAAvA<^A>A

#980A:
# ref: v<<A>>^AAAvA^A<vA<AA>>^AvAA<^A>Av<<A>A>^AAAvA<^A>A<vA>^A<A>A
# you: v<<A>>^AAAvA^A<vA<AA>>^AvAA<^A>Av<<A>A>^AAAvA<^A>A<vA>^A<A>A

#179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#you:  v<<A>>^A<vA<A>>^AAvAA<^A>Av<<A>>^AAvA^A<vA>^AA<A>Av<<A>A>^AAAvA<^A>A


#379A:
# ref: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# you: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<vA<A>>^AAAvA<^A>A


#<v<A >>^A vA ^A <vA <A A >>^A A vA <^A >A A vA ^A <vA >^A A
# (cont) <A >A <v<A >A >^A A A vA <^A >A

# reduces to <A >A v<<A A > ^ A A > A v A A ^ A < v A A A > ^ A
#             <A>A<v<AA>^AA>AvAA^A<vAAA>^A


# reduces to ^A <<^^A >>A vvvA = 379A

# and yours is...

#456A:
#cmp v<A<AA>>^AAvA^<A>AAvA^Av<A>^A<A>Av<A>^A<A>Av<A<A>>^AAvA^<A>A


#w/  <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A

# <v<A >>^A A <vA <A >>^A A vA A <^A >A <vA >^A <A >A |<vA >^A <A >A| <v<A >A >^A| A vA <^A >A

# reduces: <A A v<A A >>^A vA ^A vA ^A <vA A >^A
# compareto<Av<AA>^A>AvA^AvA^A<vAA>^A

# reduces ^^<<A >A >A vvA = 456A
#comp to  ^<<^A>A>AvvA

#ref: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#you  <v<A>>^AvA^A<v<A>A<A>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

def get_seq2(seq,orig,inner):
    #print(seq)
    #print(locs1["3"])
    seq = "A"+seq
    #print(seq)
    if orig:
        ref = locs1
    else:
        ref = locs2
    out = ""
    for i in range(len(seq)-1):
        s = seq[i]
        f = seq[i+1]
        dr = ref[f][0]-ref[s][0]
        dc = ref[f][1]-ref[s][1]
        if inner == False:
            #print(f,dc,inner)
            #print(out)
            pass
        if dc < 0 and not inner:
            out += "<"
            dc += 1
            #print(out)
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

S = S.split('\n')        
for line in S:
    a = get_seq1(line,True)
    print(line)
    print(a)
    inside = True
    for _ in range(2):
        a = get_seq2(a,False,inside)
        inside = False
        print(a)
    code = int(nums(line)[0])
    
    print(code)
    print(len(a))
    p1 += len(a)*code
    pass

print('p1 is ', p1)
print('p2 is ', p2)
