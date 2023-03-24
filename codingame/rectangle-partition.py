import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# (OLD APPROACH, bad)
# get count of squares from just sub retangles
# loop over subrec that are not square, and try combining horizontally and vertically
# loop over all subrec and try combining diagonally

# NEW APPROACH
# get all INTERSECTIONs, try to combine right or down and check

# widths - [0, 2, 5, 10]
# heights - [0, 3, 5]

widths, heights = [0], [0]
square_count = 0

w, h, count_x, count_y = [int(i) for i in input().split()]

for i in input().split():
    x = int(i)
    widths.append(x)
widths.append(w)
for i in input().split():
    y = int(i)
    heights.append(y)
heights.append(h)


for r in range(len(heights) - 1):
    for c in range(len(widths) - 1):
        nr, nc = r+1, c+1
        while nr < len(heights) and nc < len(widths):
            vr = heights[nr] - heights[r]
            vc = widths[nc] - widths[c]
            if vr < vc:
                nr += 1
            elif vr > vc:
                nc += 1
            else:
                square_count += 1
                nr += 1
                nc += 1


print(square_count)
