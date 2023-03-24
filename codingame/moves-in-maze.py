import sys
import math
import string
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

move = []
maze = []
sr, sc = 0, 0

for i in range(10):
    move.append(str(i))
for ch in string.ascii_uppercase:
    move.append(ch)

w, h = [int(i) for i in input().split()]
for i in range(h):
    row = input()
    if 'S' in row:
        sc = row.find('S')
        sr = i
    maze.append(list(row))

visited = set()
q: deque[tuple[int, int, int]] = deque([(0, sr, sc)])

while q:
    (i, r, c) = q.popleft()
    r %= h
    c %= w
    if maze[r][c] == '#' or \
            (r, c) in visited:
        continue

    maze[r][c] = move[i]
    visited.add((r, c))

    q.append((i+1, r-1, c))
    q.append((i+1, r, c-1))
    q.append((i+1, r, c+1))
    q.append((i+1, r+1, c))


for slist in maze:
    print(''.join(slist))
