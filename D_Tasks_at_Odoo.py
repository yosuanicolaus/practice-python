#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


# doesn't work (error) ... need DP?


def dp(tasks: list[int], server_count: int, server_carry: int):
    if tasks == []:
        return server_count

    if server_carry < tasks[-1]:
        server_count += 1
    else:
        server_carry -= tasks[-1]

    return min(
        dp(tasks[:i] + tasks[i + 1 :], server_count, server_carry)
        for i in range(len(tasks) - 1)
    )


def solve(tasks: list[int], time: int):
    tasks.sort()
    if tasks[-1] > time:
        return -1

    handled = [False] * len(tasks)
    server_count = 0
    server_carry = 0

    return dp(tasks, server_count, server_carry)

    # for i in range(len(tasks) - 1, -1, -1):
    #     if handled[i]:
    #         continue

    #     server_count += 1
    #     handled[i] = True
    #     server_carry = time - tasks[i]

    #     # j = i - 1
    #     # while server_carry > 0 and j >= 0:
    #     #     if tasks[j] <= server_carry:
    #     #         server_carry -= tasks[j]
    #     #         handled[j] = True
    #     #     j -= 1

    # return server_count


def main():
    _, time = map(int, input().split())
    tasks = list(map(int, input().split()))
    print(solve(tasks, time))


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
