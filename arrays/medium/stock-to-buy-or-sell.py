class Solution(object):
    def maxProfit(self, prices):
        min_prices=float('inf')
        max_prices=0
        for i in range(len(prices)):
            if prices[i]<min_prices:
                min_prices=prices[i]
            else:
                max_prices=max(max_prices,prices[i]-min_prices)
        return max_prices
sol = Solution()
stock_prices = [7,1,5,3,6,4]
print(sol.maxProfit(stock_prices))