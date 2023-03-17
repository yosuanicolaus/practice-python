#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        pre, post = 1, 1

        for num in nums:
            res.append(pre)
            pre *= num

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res


# @lc code=end
