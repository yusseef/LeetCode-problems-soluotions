# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        q = collections.deque([root])
        q.append(TreeNode("#"))
        res = []
        temp = []
        while q:
            cur_node = q.popleft()
            if cur_node.val == "#" and not temp:
                break
            elif cur_node.val == "#":
                res.append(temp)
                q.append(TreeNode("#"))
                temp = []
            else:
                temp.append(cur_node.val)
                for node in [cur_node.left, cur_node.right]:
                    if node:
                        q.append(node)
        return res
