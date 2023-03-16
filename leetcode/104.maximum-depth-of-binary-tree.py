from typing import Optional
from collections import deque
#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_branch = 1 + self.maxDepth(root.left)
        right_branch = 1 + self.maxDepth(root.right)
        return max(left_branch, right_branch)

    # iterative DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        best = 0

        while stack:
            node, depth = stack.pop()

            if node:
                best = max(best, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth+1))

        return best

    # iterative BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 0
        if root:
            queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        return level


# @lc code=end
