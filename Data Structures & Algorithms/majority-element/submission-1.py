class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=Counter(nums)
        d=n.most_common(1)
        return((d[0])[0])