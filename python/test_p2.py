from typing import List, Optional
import pytest


class ListNode:
    def __init__(self, val=0, next1=None):
        self.val = val
        self.next = next1
    
    def __str__(self):
        string = str(self.val) + ', '
        node = self
        node = node.next
        while node:
            string += str(node.val) + ', '
            node = node.next
        return string


def list_to_node(nums: List[int]) -> ListNode:
    node = first_node = ListNode(nums[0])
    for a_num in nums[1:]:
        node.next = ListNode(a_num)
        node = node.next

    return first_node


def node_to_list(node: ListNode) -> List[int]:
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums

# a = list_to_node([2, 4, 3])
# print(a)
# print(node_to_list(a))

class Solution:
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        def add_node(l11: ListNode, l22: ListNode):
            nonlocal carry
            curr = l11.val + l22.val + carry
            carry = curr // 10
            curr = curr % 10
            return curr
        
        def add_carry(l: ListNode):
            nonlocal carry
            curr = l.val + carry
            carry = curr // 10
            curr = curr % 10
            return curr

        first_node = node = ListNode(add_node(l1, l2))
        while l1 and l2:
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                node.next = ListNode(add_node(l1, l2))
                node = node.next
        
        while l1:
            node.next = ListNode(add_carry(l1))
            l1 = l1.next
            node = node.next
        
        while l2:
            node.next = ListNode(add_carry(l2))
            l2 = l2.next
            node = node.next
        
        if carry:
            node.next = ListNode(carry)

        return first_node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_node = node = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curr = val1 + val2 + carry
            carry = curr // 10
            curr = curr % 10
            node.next = ListNode(curr)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return first_node.next

@pytest.mark.parametrize("list1, list2, answer",
    [
        [[2,4,3], [5,6,4], [7,0,8]],
        [[9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]]
    ]
)
def test_solution(list1, list2, answer):
    node1 = list_to_node(list1)
    node2 = list_to_node(list2)

    node3 = Solution().addTwoNumbers(node1, node2)
    list3 = node_to_list(node3)
    assert list3 == answer
