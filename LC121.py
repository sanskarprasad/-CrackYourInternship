#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = 0
        profit = 0
        left = 0
        while right< len(prices):
            profit = max(profit,(prices[right]-prices[left]))
            left = prices.index(min(prices[left],prices[right]))
            right+=1
        return profit
