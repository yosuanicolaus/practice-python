#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) >= 2:
            first = heappop(stones)
            second = heappop(stones)
            if first < second:
                heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# @lc code=end
