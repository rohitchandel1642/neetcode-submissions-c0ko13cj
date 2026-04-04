class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        stck=[]
        for i,h in enumerate(heights):
            start=i
            while stck and stck[-1][1]>h:
                index,height=stck.pop()
                maxarea=max(maxarea,height*(i-index))
                start=index
            
            stck.append([start,h])
        
        for i,h in stck:
            
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea