#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int, int] = {}
        freq: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        res: list[int] = []

        for num in nums:
            counts.setdefault(num, 0)
            counts[num] += 1
        for num, count in counts.items():
            freq[count].append(num)

        for nums in freq[::-1]:
            for num in nums:
                res.append(num)
                k -= 1
                if k == 0:
                    return res


# @lc code=end
