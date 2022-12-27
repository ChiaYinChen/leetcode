"""
0206. Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre, curr = None, head
        while curr is not None:
            _next = curr.next
            curr.next = pre
            pre = curr
            curr = _next
        return pre
