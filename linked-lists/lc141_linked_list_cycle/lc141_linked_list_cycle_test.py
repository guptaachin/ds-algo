# This code was AUTOGENERATED.
# Change it to fit your test case.
import lc141_linked_list_cycle
import pytest
from lib.linked_list import LinkedList

# create no loop linked list
no_loop_ll = LinkedList([1,2,3,4])
# create loop linked list
loop_ll = LinkedList([1,2,3,4,5,6])
loop_ll.get_ith_node(5).next = loop_ll.get_ith_node(3)

@pytest.mark.parametrize(
    ("head", "result"),
    [
        # parametrized test case 1
        (no_loop_ll.head, False),
        (loop_ll.head, True),
    ]
)

def test_problem(head, result):
    s = lc141_linked_list_cycle.Solution()
    assert s.hasCycle(head) == result
