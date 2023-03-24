#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26
        c2 = [0] * 26

        for ch in s1:
            c1[ord(ch) - ord('a')] += 1

        for i, ch in enumerate(s2):
            c2[ord(ch) - ord('a')] += 1

            if i >= len(s1) - 1:
                if c1 == c2:
                    return True
                old_ch = s2[i - len(s1) + 1]
                oc_idx = ord(old_ch) - ord('a')
                c2[oc_idx] -= 1

        return False


# @lc code=end
