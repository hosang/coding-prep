#!/usr/bin/env python3

from collections import defaultdict
import unittest


class UnionFind(object):
    def __init__(self):
        self._weight = {}
        self._parent = {}
        self._id = {}
        self._id_to_val = {}
        self._id_cnt = 0

    def add(self, a):
        if a not in self._id:
            a_id = self._id_cnt
            self._id_cnt += 1
            self._parent[a_id] = a_id
            self._weight[a_id] = 1
            self._id[a] = a_id
            self._id_to_val[a_id] = a
        return self._id[a]

    def find(self, a):
        p_id = self._find(self.add(a))
        return self._id_to_val[p_id]

    def _find(self, a):
        p = self._parent[a]
        if p != a:
            p = self._find(p)
            self._parent[a] = p
        return p

    def union(self, a, b):
        parent_a = self._find(self.add(a))
        parent_b = self._find(self.add(b))
        if self._weight[parent_a] > self._weight[parent_b]:
            self._parent[parent_b] = parent_a
            self._weight[parent_a] += self._weight[parent_b]
        else:
            self._parent[parent_a] = parent_b
            self._weight[parent_b] += self._weight[parent_a]


def build_hist(hist, equiv_pairs):
    uf = UnionFind()
    for a, b in equiv_pairs:
        uf.union(a, b)

    new_hist = defaultdict(int)
    for name, cnt in hist.items():
        new_hist[uf.find(name)] += cnt
    return new_hist


class TestSearch(unittest.TestCase):
    def test_small(self):
        h = build_hist({}, [])
        self.assertEqual(len(h), 0)

        in_hist = {'a': 1, 'b': 2, 'c': 4, 'd': 8}
        h = build_hist(in_hist, [])
        self.assertEqual(in_hist, h)

        h = build_hist(in_hist, [('a', 'b')])
        self.assertEqual(max(h['a'], h['b']), 3)
        self.assertEqual(sum((h['a'], h['b'])), 3)

        h = build_hist(in_hist, [('a', 'b'), ('b', 'c')])
        self.assertEqual(max((h['a'], h['b'], h['c'])), 7)
        self.assertEqual(sum((h['a'], h['b'], h['c'])), 7)

        h = build_hist(in_hist, [('a', 'b'), ('d', 'c')])
        self.assertEqual(max(h['a'], h['b']), 3)
        self.assertEqual(sum((h['a'], h['b'])), 3)
        self.assertEqual(max(h['c'], h['d']), 12)
        self.assertEqual(sum((h['c'], h['d'])), 12)


if __name__ == '__main__':
    unittest.main()

