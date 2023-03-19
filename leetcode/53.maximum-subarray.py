#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        best = sum(nums)

        while l <= r:
            total = sum(nums[l:r+1])
            best = max(best, total)

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return best


# @lc code=end
