# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        lst = []
        while l1 and l2:
            if l1.next.val < l2.next.val:
                lst.append(l1)
                l1 = l1.next