# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev, prev.next = ListNode(None), head
        head_dummy = prev
        
        num = 0
        while head is not None:
            num += 1
            head = head.next
        
        for _ in range(num // k):
            first = new_next = prev.next
            curr = new_next.next
            for _ in range(k - 1):
                curr.next, curr, new_next = new_next, curr.next, curr
            prev.next, first.next = new_next, curr
            prev = first
        return head_dummy.next
