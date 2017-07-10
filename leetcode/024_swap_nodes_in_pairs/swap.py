# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(None)
        dummy_head.next = head
        n = dummy_head
        while n.next is not None and n.next.next is not None:
            # n -> n1 -> n2 -> n3 (might be none)
            # n -> n2 -> n1 -> n3 (next n1)
            n1, n2, n3 = n.next, n.next.next, n.next.next.next
            n.next, n2.next, n1.next = n2, n1, n3
            n = n.next.next
        return dummy_head.next
