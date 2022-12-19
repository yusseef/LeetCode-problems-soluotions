def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = new_list = ListNode(0)
        
        while(l1 and l2):
            if (l1.val < l2.val):
                new_list.next = l1
                l1 = l1.next  
            else:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next

        new_list.next = l1 or l2
        return head.next
