# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = p = ListNode(None)
        carry = 0
        while l1 is not None or l2 is not None:
            s = carry
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next
            carry = s // 10
            p.next = ListNode(s % 10)
            p = p.next
        if carry > 0:
            p.next = ListNode(carry)
        return head.next
