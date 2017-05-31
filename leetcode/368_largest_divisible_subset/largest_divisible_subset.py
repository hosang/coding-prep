class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        divisors = [None] * len(nums)
        global_max = (-1, -1)
        for i, x in enumerate(nums):
            max_div = (1, -1)
            for j in xrange(i):
                if x % nums[j] == 0:
                    max_div = max(max_div, (divisors[j][0] + 1, j))
            divisors[i] = max_div
            global_max = max(global_max, (max_div[0], i))

        res = []
        i = global_max[1]
        while i >= 0:
            res.append(nums[i])
            i = divisors[i][1]
        return res
