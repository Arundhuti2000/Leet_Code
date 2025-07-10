class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # Initialize with a very high number
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price # Update min_price if a lower price is found
            else:
                # If current price is not lower, it's a potential selling point
                max_profit = max(max_profit, price - min_price)
        return max_profit