
# NeetCode Challenge
# Solving Problems from NeetCode website, Trees

https://www.youtube.com/watch?v=7tCNu4CnjVc

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