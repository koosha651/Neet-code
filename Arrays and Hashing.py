# NeetCode Challenge
# Solving Problems from NeetCode website, Arrays & Hashing

# 1. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/submissions/)
if len(nums) != len(set(nums)): #set() prevents redundancy
    return True

#=============================================================================================================================================================================

# 2. Valid Anagram
# we should create 2 hashmaps and the total time complexity will be O(S + T) which is the iteration in these tow hashmaps. **Downside: potential high memory usage**


countS , countT = {},{}     #defining two seperate hash table for each list and check whether they are have same length
if len(s)!= len(T):
    return False
for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i],0)   #each time we see a character we want to increment that by 1 and 0 if that charecter has not appereard
    countT[t[i]] = 1 + countT.get(t[i],0)

for c in countS:
    if countS[c] != countT.get(c,0):
        return False
return True
#  /////////////////////////////
return Counter(s) == Counter(t)
# /////////////////////////////
return sorted(s)==sorted(t)  # use seaching algorithm time complexity O(n^2)


#=============================================================================================================================================================================


# 3. Two Sum
# we're looking for indices, so sorting is not necessary. Mostly using dictionary (hastable) helps.
# More information in  ( https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation )

def Two_sum(nums,target):
    seen={}
    for index , value in enumerate (nums) :    # enumerate gives U both index and value of element
        remain = target - nums[index]          # Since remaining + value = target
        if remain in seen:
            return (seen[remain],index)        # If true you are done, and your current Index and remaining from seen is the answer
        else:
            seen[value]=index                  # Otherwise, add current number to dictunary

nums=[11,2,15,7]
Two_sum(nums,9)


#=============================================================================================================================================================================


# 4.  Group Anagrams
# Need to know Defaultdic: https://www.youtube.com/watch?v=zTHtUm4AtcA

Name= 'Hashing technique'                      from collections import defaultdict

seen={}                                        Name= 'Hashing technique'
for char in name:                              seen={}
    if char not in seen:

        seen[char]=1                           seen=defaultdict(int)   or    seen=defaultdict(lambda:0) # gives the intial value

    else:                                      for char in name:
        seen[char]+=1                               seen[char]+=1

output: {'K': 1, 'o': 2, 's': 1, 'h': 2, 'a': 3, ' ': 1, 'S': 1, 'r': 1, 'i': 2, 'f': 1, 'n': 1}


# for soving this problem: we creat a hashmap and count the number of each charter in each word like eat={'e':1,'a':1,'t':1}then add words with same combination such as 'ate'.
# then we use{'e':1,'a':1,'t':1} as key and stor the words as values() in our dictunary. the time complexity would be O(m.n) whcih 'm' is totalnumber of input string, 'n' is
# avarge len of each word.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res=defaultdict(list) #mapping the chracter count of ech word in our array , also the default value is 'list'
        for word in strs:
            count=[0]*26   #opening 26 zeros for each 26 alphabet: a...z

            for token in word:                    #a=80 ->0, 80 - 80 =0   b=81 ->1, 81 - 80 =0
                count[ord(token) - ord('a')]+=1   # we are just counting how many charecter we have
            res[tuple(count)].append(word)        # add the

        return res.values()


#=============================================================================================================================================================================


# 5. Top K Frequent Elements

# There are several methods to solve this problem such as heap max O(k log n) , bucket sort O(n). in Bucket sort the first row of array represent the number of occurance of
# each element, and the second row is the elements whit the same number of occurance. For Array like : [1,2,1,1,100,2] we have:
 [1]   , [2] , [3] , [4] , [5], [6]
=====================================
[100]  , [2] , [1] ,  [] , []  ,  []



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # Use hashmam to count the occurance of element
        freq = [[] for i in range(len(nums) + 1)] # has exact length of the input array, the indexes represent number of occurance and the value are the lsit of number

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)   # our output right here is [[], [3], [], [1, 2], [], [], [], []] and we have to go through the array


        res = []
        for i in range(len(freq) - 1, 0, -1):  # we have to start from the last index and go to '0' index with '-1' step as decrementer
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n) the time complexity
