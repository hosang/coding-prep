class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        order = [idx for idx, _ in sorted(enumerate(nums), key=lambda x: x[1])]
        i = 0
        j = len(nums) - 1
        while nums[order[i]] + nums[order[j]] != target and i < j:
            if nums[order[i]] + nums[order[j]] < target:
                i += 1
            else:
                j -= 1
        assert i < j
        return order[i], order[j]
