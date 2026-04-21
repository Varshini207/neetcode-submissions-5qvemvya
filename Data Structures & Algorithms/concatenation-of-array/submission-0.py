class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)*2):
            if i<len(nums):
                l.append(nums[i])
            else:
                l.append(nums[i-len(nums)])
        return l