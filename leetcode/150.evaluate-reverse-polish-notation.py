#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from math import trunc


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == '+':
                    stack.append(n1 + n2)
                elif token == '-':
                    stack.append(n1 - n2)
                elif token == '*':
                    stack.append(n1 * n2)
                else:
                    stack.append(trunc(n1 / n2))

        return stack.pop()

# @lc code=end
