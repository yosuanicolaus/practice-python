from typing import Optional, List
#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: Optional[TreeNode], res: list[int]):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


# @lc code=end
