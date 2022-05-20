# NeetCode Challenge
#Solving Problem from NeetCode website

# 1. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/submissions/)
if len(nums) != len(set(nums)): #set() prevents redundancy  
    return True

# 2. Valid Anagram
#we should create 2 hashmaps and the total time complexity will be O(S + T) which is the iteration in these tow hashmaps. **Downside: potential high memory usage**


countS , countT = {},{}     #defining two seperate hash table for each list and check whether they are have same length 
if len(s)!= len(T): 
    return False
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)
        
    for c in countS:
        if countS[c] != countT.get([c],0):
            return False
    return True
#  /////////////////////////////
return Counter(s) == Counter(t)
# /////////////////////////////
return sorted(s)==sorted(t)  # use seaching algorithm time complexity O(n^2)                
        
