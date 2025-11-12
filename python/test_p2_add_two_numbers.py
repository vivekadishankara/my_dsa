from typing import Optional, List
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addition = 0
        head = current_head = ListNode()

        while l1 or l2:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            current_val = val1 + val2 + addition
            addition = current_val // 10
            current_head.next = ListNode(current_val % 10)
            current_head = current_head.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        
        if addition > 0:
            current_head.next = ListNode(addition)

        return head.next
    
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recursive_node(l1, l2, addition):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            current_val = val1 + val2 + addition
            if l1 or l2:
                current_head = ListNode(current_val % 10)
            else:
                if addition > 0:
                    current_head = ListNode(addition)
                    return current_head
                else:
                    return None
            addition = current_val // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            current_head.next = recursive_node(l1, l2, addition)

            return current_head

        return recursive_node(l1, l2, 0)

    def create_linked_list(self, numbers: List) -> Optional[ListNode]:
        if not numbers:
            return None
        head = ListNode(numbers[0])
        current = head
        for num in numbers[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

    def print_linked_list(self, head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def covert_list_to_num(self, head: Optional[ListNode]) -> int:
        current = head
        multiplier = 1
        number = 0
        while current:
            number += current.val * multiplier
            multiplier *= 10
            current = current.next
        return number

@pytest.mark.parametrize("l1, l2, answer", [
    [[2,4,3], [5,6,4], 807],
    [[0], [0], 0],
    [[9,9,9,9,9,9,9], [9,9,9,9], 10009998],
])
def test_add_two_nums(l1, l2, answer):
    sol = Solution()
    head1 = sol.create_linked_list(l1)
    head2 = sol.create_linked_list(l2)
    answer_head = sol.addTwoNumbers(head1, head2)
    answer_num = sol.covert_list_to_num(answer_head)
    assert answer_num == answer


@pytest.mark.parametrize("l1, l2, answer", [
    [[2,4,3], [5,6,4], 807],
    [[0], [0], 0],
    [[9,9,9,9,9,9,9], [9,9,9,9], 10009998],
    [[9], [1], 10],
])
def test_add_two_nums1(l1, l2, answer):
    sol = Solution()
    head1 = sol.create_linked_list(l1)
    head2 = sol.create_linked_list(l2)
    answer_head = sol.addTwoNumbers1(head1, head2)
    answer_num = sol.covert_list_to_num(answer_head)
    assert answer_num == answer
