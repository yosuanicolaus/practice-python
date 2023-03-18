#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        maxf = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                # window not valid
                count[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best

# @lc code=end
