#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list[int])

        for word in strs:
            count = [0] * 26
            for ch in word:
                ch_idx = ord(ch) - ord("a")
                count[ch_idx] += 1
            ans[tuple(count)].append(word)

        return ans.values()


# @lc code=end
