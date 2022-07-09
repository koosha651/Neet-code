
# NeetCode Challenge
# Solving Problems from NeetCode website, Trees

https://www.youtube.com/watch?v=7tCNu4CnjVc

https://www.educative.io/answers/how-to-implement-a-breadth-first-search-in-python -------->  Implement BFS

#=============================================================================================================================================================================

1. Invert Binary Tree

# the conceot is to visit every single node in the tree and then if each of these nodes has children, we must swap their children. So we can sove this problem with recursion
# as DFS


Input: root = [4,2,7,1,3,6,9]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:                #check the base case whether the root is null. if it's null then return Null
            return None

        # swap the children
        tmp = root.left                                 # otherwise swap the children
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


Output: [4,7,2,9,6,3,1]


#=============================================================================================================================================================================

2. Maximum Depth of Binary Tree

# there are 3 ways to solve:   1. recursive DFS         2. Iterative DFS            3. BFS

#1. recursive DFS: in this method start from the root & and look for max for leaf and in each node '1 + max( DFS(left) , DFS(right) )'. Time complexity & memory usage = O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))


#=============================================================================================================================================================================

3. Diameter of Binary Tree

# Using Recursive Approach to calculating the Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/discuss/1515564/Python-Easy-to-understand-solution-w-Explanation
# The depth of a node is the number of edges from the node to the tree's root node
# The height of a node is the number of edges on the longest path from the node to a leaf.
# The diameter (or width) of a tree is the number of nodes on the longest path between any two leaf nodes.


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = [0]

        def dfs(root):
            if not root:
                 return 0
            left = dfs(root.left)           # recurcivly find the hight of left sub tree
            right = dfs(root.right)         # recurcivly find the hight of right sub tree
            res[0] = max(res[0], left + right)          # calculating the diameter by adding two hight

            return 1 + max (right , left)           #return the hights

        dfs (root)
        return res[0]


#=============================================================================================================================================================================
4. Balanced Binary Tree

#we recursivly start from bottum on the tree and return two value. first value is bolian value(true/false)that tell if the node is balance and the hight of the current node.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):  # this function return pair of values, boolean and the hight of a tree. [bolian value(whetherthe tree is balance or not) , current hight of Tree]
            if not root: return [True, 0]       # since empty tree means balance, then return true for that.

            left, right = dfs(root.left), dfs(root.right)       #allocate the value for left and right subtree
            balanced = (left[0] and right[0] and    #check the difference of the two leaf will not be more that 1, also check if the left and right leaf are already Balanced
                        abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
