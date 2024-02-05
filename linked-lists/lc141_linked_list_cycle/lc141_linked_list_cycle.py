from typing import Optional
from data_structures.linked_list import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        s = head
        f = head.next
        while f != None and f.next != None:
            if s == f:
                return True
            s = s.next
            f = f.next.next
        return False

