#!/usr/bin/env python3

from itertools import count
import unittest


def loop_start(head):
    loop_node = find_loop(head)
    if loop_node is None:
        return None
    length = count_loop_len(loop_node)
    return find_loop_start(head, length)


def find_loop(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return fast
    return None


def count_loop_len(start):
    p = start.next
    for l in count(1):
        if p is start:
            return l
        p = p.next


def find_loop_start(head, l):
    p1 = p2 = head
    for _ in range(l):
        p1 = p1.next
    while p1 is not p2:
        p1, p2 = p1.next, p2.next
    return p1


class LinkedListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def gen_list(length):
    if length <= 0:
        return None, None
    head = p = LinkedListNode()
    for i in range(length):
        p.next = LinkedListNode(i)
        p = p.next
    return head.next, p


def gen_looped_list(pref_len, loop_len):
    head, before_loop = gen_list(pref_len)
    loop_head, loop_tail = gen_list(loop_len)
    if loop_tail is not None:
        loop_tail.next = loop_head

    if before_loop is None:
        return loop_head, loop_head
    before_loop.next = loop_head
    return head, loop_head


def print_list(head):
    line = []
    visited = {}
    p = head
    while p:
        if p in visited:
            line[visited[p]] = '*' + line[visited[p]]
            break
        visited[p] = len(line)
        line.append('{}'.format(p.val))
        p = p.next
    print('-'.join(line), '|')


class TestSearch(unittest.TestCase):

    def test_simple(self):
        for pref_len in range(20):
            for loop_len in range(20):
                head, loop_head = gen_looped_list(pref_len, loop_len)
                #print_list(head)
                self.assertIs(loop_start(head), loop_head)


if __name__ == '__main__':
    unittest.main()


