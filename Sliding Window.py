
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

2. Longest Substring Without Repeating Characters

# using sliding window to reduce the time to O(n). because every elementthat we have in array could be unique and for that reason it takes O(n) as well.

input: s = "abcabcbb"                                                                                       s = "abcabcbb"
                                                                                                            chat = set()
def lengthOfLongestSubstring(s: str) -> int:                                                                for i in range(len(s)):
        charSet = set()    # use set() to prevent duolicate in sub set sequence
        l = 0        #  the left will be assign to '0'
        res = 0                                                                                             print(chat) ------> Output: {'a', 'c', 'b'}


        for r in range(len(s)):        # the 'r' will contiguously change
            while s[r] in charSet:       # if we get to a duplicate we have to update our window and our set.
                charSet.remove(s[l])    # update the set by remove the most left element
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)   #find the curent window size by 'r - l +1'
        return res

Output: 3

#=============================================================================================================================================================================
3. Longest Repeating Character Replacement

# we have to use hashmap to store the frequency of alphabet element. How we decide choose the dominet element depends on the most frequent element in our current window. Every
# time we most evaluate this condition that: size of current window  - number of frequency of of top character < = k . If that was passed then we increment the right pointer
# unles increment left pointer.

input: s='ababba'

def characterReplacement(self, s: str, k: int) -> int:
        count = {}   # create hashmap to count the occurance of each element
        res = 0     # give us the longest sub-string

        l = 0 #left pointer

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            if (r - l + 1) - max(count.values()) > k:   #evaluate the condition and make sure its valid
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)       #if it passed the condition choose the maximum lenght of substring
        return res

output: 5       time complexity: O(26n) 26 position for 26 alphabet

#=============================================================================================================================================================================
