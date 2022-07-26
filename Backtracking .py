
# NeetCode Challenge
# Solving Problems from NeetCode website, Backtracking

# https://www.youtube.com/watch?v=DKCbsiDBN6c

BFS ----- > traversal -------> in a level by level manner                   DFS ----- > traversal -------> in a depth from the root node to bottom (Backtracking)


#=============================================================================================================================================================================

1. Subsets

# for solving this question there are two ways:
# for each input we could include it in the subset or not, so for each input we have two choice and for array with 'n' input we have 2^n choice for our subset.

#  first methods:

nums = [1 ,2, 3]
def subset(nums):
    output = [[]]
    for i in nums:
        output += [lst + [i] for lst in output]
    return output


for i in nums:
        res += [lst  for lst in res]            --------> return : [[], [], [], [], [], [], [], []]



for i in nums:
        res += [[i]  for lst in res]            --------> return : [[], [1], [8], [8], [3], [3], [3], [3]]

 #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  second method:

def subsets(nums):

    res = []
    subset = []
    
    def dfs(i):
        if i >= len(nums):              # if we find out we are out of bounds
            res.append(subset.copy())           # append the current subset to the result
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

     dfs(0)         # call the dfs function and give the value '0' to i
     return res    # return the result


#=============================================================================================================================================================================


2. Combination Sum
