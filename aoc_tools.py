from collections import deque, defaultdict, Counter
import itertools
import regex
from typing import TypeVar, Generator, Iterable, Tuple, List

#aoc_tools file - format and num+regex are from neil thistle (https://github.com/nthistle/advent-of-code/blob/master/2022/day01/aoc_tools.py). Will hopefully add more to this myself. nums() useful for now.

# this is like slightly borked because it doesn't get negative numbers
# oh well i guess
nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]