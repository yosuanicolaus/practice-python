#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(total: int, idx: int):
            if total > target:
                return
            if total == target:
                res.append(comb[:])
                return

            for i in range(idx, len(candidates)):
                num = candidates[i]
                comb.append(num)
                dfs(total + num, i)
                comb.pop()

        dfs(0, 0)
        return res

# @lc code=end
