# Problem statement
# You have been given the prices of 'N' stocks in an array where each array element represents the stock price for that day. You need to find the maximum profit which you can make by buying and selling the stocks. You may make as many transactions as you want but can not have more than one transaction at a time i.e, if you have the stock, you need to sell it first, and then only you can buy it again.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 1
# 7
# 1 2 3 4 5 6 7
# Sample Output 1 :
# 6
# Explanation :
# We can make the maximum profit by buying the stock on the first day and selling it on the last day.
# Sample Input 2 :
# 1
# 7
# 7 6 5 4 3 2 1
# Sample Output 2 :
# 0
# Explanation :
# We can make the maximum profit by not buying the stock.

def maximumProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

prices = [1, 2, 3, 4, 5, 6, 7]
print(maximumProfit(prices))