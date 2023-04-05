# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head


    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:

        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow


    return None
