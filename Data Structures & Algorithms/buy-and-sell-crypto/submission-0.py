class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 0
        maxProfit = 0
        while end < len(prices):
            if prices[start] > prices[end]:
                start+=1
            else:
                profit = prices[end] - prices[start]
                end += 1
            maxProfit = max(profit, maxProfit)
        return maxProfit