#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


# WA ??


def dp(remaining_nums: list[tuple[int]], target: int) -> bool:
    if len(remaining_nums) == 2:
        return any(
            (
                remaining_nums[0][0] + remaining_nums[1][0] == target,
                remaining_nums[0][1] + remaining_nums[1][1] == target,
                remaining_nums[0][0] + remaining_nums[1][0] == target,
                remaining_nums[0][1] + remaining_nums[1][1] == target,
            )
        )

    return any(
        dp(remaining_nums[:i] + remaining_nums[i + 1 :], target)
        for i in range(len(remaining_nums))
    )


def get_flip(digit: int) -> int | None:
    digits = list(str(digit))
    new_digits = digits[::-1]

    for i, digit in enumerate(new_digits):
        if digit == "6":
            new_digits[i] = "9"
        elif digit == "9":
            new_digits[i] = "6"

    return int("".join(new_digits))


def solve(target: int, arr: list[int]):
    possible_nums = [(num, num) for num in arr]

    for i, num in enumerate(arr):
        new_num = get_flip(num)
        if new_num:
            possible_nums[i] = (num, new_num)

    return "YES" if dp(possible_nums, target) else "NO"


def main():
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(target, arr))


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
