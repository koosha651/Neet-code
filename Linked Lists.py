# NeetCode Challenge
# Solving Problems from NeetCode website, Linked Lists

https://www.youtube.com/watch?v=njTh_OwMljA&t=141s


#=============================================================================================================================================================================

1. Reverse Linked List

# Total time complexity is : O(n)
# Total memory complexity :  O(1)

method_#1: Iterative                                                                                method_#2: Recursive

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, cur = None, head

        while cur:          # we want to keep going until we reach the end of the List

            # locate next hoppoing node
            next_hop = cur.next

            # reverse direction
            cur.next = prev

            # reverse pointers
            prev = cur
            cur = next_hop

        # new head of reverse linked list
        return prev


 #=============================================================================================================================================================================
2. Merge Two Sorted Lists


# for solving this QUESTION we used the dummy node:  Linked Lists with Dummy Nodes: https://www.youtube.com/watch?v=3O_f_sk3mFc&t=12s


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()      #create a dummy and do not worry about edge cases of inserting into a empty list
        tail = dummy            # connect the dummy node to the tail

        while list1 and list2:      #for iterating through these two list the condition is both of them are non empty
            if list1.val < list2.val:       # check the value in each lists
                tail.next = list1   # import the list 1 to tail
                list1 = list1.next       #update a list1 to next Node
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next          #update a tail to next Node

        if list1:       #we check if either of list still has value and in that case add them to end of the tail
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next       # at the end return the list

 #=============================================================================================================================================================================

3. Reorder List


# we solve this question in 3 steps         1. Finding the middle       2. reversing the pointers in the second half of list        3. merging two half


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


 #=============================================================================================================================================================================

4. Remove Nth Node From End of List

# For solving this question at first, you might think by reversing the list and starting from the end; we don't need to do that. what we need to do is use two pointers method
# We create a dummy node and define the gap between the left and right pointer by 'n' distance.

# 1- define dummy node      2. define 'n' distance gap between l and r      3. update Pointers       4.  delete the desired Node


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head) # define dummy node with the value of 0 and the next pointer will be head
        left = dummy        # assigne left and right pointers
        right = head

        while n > 0:        # continue to shift until 'n' be Zero
            right = right.next
            n -= 1

        while right:        # until the right pointer is not equal to Nall continue updating the pointers
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next      #L      ---->  # L -> 2 -> 3 duble shift
        return dummy.next


 # Total time complexity is: O(n)

 #=============================================================================================================================================================================

5. Copy the List with Random Pointer

# we iterate two times through the list:

# First loop for creating a deep copy of the nodes by using hashmap to map the original node to the new node.
# Second loop for connecting pointers and leveraging the hashmap to connect every old node to a new node

# 1- create hashmap for deep copy     2. iterate through 1sth loop for copy     3. iterate through 2end loop for setting Pointers

"""
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}        # create hashmap for mapping        /   don't forget to define the edge case in the second loop if the next point is null
        cur = head

        # First loop for creating a deep copy
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head      # reassigning the current to head

        # second loop for set next & random pointers
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]



 # Total time complexity is: O(n)

 #=============================================================================================================================================================================


6. Add Two Numbers

"""
This question contains lots of edge cases that need to be addressed:
    - for each digit, we have to create separate nodes like: 34 --> _ _ (2 digits)
    - if either of the two numbers has a different size like: 12 + 1245
    - Use a carry to store the second digit after sum up two numbers like: '1'4 = 5 + 9 ('1' is carry )
"""

1. create a dummy node  2.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy     # current pointer is the point at the position that we inserting a new node or new digit into / also if our carrier is not Null we continue the loop eg(7 + 8)

        carry = 0
        while l1 or l2 or carry:            # we will iterate through each list until either of them has a digit
            v1 = l1.val if l1 else 0    # v1 is going to be the digit of list 1 only if l1 is not Null / else will set it to Zero
            v2 = l2.val if l2 else 0

            # compute the new digit
            val = v1 + v2 + carry       # after this we can have a new carry, so:
            carry = val // 10       # we have to get the carry out of that
            val = val % 10
            cur.next = ListNode(val)    # now we can insert a new list node with the value that we just computed

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next



 #=============================================================================================================================================================================
