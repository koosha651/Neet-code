
# NeetCode Challenge
# Solving Problems from NeetCode website, Binary Search


1. Binary search

def search(nums, t):
    l, r=0, len(nums)-1


    while(l <= r):
        mid=int((l+r)/2)

        if nums[mid] == t:
            return mid
        elif nums[mid] < t:
            l=mid +1

        else:
            r= mid - 1
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

Time complexity : O(log m + log k)

#============================================================================================================================================================================
