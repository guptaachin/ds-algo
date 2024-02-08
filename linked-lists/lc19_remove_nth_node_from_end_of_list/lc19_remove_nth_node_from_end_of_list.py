from typing import Optional
from lib.linked_list import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = None
        prev_left = None
        right = head
        # advance left 1 time if n = 2
        for _ in range(n-1):
            right = right.next

        # please left at head.
        left = head
        prev_left = None

        # advance right until right reaches the end node
        while right.next != None:
            prev_left = left
            left = left.next
            right = right.next
        
        if prev_left == None:
            # left is sitting at head
            head = head.next
        else:
            # drop node at left pointer
            prev_left.next = left.next
        return head
