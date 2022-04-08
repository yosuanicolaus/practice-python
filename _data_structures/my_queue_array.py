class MyQueue:
    def __init__(self, capacity=8) -> None:
        self.array = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.read_pt, self.write_pt = 0, 0

    def enqueue(self, value):
        self.array[self.write_pt] = value
        self.write_pt = (self.write_pt + 1) % self.capacity
        self.size += 1
        if self.size > self.capacity:
            self.size = self.capacity
        if self.size == self.capacity and self.write_pt > self.read_pt:
            self.read_pt = self.write_pt

    def dequeue(self):
        data = self.array[self.read_pt]
        if data == None:
            raise 'empty queue!'
        self.array[self.read_pt] = None
        self.read_pt = (self.read_pt + 1) % self.capacity
        self.size -= 1
        return data

    def empty(self):
        self.array = [None] * self.capacity
        self.size = 0
        self.read_pt, self.write_pt = 0, 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print_queue(self):
        print(self.array, f'read-{self.read_pt}',
              f'write-{self.write_pt}', f'size-{self.size}')


def main():
    # default capacity = 8
    q = MyQueue()

    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(13)
    q.enqueue(13)

    q.print_queue()

    print(q.dequeue())
    q.print_queue()

    q.empty()
    q.print_queue()
    print(q.is_empty())

    for i in range(12):
        q.enqueue(101 + i)

    print(q.is_full())
    q.print_queue()


if __name__ == "__main__":
    main()
