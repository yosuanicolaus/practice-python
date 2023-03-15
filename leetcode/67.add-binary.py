#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            diff = len(b) - len(a)
            a = diff * '0' + a
        elif len(a) > len(b):
            diff = len(a) - len(b)
            b = diff * '0' + b

        res = ['0'] * len(a)
        temp = 0

        for i in range(len(a) - 1, -1, -1):
            total = temp + int(a[i]) + int(b[i])
            if total >= 2:
                temp = 1
                total -= 2
            else:
                temp = 0

            res[i] = str(total)

        ans = ''.join(res)
        if temp == 1:
            ans = '1' + ans
        return ans


# @lc code=end
