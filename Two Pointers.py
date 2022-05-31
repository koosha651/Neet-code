
# NeetCode Challenge
# Solving Problems from NeetCode website, Tow Pointers

# 1. Valid Palindrome
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
