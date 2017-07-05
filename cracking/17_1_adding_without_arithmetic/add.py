#!/usr/bin/env python3

import unittest


def add(a, b):
    while a != 0:
        carry = (a & b) << 1
        xor = a ^ b
        a, b = carry, xor
    return b


def add_v2(a, b):
    carry, sum = a, b
    while carry != 0:
        carry, sum = (carry & sum) << 1, carry ^ sum
    return sum


class TestAdd(unittest.TestCase):
    def test_simple(self):
        for a in range(200):
            for b in range(1000):
                self.assertEqual(add(a, b), a + b)
                self.assertEqual(add_v2(a, b), a + b)


if __name__ == '__main__':
    unittest.main()
