#!/usr/bin/env python3

from itertools import count
import unittest
import random
import string


def intersection(p1, p2):
    l1, l2 = length(p1), length(p2)
    for _ in range(l1 - l2):
        p1 = p1.next
    for _ in range(l2 - l1):
        p2 = p2.next
    for _ in range(min(l1, l2)):
        if p1 is p2:
            return p1
        p1 = p1.next
        p2 = p2.next
    return None


def length(p):
    for l in count():
        if p is None:
            return l
        p = p.next


class LinkedListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



def gen_list(start, end):
    p = head = LinkedListNode()
    for i in range(start, end):
        p.next = LinkedListNode(i)
        p = p.next
    return head.next, p


def gen_intersected_list(a_len, b_len, intersection_len):
    intersect_head, _ = gen_list(
            max(a_len, b_len), max(a_len, b_len) + intersection_len)
    a_head, a_tail = gen_list(0, a_len)
    if a_head is None:
        a_head = intersect_head
    else:
        a_tail.next = intersect_head
    b_head, b_tail = gen_list(0, b_len)
    if b_head is None:
        b_head = intersect_head
    else:
        b_tail.next = intersect_head
    return a_head, b_head, intersect_head


def print_lists(a, b, res):
    la, lb = length(a), length(b)

    line = []
    for _ in range(lb - la):
        line.append('   ')
    while a is not None:
        marker = '*' if a is res else ''
        line.append('{marker:1s}{a.val:2d}'.format(marker=marker, a=a))
        a = a.next
    print(' '.join(line))

    line = []
    for _ in range(la - lb):
        line.append('   ')
    while b is not None:
        if b is res:
            line.append('/')
            break
        line.append(' {b.val:2d}'.format(b=b))
        b = b.next
    print(' '.join(line))
    print()



class TestSearch(unittest.TestCase):

    def test_simple(self):
        for a_len in range(10):
            for b_len in range(10):
                for i_len in range(10):
                    a, b, result = gen_intersected_list(a_len, b_len, i_len)
                    print_lists(a, b, result)
                    self.assertIs(intersection(a, b), result)


if __name__ == '__main__':
    unittest.main()


