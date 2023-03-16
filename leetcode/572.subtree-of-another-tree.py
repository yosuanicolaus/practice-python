#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # get all potential subtree, store in 'candidates'
        candidates: list[TreeNode] = []
        dfs = [root]

        while dfs:
            node = dfs.pop()
            if node.val == subRoot.val:
                candidates.append(node)
            if node.left:
                dfs.append(node.left)
            if node.right:
                dfs.append(node.right)

        # for every candidate, check if it's same as subRoot
        for node in candidates:
            if self.same_tree(node, subRoot):
                return True
        return False

    def same_tree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree1 and not tree2:
            return True
        elif tree1 and tree2 and tree1.val == tree2.val:
            return self.same_tree(tree1.left, tree2.left) and self.same_tree(tree1.right, tree2.right)
        else:
            return False


# @lc code=end
