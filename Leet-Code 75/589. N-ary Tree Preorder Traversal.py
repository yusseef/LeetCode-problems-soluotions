"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        if root is None: return
        output.append(root.val)
        for child in root.children:
            self.traverse(child, output)