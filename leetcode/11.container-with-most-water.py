#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        best = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            best = max(best, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best

# @lc code=end
