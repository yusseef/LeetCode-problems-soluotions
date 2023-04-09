# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(node,x,y):
            if x.val < node.val and y.val < node.val:
                return LCA(node.left,x,y)
            if x.val > node.val and y.val > node.val:
                return LCA(node.right,x,y)
            return node
        return LCA(root,p,q)