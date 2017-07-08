#!/usr/bin/env python3

import unittest
import random


class BinaryNum(object):
    def __init__(self, n):
        self._n = n

    def bit(self, b):
        return (self._n >> b) & 1


def find_missing(arr):
    result = 0
    b = 0
    while arr:
        zero_arr = []
        one_arr = []
        for e in arr:
            if e.bit(b) == 0:
                zero_arr.append(e)
            else:
                one_arr.append(e)
        if len(zero_arr) > len(one_arr):
            arr = one_arr
            result |= 1 << b
            b += 1
        else:
            arr = zero_arr
            b += 1
    return result


class TestSearch(unittest.TestCase):
    def test_manual(self):
        a = lambda arr: [BinaryNum(x) for x in arr]
        self.assertEqual(find_missing(a([])), 0)
        self.assertEqual(find_missing(a([1])), 0)
        self.assertEqual(find_missing(a([0])), 1)
        self.assertEqual(find_missing(a([0, 1])), 2)
        self.assertEqual(find_missing(a([0, 2])), 1)
        self.assertEqual(find_missing(a([1, 2])), 0)

    def test_simple(self):
        num_elements = 10000
        for _ in range(100):
            arr = [BinaryNum(x) for x in range(num_elements)]
            missing = random.randrange(num_elements)
            del arr[missing]
            random.shuffle(arr)
            self.assertEqual(find_missing(arr), missing)


if __name__ == '__main__':
    unittest.main()

