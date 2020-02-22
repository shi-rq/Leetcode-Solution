'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


# 1 o(n^2) Basic method
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for n in range(len(prices) - 1):
            for i in prices[n+1:]:
                if i - prices[n] > profit: profit = i - prices[n]
        return profit


# 2 Improved
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        rh = len(prices) - 1
        for n in range(rh, 0, -1):
            if prices[n] >= prices[rh]:
                rh = n
                for lh in range(0, rh):
                    if prices[rh] - prices[lh] > profit: profit = prices[rh] - prices[lh]
        return profit
# using max() / min()
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        rh = len(prices) - 1
        for n in range(rh, 0, -1):
            if prices[n] >= prices[rh]:
                rh = n
                profit0 = prices[rh] - min(prices[0: rh])
                if profit0 > profit: profit = profit0
        return profit


# 3 More improved
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1 : return 0
        profit = 0
        if max(prices[1:]) - prices[0] > profit: profit = max(prices[1:]) - prices[0]
        for n in range(1, len(prices)-1):
            if prices[n] <= prices[n-1] and prices[n] <= prices[n+1]:
                if max(prices[n+1:]) - prices[n] > profit: profit = max(prices[n+1:]) - prices[n]
        return profit