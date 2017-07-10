class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return None
        nums.sort()
        result = sum(nums[:3])
        for i, x in enumerate(nums[:-2]):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if target == s: return s
                if abs(target - s) < abs(target - result): result = s
                if target < s:
                    k -= 1
                else:
                    j += 1
        return result
