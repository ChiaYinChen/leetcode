"""
0094. BBinary Tree Inorder Traversal (Easy)
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        res = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            res.append(node.val)
            root = node.right

        return res
