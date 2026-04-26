class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,c=0,len(heights)-1,0
        while l<len(heights)-1 and r>0:
            d=r-l
            a=heights[r]
            b=heights[l]
            a=min(a,b)*d
            if a>c:
                c=a
            if a<b:
                r-=1
            else:
                l+=1
        return c