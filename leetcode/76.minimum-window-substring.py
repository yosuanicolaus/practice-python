#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = ""
        best_len = float('inf')
        sc, tc = {}, {}
        is_eligible = False
        
        for ch in t:
            tc[ch] = 1 + tc.get(ch, 0)
        
        a, b = 0, 0

        while a < len(s) and b < len(s):
            if is_eligible:
                pass
            elif s[b] in tc:
                sc[s[b]] = 1 + sc.get(s[b], 0)
                if not self.is_window_eligible(sc, tc):
                    continue
                window = s[a:b+1]
                if len(window) < best_len:
                    best = window
                    best_len = len(window)
            else:
                b += 1
        
        return best
            
                
    def is_window_eligible(self, sc: dict, tc: dict):
            for ch, amount in tc.items():
                if sc[ch] < amount:
                    return False
            return True
        
        

            

        
# @lc code=end

