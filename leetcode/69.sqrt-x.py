#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        lo, hi = 0, x

        while True:
            m = lo + (hi - lo) // 2

            if m > x / m:
                # go low
                hi = m - 1
            else:
                if m+1 > x/(m+1):
                    return m
                # go high
                lo = m + 1


# @lc code=end
