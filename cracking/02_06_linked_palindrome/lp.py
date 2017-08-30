#!/usr/bin/env python3

from itertools import count
import unittest
import random
import string


class LinkedListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def recursive(head):
    p = head
    for length in count():
        if p is None:
            break
        p = p.next

    def rec(p, l):
        if l <= 1:
            return True, (p if l == 0 else p.next)
        is_pal, tail = rec(p.next, l - 2)
        is_pal = is_pal and p.val == tail.val
        return is_pal, tail.next

    return rec(head, length)[0]


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def gen_palindrome(length):
    s = random_string(length // 2)
    mid = '' if length % 2 == 0 else random_string(1)
    return s + mid + s[::-1]


def gen_non_palindrome(length):
    assert length > 1
    s = random_string(length)
    m = length // 2
    while s[:m] == s[-1:-m - 1:-1]:
        s = random_string(length)
    return s


def to_linked_list(s):
    if not s:
        return None
    else:
        return LinkedListNode(s[0], to_linked_list(s[1:]))


class TestSearch(unittest.TestCase):

    def test_recursive(self):
        ll = to_linked_list('')
        self.assertTrue(recursive(ll))
        ll = to_linked_list('a')
        self.assertTrue(recursive(ll))

        for length in range(2, 100):
            ll = to_linked_list(gen_palindrome(length))
            self.assertTrue(recursive(ll))
            ll = to_linked_list(gen_non_palindrome(length))
            self.assertFalse(recursive(ll))


if __name__ == '__main__':
    unittest.main()


