#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        perm: list[int] = []
        num_count: dict[int, int] = {}

        for n in nums:
            num_count[n] = 1 + num_count.get(n, 0)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for num, count in num_count.items():
                if count > 0:
                    num_count[num] -= 1
                    perm.append(num)
                    dfs()
                    perm.pop()
                    num_count[num] += 1

        dfs()
        return res

# @lc code=end
