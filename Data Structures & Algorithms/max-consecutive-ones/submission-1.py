class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,n,c=0,len(nums),0
        for i in range(n):
            if nums[i]==1:
                c+=1
                m=max(m,c)
            else:
                c=0
        return m

               