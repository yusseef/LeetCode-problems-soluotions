class Solution(object):
    def minElem(self, root):
        if not root:
            return float('inf')
        
        if not root.left and not root.right:
            return root.val
        
        return min(root.val, self.minElem(root.left), self.minElem(root.right))
    
    def maxElem(self, root):
        if not root:
            return float('-inf')
        
        if not root.left and not root.right:
            return root.val
        
        return max(root.val, self.maxElem(root.left), self.maxElem(root.right))
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or not(root.left or root.right):
            return True
        validRoot = root.val > self.maxElem(root.left) and root.val < self.minElem(root.right)
        validLeft = self.isValidBST(root.left)
        validRight = self.isValidBST(root.right)
        return validRoot and validLeft and validRight