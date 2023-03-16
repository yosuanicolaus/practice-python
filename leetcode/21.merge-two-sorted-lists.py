from typing import Optional
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            curr, o1, o2 = list1, list1.next, list2
        else:
            curr, o1, o2 = list2, list1, list2.next
        begin = curr

        while curr:
            if not o1:
                curr.next = o2
                break
            if not o2:
                curr.next = o1
                break

            if o1.val <= o2.val:
                curr.next = o1
                curr, o1 = o1, o1.next
            else:
                curr.next = o2
                curr, o2 = o2, o2.next

        return begin


# @lc code=end
