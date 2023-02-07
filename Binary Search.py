
# NeetCode Challenge
# Solving Problems from NeetCode website, Binary Search

Binary search algorithm basic ideas:

+ The array has to be already sorted
+  divide and conquer technique, which is repeatedly breaks down the array into two subarrays



#=============================================================================================================================================================================

# the time complexity for binary search is (log N), since the while loop is going to run as long as we can divide the input array by 2.

1. Binary search

def search(nums, t):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow. we take R and minus it by L so we get half of distance between L & R Then we add it to left for middle
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1




nums=[-1,0,3,5,9,12]
t =9
search(nums, t)


#=============================================================================================================================================================================

2. Search 2D matrix

def searchmatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot= 0, ROWS-1

    while top <= bot:
        mid_row = (top + bot) // 2
        if target > matrix[mid_row][-1]:        # one case is the target value is greater than the largest value in this row. Then we look at that right most value in that row [row][-1]
            top = mid_row + 1
        elif target < matrix[mid_row][0]:       # one case is the target value is less than the lowest value in this row.
            bot = mid_row - 1

        else:
            break

    if not top <= bot:               # if  non of the rows contain the target return False
        return False
                # if that is not the case we continue to second binary loop
        # this is the row that contain the desire value

    mid_row = (top + bot) // 2

    l, r = 0, COLS - 1

    while l <= r:
        m = (l + r) // 2
        if target < matrix[mid_row][m]:
            r = m - 1
        elif target > matrix[mid_row][m]:
            l = m + 1
        else:
            return True
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
searchmatrix(matrix , target)

# Time complexity : O(log m + log k)
# the time complexity for each
#============================================================================================================================================================================

2. Koko Eating Bananas

# there are tow ways to solve this problem:     1) brute force algorithm             2) Binary search
# 1) we are going to try every single value from one, all the way up until the max value of piles in array,like: [1, ...... , 11] and the time complexity is : O(max(p) * p)

#
Input: piles = [3,6,7,11], h = 8

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p-1)//m) + 1
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k

#============================================================================================================================================================================
