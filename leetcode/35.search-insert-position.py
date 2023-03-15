#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # binary search (O(log n))

        low, high = 0, len(nums) - 1

        if target > nums[high]:
            return len(nums)

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                return mid

        return low


# @lc code=end
