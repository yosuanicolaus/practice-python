#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()

        for a in range(len(nums) - 2):
            b, c = a + 1, len(nums) - 1
            while b < c:
                three_sum = nums[a] + nums[b] + nums[c]
                if three_sum < 0:
                    b += 1
                elif three_sum > 0:
                    c -= 1
                else:
                    res.add((nums[a], nums[b], nums[c]))
                    b += 1
                    c -= 1

        return list(res)


# @lc code=end
