#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        updater = 0
        length = 0

        for num in nums:
            if num != val:
                nums[updater] = num
                updater += 1
                length += 1

        return length

# @lc code=end
