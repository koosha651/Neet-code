
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

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap , self.k = nums , k        # first create member variable. a min-heap with list of number and the value 'k'
        heapq.heapify(self.minHeap)             # create heap by list of numbers
        while len(self.minHeap) > k:            # while lenght of min-heap is larger than 'k' pop the min
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)       # add value to heap

        if len(self.minHeap) > self.k:          # if current lenght of min-heap is larger than 'k' return the minimum which store in the [0] place
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

#=============================================================================================================================================================================

2. Last Stone Weight

# since we dealing with maximum value, need to implement max-Heap. In order to take list of array and turn them to max-heap it takes O(n). every time we get the max it takes
# O(log n ). since python doesn't have Max-Heap, we multiple -1 into every element and get minimum amount.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


#=============================================================================================================================================================================
