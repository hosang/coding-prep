#!/usr/bin/env python3.4

import unittest
import random
import statistics


def bisect(a, x, left=True):
    l = 0
    r = len(a) - 1
    res = 0 if left else len(a)
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            if left:
                res = m
                r = m - 1
            else:
                res = m + 1
                l = m + 1
        elif a[m] < x:
            l = m + 1
            if left:
                res = m + 1
        else:
            r = m - 1
            if not left:
                res = m
    return res


class TestBisect(unittest.TestCase):
    cases = [
            ([1], 0, 0, 0),
            ([1], 1, 0, 1),
            ([1], 2, 1, 1),
            ([1, 2, 3], 0, 0, 0),
            ([1, 2, 3], 1, 0, 1),
            ([1, 2, 3], 2, 1, 2),
            ([1, 2, 3], 3, 2, 3),
            ([1, 2, 3], 4, 3, 3),
    ]

    def test_bisect(self):
        for arr, x, want_l, want_r in self.cases:
            got_l = bisect(arr, x, left=True)
            self.assertEqual(got_l, want_l,
                    'failed for {}, {}, left: want {}, got {}'.format(
                        arr, x, want_l, got_l))
            got_r = bisect(arr, x, left=False)
            self.assertEqual(got_r, want_r,
                    'failed for {}, {}, right: want {} got {}'.format(
                        arr, x, want_r, got_r))

    def test_random_bisect(self):
        N = 1000
        for seed in (42, 1024, 31415):
            random.seed(seed)
            samples = random.sample(range(N), 100)
            samples.sort()
            for x in range(-1, N + 2):
                got_l = bisect(samples, x, left=True)
                got_r = bisect(samples, x, left=False)
                smaller = sum(y < x for y in samples)
                smaller_equal = sum(y <= x for y in samples)
                self.assertEqual(got_l, smaller,
                    'failed for {}, {}, left: want {} got {}'.format(
                        samples, x, smaller, got_l))
                self.assertEqual(got_r, smaller_equal,
                    'failed for {}, {}, right: want {} got {}'.format(
                        samples, x, smaller_equal, got_r))


def find_pos(nums1, nums2, pos):
    if pos >= len(nums1) + len(nums2):
        return None
    elif not nums1:
        return nums2[pos]
    elif not nums2:
        return nums1[pos]

    if len(nums1) > len(nums2):
        x = nums1[len(nums1) // 2]
    else:
        x = nums2[len(nums2) // 2]
    min1 = bisect(nums1, x, left=True)
    max1 = bisect(nums1, x, left=False)
    min2 = bisect(nums2, x, left=True)
    max2 = bisect(nums2, x, left=False)
    if min1 + min2 <= pos < max1 + max2:
        return x
    elif pos < min1 + min2:
        return find_pos(nums1[:min1], nums2[:min2], pos)
    else:
        return find_pos(nums1[max1:], nums2[max2:], pos - max1 - max2)


def median(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 + n2 == 0:
        return None
    elif (n1 + n2) % 2 == 1:
        return find_pos(nums1, nums2, (n1 + n2) // 2)
    else:
        return (find_pos(nums1, nums2, (n1 + n2 - 1) // 2) + 
                find_pos(nums1, nums2, (n1 + n2) // 2)) / 2.0


class TestMedian(unittest.TestCase):
    cases = [
            ([1], [1], 1),
            ([1, 1, 1, 1], [1, 1], 1),
            ([1], [2], 1.5),
            ([1], [2, 3], 2),
            ([1], [2, 3, 4], 2.5),
    ]

    def test_median(self):
        for nums1, nums2, want in self.cases:
            got = median(nums1, nums2)
            got2 = median(nums2, nums1)
            self.assertEqual(got, want,
                    'failed for {}, {}: want {}, got {}'.format(
                        nums1, nums2, want, got))
            self.assertEqual(got2, want,
                    'failed for {}, {}: want {}, got {}'.format(
                        nums1, nums2, want, got2))

    def test_random(self):
        maxlen = 40
        N = 100
        random.seed(42)
        for n1 in range(maxlen + 1):
            for n2 in range(maxlen + 1):
                if n1 == n2 == 0:
                    continue
                nums1 = random.sample(range(N), n1)
                nums1.sort()
                nums2 = random.sample(range(N), n2)
                nums2.sort()
                want = statistics.median(nums1 + nums2)
                got = median(nums1, nums2)
                self.assertEqual(got, want,
                        'failed for {}, {}: want {}, got {}'.format(
                            nums1, nums2, want, got))


if __name__ == '__main__':
    unittest.main()

