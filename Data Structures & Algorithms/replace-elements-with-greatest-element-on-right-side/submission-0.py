class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=0
        while l<len(arr):
            c=0
            for i in range(l+1,len(arr)):
                if c<arr[i]:
                     c=arr[i]
            arr[l]=c
            l+=1
        arr[-1]=-1
        return arr