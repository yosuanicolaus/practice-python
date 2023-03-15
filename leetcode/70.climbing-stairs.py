#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        elif n in self.memo:
            return self.memo[n]

        total = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.memo[n] = total
        return total


# @lc code=end
