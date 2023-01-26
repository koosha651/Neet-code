
# NeetCode Challenge
# Solving Problems from NeetCode website, Tow Pointers

1. Valid Palindrome
# Two ways to solve the problem. First method use extra memory by building 'newstr'

s = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    newstr= ''
    for c in s:
        if c.isalnum():
            newstr += c.lower()
    return strs == strs[::-1]


# Second methods use two pointers to compare start and end of string untill they meet eachother. Time complexity is O(n) but memory is O(1)
def isPalindrome(s: str) -> bool:
    l,r= 0,len(s)-1
    while l<r:
        while l<r and not self.alphaNum(s[l]):
            l+=1
        while r>r and not self.alphaNum(s[r]):
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l.r = l+1 , r-1
    return True


def alphaNum(c):                                    # Could write own alpha-numeric function
    return (ord('A') <= ord(c) <= ord('Z')
            ord('a') <= ord(c) <= ord('z')
            ord('0') <= ord(c) <= ord('9'))


#=============================================================================================================================================================================


2. Two Sum II - Input Array Is Sorted
#                                                           Dictionary: O(n) time       O(n) space
# we could solve like Two sum in Arrays & Hashing but:      Two pointers: O(n) time       O(1) space  ✔
#                                                           Binary search: O(nlogn) time   O(1) space

numbers = [2,3,4]
target = 6

def two_sum(num,t):

    l,r = 0,len(numbers)-1
    while l<r:
        cur_sum = num[l] + num[r]
        if cur_sum < t:
            l+=1
        elif cur_sum > t:
            r-=1
        else:
            return (l+1,r+1)

#=============================================================================================================================================================================

3. 3Sum

 # By sorting the Array O(n log n) for find the First number and use 2 loops to find the two Sum by two pointers, total time complexity will be : O (n log n) + O (n^2) which
 # will be O (n^2)
 
 # sort() ----> sort the list in-place & returning None (can only be used with lists)  : nums.sort()
 
 # sorted() -----> sort the list & return a new sorted list : sorted(a)

Input: nums = [-1,0,1,2,-1,-4]

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res=[]
    nums.sorted()         # The time complexity of sorting the array:  O(n log n)

    for index , value in enumerate(nums):
        if index > 0 and nums[index] == nums[index-1]:   # after sorting, check if 'i' will not be a first position, also check if the previous number are the same
            continue

        l,r = index+1 , len(nums)-1      # define two Pointers
        while l<r:          # check for each time to Pointers not pass from eachother
            crt_Sum = nums[index] + nums[l] + nums[r]   # current sum of 3 numbers and then check whether it bigger or smaller than 0.
            if crt_Sum < 0:
                l+=1
            elif crt_Sum > 0:
                r-=1
            else:
                res.append([nums[index] , nums[l] , nums[r]]) # we ahve to print the answer in a List

                # now we have to update our pointers to examine other combinations. E.g [-2 ,-2, 0, 0, 2, 2] in this array we can update two pointers but that is not necessary,
                # so we only update the Left pointers and if the current 3sum has not changed, it will automatically use the previous If statement in the while loop
                # to update the Right pointer

                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1

    return res

Output: [[-1,-1,2],[-1,0,1]]



#=============================================================================================================================================================================

11. Container With Most Water

# for solving this question show look at the pattern between heights. 

height = [1,8,6,2,5,4,8,3,7]


def maxArea(height):
    # BRUTE FORCE
    res = 0
    
    for l in range(len(height)):
        for r in range(l+1 , len(height)):
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
    return res

maxArea(height)

# TIME COMPLEXITY = O(n^2)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    
    res = 0
    l,r = 0 , len(height)-1     # two pointers, left init as 0, right init as size-1
    
    while l< r:
        area = (r-l) * min(height[l], height[r])    # (width between) * (minimum height of the leftmost stick and rightmost stick)
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

maxArea(height)

# linearn time solution: O(n)


#=============================================================================================================================================================================
