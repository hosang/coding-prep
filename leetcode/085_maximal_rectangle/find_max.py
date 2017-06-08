# using solution of problem 84
# largestRectangleArea is in O(n)
# so maximalRectangle is in O(n) where n is the number of elements in matrix

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            for i, val in enumerate(row):
                heights[i] = 0 if val == '0' else heights[i] + 1
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(-1)
        stack = []
        max_area = 0
        for x, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                rect_h = heights[stack.pop()]
                x_start = 0 if not stack else stack[-1] + 1
                max_area = max(max_area, (x - x_start) * rect_h)
            stack.append(x)
        heights.pop()
        return max_area
