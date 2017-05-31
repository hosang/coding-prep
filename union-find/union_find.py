#!/usr/bin/env python3.4


import unittest
from collections import defaultdict


# weighted quick union:
# depth of any node is at most ld N
# proof: depth of tree increases by 1 only when mergin with a tree
#   smaller or same size, so the tree size at most doubles
#   => depth can only increase ld N times (because we double every time)

class Node(object):
    val = None
    parent = None
    size = 1

    def __init__(self, val=None, parent=None):
        self.val = val
        if parent is None:
            self.parent = self
        else:
            self.parent = parent


class UnionFind(object):
    elements = {}

    def _get_node(self, val):
        if val in self.elements:
            return self.elements[val]
        else:
            n = Node(val)
            self.elements[val] = n
            return n

    def _find(self, n):
        if n.parent is n:
            return n
        else:
            # path compression
            p = self._find(n.parent)
            n.parent = p
            return p

    def union(self, a, b):
        na = self._get_node(a)
        nb = self._get_node(b)
        root_a = self._find(na)
        root_b = self._find(nb)
        if root_b.size < root_a.size:
            root_b.parent = root_a
            root_a.size += root_b.size
        else:
            root_a.parent = root_b
            root_b.size += root_a.size

    def connected(self, a, b):
        na = self._get_node(a)
        nb = self._get_node(b)
        return self._find(na) is self._find(nb)

    def print_components(self):
        root_to_id = defaultdict(list)
        for id, n in self.elements.items():
            root = self._find(n)
            root_to_id[root.val].append(id)

        print("there are {} components".format(len(root_to_id)))
        for ids in root_to_id.values():
            ids = ', '.join(str(x) for x in sorted(ids))
            print("{{{}}}  ".format(ids), end='')
        print()


class TestUnionFind(unittest.TestCase):
    def test_simple(self):
        uf = UnionFind()
        uf.union(3, 4)
        self.assertTrue(uf.connected(3, 4))
        uf.union(3, 8)
        uf.union(6, 5)
        uf.union(9, 4)
        uf.union(2, 1)
        self.assertTrue(uf.connected(8, 9))
        self.assertFalse(uf.connected(0, 7))
        uf.union(5, 0)
        uf.union(7, 2)
        uf.union(6, 1)
        uf.union(0, 1)
        self.assertTrue(uf.connected(0, 7))


if __name__ == '__main__':
    unittest.main()
