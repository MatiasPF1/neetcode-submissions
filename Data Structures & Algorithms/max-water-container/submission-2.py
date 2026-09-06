class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right= len(heights) - 1
        Answer = 0

        while left < right:
            widht = right - left 
            height = min(heights[left], heights[right])
            Area = widht * height 
            Answer = max(Answer,Area)
            if heights[left] < heights[right]:
                left +=1 
            else:
                right -=1 
        return Answer


        