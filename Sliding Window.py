
# NeetCode Challenge
# Solving Problems from NeetCode website, Sliding Window

# the way we can recognize these problems: 
things we iterate over sequentially: 
    * the contiguous sequence of element
    * string, arrays, linked list
 type of question that is usually asked is:
    * asked about min, max, longest, shortest, whether contain 
    * maybe we have to calculate something 


#=============================================================================================================================================================================
  


https://www.youtube.com/watch?v=MK-NZ4hN7rs


1. Best Time to Buy and Sell Stock

# since we use tow pointer technique instead using array the memory usage is O(1)
# the time complexity will be linear because we used tow pointer technique                                                          second method

Input: prices = [7,1,5,3,6,4]

class Solution:                                                                                                 def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(prices):                                                                                                    res = 0   
    l , r = 0 , 1 # left is buy.  right is sell                                                                               l = 0
    maxP = 0
                                                                                                                              for r in range(1, len(prices)):
    while r < len(prices):      # check r will not pass the arrays size                                                            if prices[r] < prices[l]:
        if prices[l] < prices[r]:       # if buy price is lower that nex price increment the right Index                               l = r
            profit = prices[r] - prices[l]                                                                                         res = max(res, prices[r] - prices[l])
            maxP = max(maxP,profit)
        else:                              # if the buy prices is higher than sell price                                      return res
            l = r
        r += 1
    return maxP

Output: 5

#=============================================================================================================================================================================

2.
