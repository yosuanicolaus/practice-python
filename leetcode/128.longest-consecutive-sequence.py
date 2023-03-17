#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ns = set(nums)
        best = 0

        for num in ns:
            if num - 1 in ns:
                # not a start of sequence
                continue

            seq_len = 1

            while num + 1 in ns:
                seq_len += 1
                num += 1

            best = max(best, seq_len)

        return best

# @lc code=end
