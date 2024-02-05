class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, list_vals):
        self.head = ListNode(list_vals[0])
        current = self.head
        for i in range(1, len(list_vals)):
            current.next = ListNode(list_vals[i])
            current = current.next

    def get_ith_node(self, i):
        current = self.head
        for _ in range(i-1):
            if current == None:
                return None
            current = current.next
        return current
