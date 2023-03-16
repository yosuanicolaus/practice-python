#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # TODO - rewrite with the proper solution (bit manipulation)
    def reverseBits(self, n: int) -> int:
        sbin = bin(n)[2:]
        if len(sbin) < 32:
            sbin = "0" * (32 - len(sbin)) + sbin
        lbin = list(sbin)
        a, b = 0, len(lbin) - 1

        while a < b:
            lbin[a], lbin[b] = lbin[b], lbin[a]
            a, b = a+1, b-1

        sbin = ''.join(lbin)
        return int(sbin, 2)


# @lc code=end
