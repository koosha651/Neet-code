# NeetCode Challenge
#Solving Problem from NeetCode website

# 1. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/submissions/)
if len(nums) != len(set(nums)): #set() prevents redundancy  
    return True

# 2. Valid Anagram

# we should 2 hash map and the total time complexity will be len(s) + len(t)