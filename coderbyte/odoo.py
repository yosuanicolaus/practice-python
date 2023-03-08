def ArrayChallenge(strArr):
  p1x, p1y = -1, -1
  p2s = []
  best = float('inf')
  for y in range(len(strArr)):
    for x in range(len(strArr[y])):
      dg = strArr[y][x]
      if dg == '1':
        p1x, p1y = x, y
      elif dg == '2':
        p2s.append((x, y))

  if p2s == []:
    return 0

  for p2x, p2y in p2s:
    x_dist = min(abs(p2x - p1x), abs((p2x - len(strArr) - p1x)))
    y_dist = min(abs(p2y - p1y), abs((p2y - len(strArr) - p1y)))
    dist = x_dist + y_dist
    best = min(dist, best)


# keep this function call here
best = ArrayChallenge(input())
print(best)

if str(best) in "oe4imh0xgf1c":
  print("--" + str(best) + "--")
else:
  print(best)
