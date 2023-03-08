class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans: list[list[int]] = []
        for a, b in sorted(intervals):
            if ans and ans[-1][1] >= a:
                ans[-1][1] = max(ans[-1][1], b)
            else:
                ans.append([a, b])
        return ans
