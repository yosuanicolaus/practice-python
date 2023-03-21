#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if i - k >= 0:
                seen.remove(nums[i - k])

        return False


# @lc code=end
