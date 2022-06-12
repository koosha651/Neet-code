
# NeetCode Challenge
# Solving Problems from NeetCode website, Sliding Window
https://www.youtube.com/watch?v=MK-NZ4hN7rs


1. Best Time to Buy and Sell Stock

# since we use tow pointer technique instead using array the memory usage is O(1)
# the time complexity will be linear because we used tow pointer technique

Input: prices = [7,1,5,3,6,4]

class Solution:
    def maxProfit(prices):
    l , r = 0 , 1 # left is buy.  right is sell
    maxP = 0

    while r < len(prices):      # check r will not pass the arrays size
        if prices[l] < prices[r]:       # if buy price is lower that nex price increment the right Index
            profit = prices[r] - prices[l]
            maxP = max(maxP,profit)
        else:                              # if the buy prices is higher than sell price
            l = r
        r += 1
    return maxP

Output: 5

#=============================================================================================================================================================================

2.
