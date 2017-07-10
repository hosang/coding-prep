class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        result = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                k, l = j + 1, n - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        result.append((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        while l > k and nums[l + 1] == nums[l]:
                            l -= 1
                    elif s > target:
                        if nums[i] + nums[j] + nums[k] + nums[k + 1] > target:
                            break
                        l -= 1
                    else:
                        if nums[i] + nums[j] + nums[l - 1] + nums[l] < target:
                            break
                        k += 1
                j += 1
                while j < n - 2 and nums[j - 1] == nums[j]:
                    j += 1
            i += 1
            while i < n - 3 and nums[i - 1] == nums[i]:
                i += 1
        return result
