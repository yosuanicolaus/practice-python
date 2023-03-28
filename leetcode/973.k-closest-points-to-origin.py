#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
from heapq import heapify, heappop, nsmallest
from typing import List

# @lc code=start


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_pts: list[tuple[int, int, int]] = []
        res: list[list[int]] = []

        for x, y in points:
            dist = x**2 + y**2
            dist_pts.append((dist, x, y))

        heapify(dist_pts)
        for _ in range(k):
            dist, x, y = heappop(dist_pts)
            res.append([x, y])

        return res


# @lc code=end
