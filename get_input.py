#! /usr/bin/env python3

# Input file fetching tool courtesy of Jonathan Paulson

import argparse
import subprocess
import sys
import pip._vendor.requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.

# 2024 cookies
SESSION = '53616c7465645f5f9f93395a1175872ddaee7036a348e4573e9874a72cb0dc789bf731007aabe22252d3b05845a31f39c4a2febadf771523e375e78949a986aa'

useragent = 'https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py by jonathanpaulson@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2024)
parser.add_argument('--day', type=int, default=13)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}"' #-A {useragent} commented out
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
