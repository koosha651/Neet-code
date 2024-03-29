
# NeetCode Challenge
# Solving Problems from NeetCode website, Backtracking

# https://www.youtube.com/watch?v=DKCbsiDBN6c

BFS ----- > traversal -------> in a level by level manner                   DFS ----- > traversal -------> in a depth from the root node to bottom (Backtracking)


#=============================================================================================================================================================================

1. Subsets

# for solving this question there are two ways:
# for each input we could include it in the subset or not, so for each input we have two choices, and for an array with 'n' input we have a 2^n choice for our subset.

#  first methods:

nums = [1 ,8, 3]
def subset(nums):
    output = [[]]
    for i in nums:
        output += [lst + [i] for lst in output]
    return output

> > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >

# for more explanation

for i in nums:
        res += [lst  for lst in res]            --------> return : [[], [], [], [], [], [], [], []]



for i in nums:
        res += [[i]  for lst in res]            --------> return : [[], [1], [8], [8], [3], [3], [3], [3]]

 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  second method:

def subsets(nums):

    res = []
    subset = []                 # create this subset list to store the subset and has lobaly access

    def dfs(i):                         # use dfs method to traverse in the graph, 'i' is the indext of the value that we make decision about
        if i >= len(nums):              # if we find out we are out of bounds
            res.append(subset.copy())           # append the current subset to the result. Add copy version of subset because we frequently add value to subset
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)                      # recursively run dfs on the next element

        # decision NOT to include nums[i]       ,        basically we skipping the nums[i]
        subset.pop()            #  remove of pop the element that already appended
        dfs(i + 1)

     dfs(0)         # call the dfs function and give the value '0' to i
     return res    # return the result


#=============================================================================================================================================================================


2. Combination Sum

# we solve this question recursively. Also, define an additional function and pass a few features.
# 'i' represents the which candidate should be chosen / 'cur' represent the values that we already added / 'total' represent the total sum of values in 'cur'

nums = [5,3,6,7]
target = 1

def subset(candidates, target):
    res = []

    def dfs(i , cur , total):
        if total == target:                  # first base case: if the total sum of value will equal to target, add the current value
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:      # second base case: if total value greater that target or the numerator go out of bounds
            return

        # we have two decisions to make: include the value or not

        cur.append(candidates[i])
        dfs(i ,cur,total + candidates[i])      # since the total has been changed by adding candidates[i] to 'cur' we change the pass new total
        cur.pop()
        dfs(i+1 , cur , total)


    dfs(0,[],0)
    return res

subset(nums,target)



#=============================================================================================================================================================================

3. Permutations

# we solve this question recursively.


nums = [1,2,3]

def permute(nums):

    res = []        # create a result list to add the permute number

    if len(nums) == 1:
        return [nums.copy()]    # ** don not forget to put the copy version of nums

    for i in range(len(nums)):       # go through the list and and pop the first elemet
        n = nums.pop(0)
        perms = permute(nums)        # recursively call the function [2,3] [3,2]  ,....

        for perm in perms:
            perm.append(n)           # add 1 to each

        res.extend(perms)           # The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
        nums.append(n)
    return res

permute(nums)

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


#=============================================================================================================================================================================

4. subset II

# this problem is very simal to subset, with little difference in repeated elements. to prevent duplicates in the subset first sort the array.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()


            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:     # if the element in array similar to each other we go to next element
                i += 1
            backtrack(i + 1, subset)        # After we reach to unique element in sorted array, again apply the

        backtrack(0, [])
        return res




#=============================================================================================================================================================================

5.  Combination Sum II

# use the help from

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bact(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            bact(i+1 , cur, total+candidates[i] )
            cur.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            bact(i+1 , cur, total)

        bact(0,[],0)
        return res


#=============================================================================================================================================================================
