#! /usr/bin/env python3

# Advent of Code 2024 Day 3

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [[-1,0],[0,1],[1,0],[0,-1]]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode

data = open('3.in').read().strip()
lines = data.split('\n')

p1 = 0
p2 = 0

# accidentally kept the line splitting whitespace command, led to time loss
# from debugging when i just needed to conjoin the input file as a single string
for line in lines:
    words = ''.join(lines)

# get list of lines where each one immediately follows a mult command. 0th index won't count
words = words.split('mul(')

# part 2, add substring finder -- boolean array of enabled or disabled instructions
does = []
for i,word in enumerate(words):
    if i == 0:
        does.append(True)
        continue
    rev = word[::-1]
    dis = "don't()"[::-1]
    en = "do()"[::-1]


    # casework:

    # case 1: both commands appear in previous entry, do appears after don't
    if 0 <= rev.find(en) < rev.find(dis):
        does.append(True)
        print(rev)
    # case 2: neither command appears in previous entry
    elif rev.find(en) == -1 and rev.find(dis) == -1:
        does.append(does[i-1])
    # case 3: disable only in previous entry
    elif rev.find(en) == -1 and rev.find(dis) >= 0:
        does.append(False)
    # only remaining case: enable only in previous entry
    else:
        does.append(True)
        if rev.find(dis) >=0:
            print(rev[::-1])


for j, word in enumerate(words[1:]):
    valid = False

    #find the first right parenthesis, care only about the substring before that point
    for i in range(len(word)):
        if word[i] == ')':
            word = word[:i]
            valid = True
            break
    
    if valid == True:
        word = word.split(',')
        # checking correct syntax for the two entries in the mul(__) command
        if len(word) == 2 and word[0].isdigit() and word[1].isdigit():
            if does[j]:
                p2 += (int(word[0]) * int(word[1]))
            if True:
                p1 += (int(word[0]) * int(word[1]))


print('p1 is ', p1)
print('p2 is ', p2)