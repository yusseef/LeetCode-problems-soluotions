# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.previous = None
        self.min = float('inf')
        
    def minDiffInBST(self, root: TreeNode) -> int:
        self.inOrder(root)
        return self.min
        
    def inOrder(self, root: TreeNode) -> None:
        if not root:
            return
        
        self.inOrder(root.left)
        if self.previous:
            self.min = min(self.min, root.val - self.previous.val)
        self.previous = root
        self.inOrder(root.right)