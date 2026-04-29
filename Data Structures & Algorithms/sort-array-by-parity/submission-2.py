class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        o,e=[],[]
        for a in nums:
            if a%2==0:
                e.append(a)
            else:
                o.append(a)
        return e+o
