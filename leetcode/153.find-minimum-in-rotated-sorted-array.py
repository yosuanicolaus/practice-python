#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        # edge case: nums is not rotated
        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[-1]:
                # this is the left asc array, go right
                l = mid + 1
            elif nums[mid] < nums[mid-1]:
                # found the gap point
                return nums[mid]
            else:
                # on the right asc array, but not the gap yet, go left
                r = mid - 1

        return nums[l]

# @lc code=end
