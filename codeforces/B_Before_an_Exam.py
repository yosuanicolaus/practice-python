#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def solve(sumtime: int, min_times: list[int], max_times: list[int]):
    ans = []
    remaining = sumtime

    for min_time in min_times:
        ans.append(min_time)
        remaining -= min_time

    i = 0
    while remaining > 0:
        capacity = max_times[i] - min_times[i]
        if remaining > capacity:
            ans[i] = max_times[i]
            remaining -= capacity
        else:
            ans[i] = min_times[i] + remaining
            break
        i += 1

    return " ".join(map(str, ans))


def main():
    d, sumtime = map(int, input().split())
    min_times = []
    max_times = []
    sum_min = 0
    sum_max = 0

    for _ in range(d):
        min_t, max_t = map(int, input().split())
        sum_min += min_t
        sum_max += max_t
        min_times.append(min_t)
        max_times.append(max_t)

    if sumtime < sum_min or sumtime > sum_max:
        print("NO")
    else:
        print("YES")
        print(solve(sumtime, min_times, max_times))


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
