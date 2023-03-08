class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        scm = {}
        tcm = {}

        for i in range(len(s)):
            scm.setdefault(s[i], 0)
            tcm.setdefault(t[i], 0)
            scm[s[i]] += 1
            tcm[t[i]] += 1

        return scm == tcm
