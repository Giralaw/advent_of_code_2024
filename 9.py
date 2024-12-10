#! /usr/bin/env python3

# Advent of Code 2024 Day 9

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]

dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]

import string, math, time, re, itertools, numpy as np
from copy import deepcopy
from collections import defaultdict, deque
import functools
#from aoc_tools import * # regex module doesn't work with pypy
from statistics import mode, multimode

data = open('9.in').read().strip()
G = [int(a) for a in data]
ref = deepcopy(G)

p1 = 0
p2 = 0


sz = len(G)
id_f = (len(G)-1)//2
id_i = 0

i = 0
pos = 0
j = sz-1

blk = G[j]

drv = []

while id_i < id_f:
    # block has actual data to use
    if i % 2 == 0:
        curr = G[i]
        while curr > 0:
            #print(pos,id_i)
            p1 += pos*id_i
            pos += 1

            #print(id_i, end= '')
            drv.append(str(id_i))
            curr = curr -1
        id_i += 1
        i += 1
        if id_i >= id_f:
            break
    else:
        # how much space we have to fill with end data
        spc = G[i]
        while spc > 0:
            if blk > 0:
                #print(pos,id_f)
                p1 += pos*id_f
                pos += 1

                #print(id_f, end= '')
                drv.append(str(id_f))
                blk -= 1
                spc -= 1
            else:
                id_f -= 1
                j -= 2
                blk = G[j]
        i += 1
    #print(i,j)

# finishing the last block
while blk > 0:
    p1 += (pos)*id_f
    pos += 1
    blk -=1


# __________
# part 2-- contiguous file movement
# just gonna go from scratch


# visualization array for debugging
tot = 0
for a in ref:
    tot += a

vis = ['.' for _ in range(tot)]

sz = len(G)
id_f = (len(G)-1)//2
id_i = 0

i = 1

j = sz-1

blk = G[j]

drv = []

while id_f > 0:
    #print(id_f)
    # how much space we have available to fill with end data

    i = 1
    pos = G[0]

    while i < j:
        pos += (ref[i] - G[i])
        spc = G[i]
        blk = G[j]
        #print(id_f, pos, spc,blk)

        if spc >= blk:
            swapped = True
            spc -= blk
            G[i] -= blk
            G[j] = 0

            while blk > 0:
                vis[pos] = str(id_f)
                p2 += pos*id_f
                pos += 1
                blk -= 1

            id_f -= 1
            j -= 2
            blk = G[j]
            break


        else:
            swapped = False
            pos += G[i+1] + G[i]
            i += 2

    # ah, beautiful. Just needed to add a flag to avoid redundant decrementing
    # in the case where I had successfully swapped. Probably a more elegant way to do this,
    # but glad I was able to parse my algorithm's logic clearly enough to identify that.
    if not(swapped):
        id_f -= 1
        j -= 2
        blk = G[j]
        swapped = True

pos = 0
i = 0


while i < sz-1:
    curr = G[i]
    if curr == 0:
        pos += ref[i]
    while curr > 0:
        vis[pos] = str(id_i)
        p2 += pos*id_i
        pos += 1


        curr = curr -1
    id_i += 1

    pos += ref[i+1]
    i += 2

print("".join(vis))

print('p1 is ', p1)
print('p2 is ', p2)