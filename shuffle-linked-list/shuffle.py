#!/usr/bin/env python3.4

import random
import unittest

class Node(object):
    value = None
    next = None

    def __init__(self, value=None):
        self.value = value


def shuffle_merge(h1, h2):
    p = head = Node()

    while h1 is not None or h2 is not None:
        if h1 is None or (h2 is not None and random.choice((True, False))):
            p.next = h2
            p = p.next
            h2 = h2.next
        else:
            p.next = h1
            p = p.next
            h1 = h1.next
    return head.next


def shuffle_recurse(head, n):
    if n <= 1:
        return head

    n1 = n // 2
    n2 = n - n1

    head1 = p = head
    for _ in range(n1 - 1):
        p = p.next
    head2 = p.next
    p.next = None

    head1 = shuffle_recurse(head1, n1)
    head2 = shuffle_recurse(head2, n2)
    merged = shuffle_merge(head1, head2)
    return merged


def shuffle(head):
    n = 0
    p = head
    while p is not None:
        p = p.next
        n += 1

    return shuffle_recurse(head, n)


def array_to_list(arr):
    p = head = Node()
    for x in arr:
        p.next = Node(x)
        p = p.next
    return head.next


def list_to_array(head):
    arr = []
    while head is not None:
        arr.append(head.value)
        head = head.next
    return arr


class TestShuffle(unittest.TestCase):

    def test_set_same(self):
        for _ in range(20):
            arr = list(range(1000))
            linked_list = array_to_list(arr)
            shuffled_list = shuffle(linked_list)
            shuffled_arr = list_to_array(shuffled_list)
            self.assertEqual(set(arr), set(shuffled_arr))


if __name__ == '__main__':
    unittest.main()

