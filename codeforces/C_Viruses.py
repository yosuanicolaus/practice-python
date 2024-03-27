#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

import bisect


def solve(project_line: list, virus_line: list) -> list:
    project_line.sort(key=lambda x: x[0])
    virus_line.sort(key=lambda x: x[0])
    virus_line_pos = [p for (p, _) in virus_line]

    for pos, pd in project_line[::-1]:
        start_idx = bisect.bisect_right(virus_line_pos, pos)

        for _, vd in virus_line[start_idx:]:
            if not vd["active"]:
                # virus already die
                continue

            project = pd["name"]
            if project in vd["target_projects"]:
                # start battle
                if vd["target_projects"][project] < pd["life"]:
                    # virus die
                    vd["active"] = False
                pd["life"] -= vd["target_projects"][project]

                if pd["life"] <= 0:
                    # project die
                    pd["life"] = 0
                    break

    survivor = []
    for _, pd in project_line[::-1]:
        if pd["life"] > 0:
            survivor.append(pd["name"])

    return survivor


def main():
    n, m, q = map(int, input().split())

    project_line = []
    virus_line = []

    for _ in range(n):
        project, life, pos = input().split()
        life, pos = int(life), int(pos)

        project_line.append(
            (
                pos,
                {
                    "life": life,
                    "name": project,
                },
            )
        )

    virus_id_idx = {}
    for _ in range(m):
        virus_id, pos = map(int, input().split())
        virus_line.append(
            (
                pos,
                {"id": virus_id, "active": True, "target_projects": {}},
            )
        )
        virus_id_idx[virus_id] = len(virus_line) - 1

    for _ in range(q):
        virus_id, project, dmg = input().split()
        virus_id, dmg = int(virus_id), int(dmg)

        virus_line[virus_id_idx[virus_id]][1]["target_projects"][project] = dmg

    survivor = solve(project_line, virus_line)
    print(len(survivor))
    print(" ".join(survivor))


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
