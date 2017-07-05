#!/usr/bin/env python3

from collections import Counter
import unittest
import string
import random


simple = lambda a, b: Counter(a) == Counter(b)

def v1(a, b, num_chars=256):
    a_hist = str_hist(a, num_chars)
    b_hist = str_hist(b, num_chars)
    for a_cnt, b_cnt in zip(a_hist, b_hist):
        if a_cnt != b_cnt:
            return False
    return True

def str_hist(s, n):
    hist = [0] * n
    for c in s:
        hist[ord(c)] += 1
    return hist

def less_mem(a, b, num_chars=256):
    hist = [0] * num_chars
    for c in a:
        hist[ord(c)] += 1
    for c in b:
        hist[ord(c)] -= 1
        if hist[ord(c)] < 0:
            return False
    for count in hist:
        if count != 0:
            return False
    return True


def sample(population, k):
    # sample with replacement
    n = len(population)
    return [population[random.randrange(n)] for _ in range(k)]

class TestPermutation(unittest.TestCase):
    def test_simple(self):
        k = 200
        for _ in range(100):
            chars = sample(string.ascii_letters, k)
            chars2 = sample(string.ascii_letters, k - 1)

            random.shuffle(chars)
            a = ''.join(chars)
            random.shuffle(chars)
            b = ''.join(chars)
            random.shuffle(chars2)
            c = ''.join(chars2)

            self.assertTrue(simple(a, b))
            self.assertTrue(v1(a, b))
            self.assertTrue(less_mem(a, b))
            self.assertFalse(simple(a, c))
            self.assertFalse(v1(a, c))
            self.assertFalse(less_mem(a, c))

if __name__ == '__main__':
    unittest.main()

