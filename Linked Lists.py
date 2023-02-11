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

        while cur:          # we want to keep going untill we reach the end of the List

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

# Linked Lists with Dummy Nodes: https://www.youtube.com/watch?v=3O_f_sk3mFc&t=12s
