class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for j, y in enumerate(nums):
            x = target - y
            if x in seen:
                i = seen[x]
                return i, j
            seen[y] = j
        return None
