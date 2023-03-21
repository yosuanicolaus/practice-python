#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_count: int, close_count: int):
            if open_count == close_count == n:
                res.append("".join(stack))

            if open_count < n:
                stack.append('(')
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(')')
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return res


# @lc code=end


s = Solution()
s.generateParenthesis(2)
