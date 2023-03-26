from collections import deque

graph: dict[int, set[int]] = {}
gates: set[int] = set()

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph.setdefault(n1, set())
    graph.setdefault(n2, set())
    graph[n1].add(n2)
    graph[n2].add(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.add(ei)


# game loop
while True:
    # The index of the node on which the Bobnet agent is positioned this turn
    si = int(input())
    q = deque([si])

    # run BFS from bobnet location
    while q:
        curr = q.popleft()

        for end in graph[curr]:
            if end in gates:
                print(curr, end)
                break
            q.append(end)
        else:
            continue
        break

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    # print("0 1")
