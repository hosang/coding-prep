# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
            
        assert root.val == key
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            p = root.right
            while p.left is not None:
                p = p.left
            p.left = root.left
            return root.right
            
