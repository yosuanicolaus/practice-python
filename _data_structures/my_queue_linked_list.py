class ListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class MyQueue:
    def __init__(self) -> None:
        self.tail = ListNode(None)
        self.head = ListNode(None, self.tail)
        self.tail.prev = self.head
        self.size = 0

    def enqueue(self, data):
        node = ListNode(data)
        temp = self.tail.prev
        temp.next = node
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def dequeue(self):
        temp = self.head.next
        self.head.next = temp.next
        data = temp.data
        del temp
        self.size -= 1
        return data

    def empty(self):
        temp = self.head.next
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        while temp != self.tail:
            nxt = temp.next
            del temp
            temp = nxt

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        temp = self.head.next
        while temp.data != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()


def main():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    q.print_queue()
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(10)
    q.print_queue()

    q.empty()
    q.enqueue(30)
    q.print_queue()


if __name__ == "__main__":
    main()
