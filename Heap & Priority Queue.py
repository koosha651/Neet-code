
# NeetCode Challenge
# Solving Problems from NeetCode website, Heap & Priority Queue

# by adding ' import heapq ' library, can use the heap 
arr[(k - 1)/2] will return the parent node   
arr[(2*k) + 1] will return left child
arr[(2*k) + 2] will return right child
#=============================================================================================================================================================================
1. Kth Largest Element in a Stream

# Basicly the question ask us to return 'k' largest element in list our number. Stream means we can continue adding number to our list.  
# Main reason that use Heap is that we can do add\pop in O(log n) time and get the min value in O(1). using binary search take O(lon n) to sort and O(n) to add value to array.
# 1: take number & add it ti min-Heap 
# 2: use while loop whhich while the size of heap is greater than 'K' pop the min value
# add number --(in)--> O(log n) time --(adding 'm' times)--> O(m log n) time
# pop number --(in)--> O(log n) time --(pop 'k' times)--> O((n - k) log n) time

