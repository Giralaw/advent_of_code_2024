#! /usr/bin/env python3

# Advent of Code 2024 Day 23

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

infile = sys.argv[1] if len(sys.argv)>=2 else '23.in'
p1 = 0
p2 = 0

S = open(infile).read().strip()
#grid conditions
G = S.split('\n')
#R,C = len(G),len(G[0])
#G = [[G[r][c] for c in range(C)] for r in range(R)]


# first we make our graph (an adjacency dict)
# and a list of all vertices
verts = set()
edges = defaultdict(list)
for line in S.split('\n'):
    a,b = line.split('-')
    edges[a].append(b)
    edges[b].append(a)
    verts.add(a)
    verts.add(b)

seen = set()
ans = 0
for edge in edges.keys():
    for v in edges[edge]:
        for y in edges[v]:
            if y != edge:
                if edge in edges[y]:
                    if edge[0] == 't' or v[0] == 't' or y[0] == 't':
                        seen.add(frozenset((edge,v,y)))
p1 = len(seen)


# part 2: find the largest set of computers all connected to each other
# e.g. complete graph

# apparently this is the algorithm that finds all maximal
# cliques (e.g. complete subgraphs) in a graph (found from google)
cliques = set()
def BronKerbosch1(R, P, X):
    if len(P) == 0 and len(X) == 0:
        cliques.add(frozenset(R))

    Ptemp = deepcopy(P)
    for v in Ptemp:
        BronKerbosch1(R.union({v}), P.intersection(set(edges[v])), X.intersection(set(edges[v])))
        P.remove(v)
        X.add(v)
    return 0

BronKerbosch1(set(), verts, set())
best = max(len(clique) for clique in cliques)

for clique in cliques:
    if len(clique) == best:
        sol = clique
        break

sol = sorted(sol)
p2 = ','.join(e for e in sol)


print('p1 is ', p1)
print('p2 is ', p2)
