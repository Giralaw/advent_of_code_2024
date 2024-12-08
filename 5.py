#! /usr/bin/env python3

# Advent of Code 2024 Day 5

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
# from aoc_tools import *
from statistics import mode, multimode

start = time.time()

data = open('5.in').read().strip()
rules, pages = data.split('\n\n')

p1 = 0
p2 = 0

instr = []

rules = rules.split('\n')
for rule in rules:
    instr.append(tuple(rule.split("|")))


pages = pages.split('\n')
# this option assumes each line should be treated separately

corr = 0
incorr = 0
fixed = 0

#noice
for line in pages:
    ok = True
    words = line.split(",")
    pairs = []

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            pairs.append((words[i],words[j]))
    for a in pairs:
        if (a[1],a[0]) in instr:
            ok = False

    # part 1
    if ok == True:
        length = len(words)
        p1 += int(words[length//2])
        corr += 1

    # part 2
    else:
        incorr += 1
        fix = deepcopy(words)
        
        while(ok == False):
            ok = True

            for a in pairs:

                # rule violation, need to swap elements
                if (a[1],a[0]) in instr:
                    tmp1 = fix.index(a[1])
                    tmp2 = fix.index(a[0])
                    fix[tmp1] = a[0]
                    fix[tmp2] = a[1]

                    ok = False
                    break
            

            pairs = []

            # O(n^3), could probably be better with a hash map or some other clever data structure

            # wipes pairs list clean each time we perform a swap, and remakes list from scratch
            # defaulted to conceptual simplicity on this one
            for i in range(len(words)):
                for j in range(i+1, len(words)):
                    pairs.append((fix[i],fix[j]))
            

        if ok == True:
            fixed += 1

            length = len(words)
            #print(int(fix[length//2]))
            p2 += int(fix[length//2])

# if you want input file to be one long string instead, use this and comment prev section
#''.join(lines)

stop = time.time() - start
print('time taken is', stop)
print(corr, incorr, fixed)
print('p1 is ', p1)
print('p2 is ', p2)