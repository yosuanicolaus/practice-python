#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        rotated = nums[r] < nums[l]

        while l <= r:
            m = l + (r - l) // 2

            if rotated and target <= nums[-1] and nums[m] > nums[-1]:
                # go to right array
                l = m + 1
            elif rotated and target >= nums[0] and nums[m] < nums[0]:
                # go to left array
                r = m - 1
            elif nums[m] < target:
                # go right
                l = m + 1
            elif nums[m] > target:
                # go left
                r = m - 1
            else:
                return m

        return -1


# @lc code=end

s = Solution()
print(s.search([3, 1], 1))
