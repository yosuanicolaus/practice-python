#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        l, r = 0, 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            best = max(best, 1 + r - l)
            seen.add(s[r])
            r += 1

        return best


# @lc code=end
