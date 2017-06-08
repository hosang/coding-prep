
class Solution(object):
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
