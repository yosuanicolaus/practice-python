from typing import Optional
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev, curr = None, head

    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev, curr = curr, temp

    #     return prev

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None

    #     new_head = head

    #     if head.next:
    #         new_head = self.reverseList(head.next)
    #         head.next.next = head

    #     head.next = None
    #     return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse_help(head)

    def _reverse_help(self, head, prev=None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        prev = head
        return self._reverse_help(n, prev)


# @lc code=end
