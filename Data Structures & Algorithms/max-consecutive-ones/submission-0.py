class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,n=0,len(nums)
        for i in range(n):
            c=0
            for j in range(i,n):
                if nums[j]==0: break
                c+=1
            m=max(m,c)
        return m

               