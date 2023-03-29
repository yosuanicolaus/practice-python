#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        seen = set()

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                perm.append(num)
                dfs()
                perm.pop()
                seen.remove(num)

        dfs()
        return res


# @lc code=end
