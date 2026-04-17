class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=[]
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                a.append(prices[j]-prices[i])
        return(max(a))
            
