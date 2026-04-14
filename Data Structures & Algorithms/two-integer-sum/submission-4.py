class Solution:
    def twoSum(self, nums, target):
        d={}
        for i,v in enumerate(nums):
            c=target-v
            if c in d:
                return[d[c],i]
            d[v]=i
        

