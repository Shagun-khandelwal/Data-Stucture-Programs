# leetcode 121. Best time to buy and sell stock
def maxProfit(prices: list[int]) -> int:
    # mini =maxi= min(prices)
    # buy_index = prices.index(mini)
    # for i in range(buy_index,len(prices)):
    #     if prices[i]>maxi:
    #         maxi=prices[i]
    # return maxi-mini
    left = 0
    right = 1
    max_profit = 0
    profit = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit < 0:
            left = right
        elif profit > 0:
            max_profit = max(max_profit, profit)
        right += 1
    return max_profit
prices=[1,5,3,6,4]
print(maxProfit(prices))