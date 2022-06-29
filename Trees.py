
# NeetCode Challenge
# Solving Problems from NeetCode website, Trees

https://www.youtube.com/watch?v=7tCNu4CnjVc

#=============================================================================================================================================================================

1.  Invert Binary Tree

# the conceot is to visit every single node in the tree and then if each of these nodes has children, we must swap their children. So we can sove this problem with recursion as DFS

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