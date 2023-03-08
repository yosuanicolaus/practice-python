from typing import Union


class ListNode:
    def __init__(self, key: int, val: int, nxt) -> None:
        self.key = key
        self.val = val
        self.next = nxt


class MyHashMap:
    def __init__(self):
        self.size = 19997
        self.mult = 12582917
        self.data: list[Union[ListNode, None]] = [
            None for _ in range(self.size)]

    def hash(self, key: int):
        return key * self.mult % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key, value, self.data[h])
        self.data[h] = node

    def get(self, key: int) -> int:
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        node = self.data[h]
        if node == None:
            return
        if node.key == key:
            self.data[h] = node.next
            return
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
