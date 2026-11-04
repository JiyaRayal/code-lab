def maxprofit(prices):
    min_price = price[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price,price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit