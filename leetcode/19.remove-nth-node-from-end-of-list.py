#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr, future = dummy, head

        for _ in range(n):
            future = future.next

        while future:
            curr = curr.next
            future = future.next

        curr.next = curr.next.next
        return dummy.next

# @lc code=end
