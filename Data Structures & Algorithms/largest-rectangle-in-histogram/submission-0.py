class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []      # stores indices
        maxArea = 0

        heights.append(0)   # add a dummy bar to empty the stack at the end

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                h = heights[stack.pop()]   # height of rectangle

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                maxArea = max(maxArea, h * w)

            stack.append(i)

        return maxArea