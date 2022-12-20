# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length_list = 0
        start = node = head 
        while start:
            length_list += 1
            start = start.next
        print(length_list)
        mid = length_list // 2
        print(mid)
        count = 0
        while node:
            if counter == mid:
                return node
            else:
                count += 1
                node = node.next
        return None