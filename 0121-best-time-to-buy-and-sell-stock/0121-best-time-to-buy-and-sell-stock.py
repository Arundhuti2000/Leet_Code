class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        n= len(prices)
        while left<right<n:
            if prices[left]<prices[right]:
                max_profit= max(max_profit, prices[right]-prices[left])
                right+=1
            else:    
                left=right
                right+=1 
        return max_profit