class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = i = 0
        seen = {}
        for j, c in enumerate(s):
            i = max(i, seen.get(c, -1) + 1)
            seen[c] = j
            max_len = max(max_len, j - i + 1)
        return max_len
