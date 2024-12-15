#! /usr/bin/env python3

# Advent of Code 2024 Day 14

dirs1 = [(-1,1),(1,1),(1,-1),(-1,-1)]
dirs2 = [(-1,0),(0,1),(1,0),(0,-1)]
# neighbor directions ordered to go clockwise start from right in a
# list-of-lists grid (i.e. (0,0) is top left corner)
adj8 = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

import sys, string, math, time, re, itertools, numpy as np
from sympy import Matrix
from copy import deepcopy
from collections import defaultdict, deque
import functools
from aoc_tools import *
from statistics import mode, multimode
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**6)

infile = sys.argv[1] if len(sys.argv)>=2 else '14.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
G = S.split('\n')
R,C = len(G),len(G[0])
R,C = 103,101

qs = [0,0,0,0]

G = [['.' for _ in range(C)] for _ in range(R)]



pos = np.empty((1,4), dtype = int)

for line in S.split('\n'):
    # locations after 100 seconds
    # number of robots in each quadrant, multiply each occ together
    # ignore robots on the line
    px,py,vx,vy = nums(line)
    new_row = np.array([px,py,vx,vy])
    pos = np.vstack([pos, new_row])

    fin = ((100*vx+px) % C, (100*vy +py) % R)

    if fin[0] < C//2 and fin[1] < R//2:
        qs[0] += 1
    elif fin[0] > C//2 and fin[1] < R//2:
        qs[1] += 1
    elif fin[0] < C//2 and fin[1] > R//2:
        qs[2] += 1
    elif fin[0] > C//2 and fin[1] > R//2:
        qs[3] += 1

p1 = 1
for a in qs:
    p1 *= a


vel = pos[1:,2:]
pos = pos[1:,:2]

# cycle starts at 10430 apparently :/
#26 seconds to use deepcopy to generate new G
# 25 for gen from scratch, so marginally faster, not too significant
# dropping the dictionary + updates shaves 17 seconds off, so that
# costs a lot
start = time.time()
#pics = defaultdict()

# entropy function for numpy approach
def calc_entropy(pos, w,h):
    grid = np.zeros((h,w), dtype=int)
    np.add.at(grid, (pos[:,1], pos[:,0]), 1)
    counts = np.bincount(grid.flatten())
    probs = counts[counts >0] / counts.sum()
    entropy = -np.sum(probs* np.log2(probs))
    return entropy

entropies = []
for t in range(0,10500):
    pic = [['.' for c in range(C)] for r in range(R)]
    for line in S.split('\n'):
        px,py,vx,vy = nums(line)
        fin = ((t*vx+px) % C, (t*vy+py) % R)
        pic[fin[1]][fin[0]] = '#'
    if t % 1000 == 0:
        print(t)
    
    # alternate approach -- calc entropy, use numpy and mpl
    entropies.append(calc_entropy(pos,C,R))
    pos =(pos+vel) % [C,R]
    
    # this section was to find the cycle, though it wasn't
    # really integral to solving p2
    #if pic in pics.values():
    #    print('cycle starts at',t)
    #    break
    #pics[t] = pic
    
    # my first method, inspired by a comment on jpaul video, 
    # was to output to a file and then search for a long line of #
    # automated version of this is to just search for "############" in each output,
    # but kinda feels like a dangerous assumption in general
    gstr = []
    found = False
    for row in pic:
        if '############' in ''.join(row):
            p2 = t
            found = True
        gstr.append(''.join(row))
    if found == True:
        print('\n'.join(gstr))
        #break
    #time.sleep(0.1)

# entropy and matplotlib fun stuff
min_ent = min(entropies)
sol = entropies.index(min_ent)
print(f'min entropy {min_ent} is at {sol}')
indices = list(range(len(entropies)))
plt.plot(indices, entropies)
plt.text(sol,entropies[sol], f'({sol}, {entropies[sol]})',fontsize=8, ha='right')
plt.xlabel('Time')
plt.ylabel('entropy')
plt.title('Plot of entropy vs. time')
plt.show()


fin = time.time() - start
print('time for part 2 is',fin)

print('p1 is ', p1)
print('p2 is ', p2)
