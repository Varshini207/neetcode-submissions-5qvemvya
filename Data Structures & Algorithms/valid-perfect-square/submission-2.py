class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        while i<((num)/2)+1:
            if i*i==num:
                return True
            if i*i>num:
                return False
            i+=1
        return False