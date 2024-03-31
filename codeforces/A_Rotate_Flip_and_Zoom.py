#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def solve():
    pass


def main():
    w, h = map(int, input().split())
    pic = []
    for _ in range(h):
        pic.append(list(input()))

    # rotate 90 degree clockwise
    new_pic = [["."] * h for _ in range(w)]
    pt_y_old, pt_x_old = 0, 0
    pt_y_new, pt_x_new = 0, h - 1

    while pt_y_new < w:
        new_pic[pt_y_new][pt_x_new] = pic[pt_y_old][pt_x_old]
        pt_y_new += 1
        pt_x_old += 1
        if pt_y_new == w and pt_x_new > 0:
            pt_y_new = 0
            pt_x_new -= 1
            pt_y_old += 1
            pt_x_old = 0

    # flip horizontally
    for pic_list in new_pic:
        pic_list.reverse()

    final_pic = [["."] * h * 2 for _ in range(w * 2)]
    for y in range(w):
        for x in range(h):
            if new_pic[y][x] == "*":
                final_pic[y * 2][x * 2] = "*"
                final_pic[y * 2][x * 2 + 1] = "*"
                final_pic[y * 2 + 1][x * 2] = "*"
                final_pic[y * 2 + 1][x * 2 + 1] = "*"

    for s in final_pic:
        print("".join(s))


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
