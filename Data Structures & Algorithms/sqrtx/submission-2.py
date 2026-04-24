class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        if x==0:
            return 0
        elif x==1 or x==2:
            return 1
        while i<(x/2)+1:
            if i*i==x:
                return i
            elif i*i>x:
                return (i-1)
            i+=1