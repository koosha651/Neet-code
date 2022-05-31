
# NeetCode Challenge
# Solving Problems from NeetCode website, Tow Pointers

# 1. Valid Palindrome
# Two ways to solve the problem. First method use extra memory. Second methods 

s = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    strs= ''
    for c in s:
        if c.isalnum():
            strs += c.lower()
    return strs == strs[::-1]
        
