class ListNode:
    def __init__(self, val, next: 'ListNode' = None) -> None:
        self.val = val
        self.next = next


def remove_duplicates(node: ListNode):
    prev, curr = node, node.next
    seen = set([prev.val])

    while curr:
        if curr.val in seen:
            curr = curr.next
            prev.next = curr
        seen.add(curr.val)
        prev, curr = curr, curr.next
