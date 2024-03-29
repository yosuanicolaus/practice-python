#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


# TLE on tc7


def solve():
    n, m = map(int, input().split())
    replace_costs = list(map(int, input().split()))
    overtake_costs = list(map(int, input().split()))
    final_cost = replace_costs[m - 1]

    def get_min_cost(from_range, to_range):
        min_cost = 0
        for i in range(from_range, to_range):
            min_cost += min(replace_costs[i], overtake_costs[i])
        return min_cost

    # get cheapest final_cost
    for i in range(m - 1):
        temp_cost = replace_costs[i] + get_min_cost(i + 1, m)
        final_cost = min(final_cost, temp_cost)

    # get journey (just to before the max allowed) cost
    journey_cost = get_min_cost(m, n)
    return final_cost + journey_cost


def main():
    t = int(input())
    for _ in range(t):
        print(solve())


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input():
    return sys.stdin.readline().rstrip("\r\n")


# endregion

if __name__ == "__main__":
    main()
