class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx=0
        left=0
        right=len(heights)-1
        while left < right:
                width = min(heights[left], heights[right])
                length = right - left
                total = width * length
                if maxx < total:
                    maxx = total
                
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1
        return maxx



        