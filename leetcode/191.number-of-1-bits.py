#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n % 2
            n >>= 1

        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            n &= (n-1)
            res += 1

        return res


# @lc code=end
