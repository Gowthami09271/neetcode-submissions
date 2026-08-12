class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_v=0
        res=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    res=prices[j]-prices[i]
                    max_v=max(max_v,res)
                    
        return max_v
                
                
                    
