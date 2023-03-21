#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []

        res = set()
        nums.sort()

        for a in range(len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                c, d = b + 1, len(nums) - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    else:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1

        return [list(tup) for tup in res]

# @lc code=end
