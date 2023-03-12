#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = 0
        while h < len(haystack):
            if haystack[h] != needle[0]:
                h += 1
                continue

            for n in range(len(needle)):
                if h + n < len(haystack) and haystack[h+n] == needle[n]:
                    if n == len(needle) - 1:
                        return h
                    else:
                        continue
                else:
                    break
            h += 1

        return -1

# @lc code=end
