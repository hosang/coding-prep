class TreeNode(object):
    val = None
    size = 1
    left = right = None

    def __init__(self, val):
        self.val = val


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0] * len(nums)
        root = None
        for i in range(len(nums) - 1, -1, -1):
            root, counts[i] = Solution._insert(root, nums[i])
        return counts

    @staticmethod
    def _insert(root, x):
        if root is None:
            return TreeNode(x), 0

        if x <= root.val:
            root.left, num_smaller = Solution._insert(root.left, x)
        else:
            root.right, num_smaller = Solution._insert(root.right, x)
            num_smaller += root.size - root.right.size + 1
        root.size += 1
        return root, num_smaller
