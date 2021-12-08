#this is part 2 solution, unfortunately not mine :( but it is so amazing that I left it here for learning reasons, to revisit and see how sweet it can be:
from itertools import *
z = 0
while s := input().strip():
    a, b = s.split(' | ')
    l = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    for i in permutations('abcdefg'):
        d = {i:j for i, j in zip(i, 'abcdefg')}
        f = lambda x: ''.join(sorted([d[j] for j in x]))
        if all(f(j) in l for j in a.split()):
            z += int(''.join(str(l.index(f(j))) for j in b.split()))
            break
print(z)