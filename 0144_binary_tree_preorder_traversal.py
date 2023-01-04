"""
0144. Binary Tree Preorder Traversal (Easy)
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                # as we are using stack which works on LIFO,
                # we need to push right tree first so that left will be popped out
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
