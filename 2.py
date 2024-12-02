#! /usr/bin/env python3

# Advent of Code 2024 Day 2

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('2.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

for line in lines:

    safe = 1
    words = line.split()
    words = [int(word) for word in words]

    if True:

        # tolerances
        # set to 0 to get part 1

        # omg i'd initialize the safe = 1 flag here when i needed to do it inside the for loop
        tol = 1

        for i in range(len(words)):
            safe = 1
            words_tol = words[:i] + words[i+tol:]
            print(words_tol)

            if not(words_tol == sorted(words_tol) or words_tol == sorted(words_tol,reverse=True)):
                print("wrongie", words_tol)
                safe = 0
            for j in range(len(words_tol)-1):
                diff = abs(words_tol[j+1] - words_tol[j])
                if not(0 < diff < 4):
                    print(words_tol)
                    safe = 0
            if safe == 1:
                break
                
        if safe == 1:
            p2 += 1
            
            # print("safe:", line)
        else:
            print("unsafe:", line)



print('p1 is ', p1)
print('p2 is ', p2)