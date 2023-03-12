#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        result = 0
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

        while i < len(s):
            # check if it's a subtraction
            if i + 1 < len(s) and value[s[i]] < value[s[i+1]]:
                result += value[s[i+1]] - value[s[i]]
                i += 2
            else:
                # add to result as normal
                result += value[s[i]]
                i += 1

        return result


# @lc code=end
