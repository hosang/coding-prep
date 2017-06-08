#!/usr/bin/env python3.4

import random
import unittest


class TreeNode(object):
    val = None
    left = None
    right = None

    def __init__(self, val=None):
        self.val = val


def tree_insert(root, val):
    if root is None:
        return TreeNode(val)

    if val <= root.val:
        root.left = tree_insert(root.left, val)
    else:
        root.right = tree_insert(root.right, val)
    return root


def random_tree(val_max=1000, size=100):
    root = None
    for _ in range(size):
        val = random.randrange(0, val_max)
        root = tree_insert(root, val)
    return root


def traverse_inorder(root):
    if root is None: return

    yield from traverse_inorder(root.left)
    yield root.val
    yield from traverse_inorder(root.right)


def traverse_preorder(root):
    if root is None: return

    yield root.val
    yield from traverse_preorder(root.left)
    yield from traverse_preorder(root.right)


def morris_traversal(n):
    while n is not None:
        if n.left is None:
            yield n.val
            n = n.right
        else:
            ins_point = n.left
            while ins_point.right is not n and ins_point.right is not None:
                ins_point = ins_point.right
            if ins_point.right is n:
                ins_point.right = None
                yield n.val
                n = n.right
            else:
                ins_point.right = n
                n = n.left


def morris_traversal_preorder(n):
    while n is not None:
        if n.left is None:
            yield n.val
            n = n.right
        else:
            ins_point = n.left
            while ins_point.right is not n and ins_point.right is not None:
                ins_point = ins_point.right
            if ins_point.right is n:
                ins_point.right = None
                n = n.right
            else:
                yield n.val
                ins_point.right = n
                n = n.left


class TestMorris(unittest.TestCase):

    def test_inorder(self):
        N = 1000
        num_runs = 100
        for _ in range(num_runs):
            root = random_tree(size=N)
            in_order = list(traverse_inorder(root))
            morris = list(morris_traversal(root))
            self.assertEqual(in_order, morris)
            # make sure we didn't modify the tree
            in_order = list(traverse_inorder(root))
            self.assertEqual(in_order, morris)

    def test_preorder(self):
        N = 10
        num_runs = 100
        for _ in range(num_runs):
            root = random_tree(size=N)
            pre_order = list(traverse_preorder(root))
            morris = list(morris_traversal_preorder(root))
            self.assertEqual(pre_order, morris)
            # make sure we didn't modify the tree
            pre_order = list(traverse_preorder(root))
            self.assertEqual(pre_order, morris)


if __name__ == '__main__':
    unittest.main()

