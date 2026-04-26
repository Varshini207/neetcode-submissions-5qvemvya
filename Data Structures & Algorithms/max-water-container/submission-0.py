class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        c=0
        r=len(heights)-1
        while l<len(heights) and r>0:
            a=min(heights[l],heights[r])*(r-l)
            b=min(heights[l],heights[r])
            if a>c:
                c=a
            if b==heights[l]:
                l+=1
            else:
                r-=1
        return c