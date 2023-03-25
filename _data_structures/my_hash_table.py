class ListNode:
    def __init__(self, key: int | str, val: int | str, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next


class MyHashTable:
    def __init__(self) -> None:
        self.SIZE = 32
        self.table: list[ListNode] = [None] * self.SIZE

    def hash(self, key: int | str):
        # djb2 hash function
        key = str(key)
        hash_addr = 5381
        for ch in key:
            hash_addr = ((hash_addr << 5) + hash_addr) + ord(ch)
        return hash_addr % self.SIZE

    def add(self, key: int | str, value: int | str):
        table_key = self.hash(key)
        curr = self.table[table_key]
        if not curr:
            self.table[table_key] = ListNode(key, value)
            return
        while curr:
            if curr.key == key:
                curr.val = value
            elif not curr.next:
                curr.next = ListNode(key, value)
                return
            curr = curr.next

    def exist(self, key: int | str):
        table_key = self.hash(key)
        curr = self.table[table_key]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False

    def get(self, key: int | str):
        table_key = self.hash(key)
        curr = self.table[table_key]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return None

    def remove(self, key: int | str):
        table_key = self.hash(key)
        curr = self.table[table_key]
        if not curr:
            return
        if curr.key == key:
            self.table[table_key] = curr.next
            return
        prev, curr = curr, curr.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            curr = curr.next

    def print(self):
        res = []
        for node in self.table:
            while node:
                res.append({node.key: node.val})
                node = node.next
        print(res)


# test = MyHashTable()
# test.add("hello", 234)
# test.add(23, "world")
# test.add("hello", "hehe")

# print(test.exist("notyet"))
# test.add("notyet", "lol")
# print(test.exist("notyet"))

# print(test.get("notyet"))
# print(test.get(23))
# print(test.get(2))

# test.print()
# test.remove(23)
# test.print()
