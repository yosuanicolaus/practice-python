'''
 Implement a vector (mutable array with automatic resizing):

    Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
    New raw data array with allocated memory
        can allocate int array under the hood, just not use its features
        start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
    size() - number of items
    capacity() - number of items it can hold
    is_empty()
    at(index) - returns item at given index, blows up if index out of bounds
    push(item)
    insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
    prepend(item) - can use insert above at index 0
    pop() - remove from end, return value
    delete(index) - delete item at index, shifting all trailing elements left
    remove(item) - looks for value and removes index holding it (even if in multiple places)
    find(item) - looks for value and returns first index with that value, -1 if not found
    resize(new_capacity) // private function
        when you reach capacity, resize to double the size
        when popping an item, if size is 1/4 of capacity, resize to half

'''


class MyVector:
    def __init__(self, *args) -> None:
        self.array = [None] * 16
        self.arr_size = 0
        self.arr_capacity = 16
        self.idx_pointer = 0

        for arg in args:
            self.array[self.idx_pointer] = arg
            self.idx_pointer += 1
            self.arr_size += 1

    def size(self):
        return self.arr_size

    def capacity(self):
        return self.arr_capacity

    def is_empty(self):
        return self.arr_size == 0

    def at(self, idx):
        if idx >= self.arr_size:
            raise 'index out of bonds!'
        self.idx_pointer = idx
        return self.array[self.idx_pointer]

    def check_new_size(self, new_size):
        if new_size > self.arr_capacity:
            self._resize(self.arr_capacity * 2)
        elif new_size <= self.arr_capacity // 4:
            self._resize(self.arr_capacity // 2)

    def push(self, item):
        self.check_new_size(self.arr_size + 1)
        self.idx_pointer = self.arr_size
        self.array[self.idx_pointer] = item
        self.idx_pointer += 1
        self.arr_size += 1

    def insert(self, idx, item):
        self.check_new_size(self.arr_size + 1)
        self.idx_pointer = idx
        temp = self.array[self.idx_pointer]
        while temp:
            temp = self.array[self.idx_pointer]
            self.array[self.idx_pointer] = item
            item = temp
            self.idx_pointer += 1
        self.arr_size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        self.idx_pointer = self.arr_size - 1
        pop = self.array[self.idx_pointer]
        self.array[self.idx_pointer] = None
        self.arr_size -= 1
        self.check_new_size(self.arr_size)
        return pop

    def delete(self, index):
        self.idx_pointer = index
        while self.array[self.idx_pointer] != None:
            self.array[self.idx_pointer] = self.array[self.idx_pointer + 1]
            self.idx_pointer += 1
        self.arr_size -= 1
        self.check_new_size(self.arr_size)

    def remove(self, item):
        self.idx_pointer = 0
        while self.array[self.idx_pointer] != None:
            if self.array[self.idx_pointer] == item:
                self.delete(self.idx_pointer)
                break
            self.idx_pointer += 1

    def find(self, item):
        self.idx_pointer = 0
        while self.array[self.idx_pointer] != None:
            if self.array[self.idx_pointer] == item:
                return self.idx_pointer
            self.idx_pointer += 1

    def _resize(self, new_capacity):
        diff = abs(new_capacity - self.arr_capacity)
        if self.arr_capacity < new_capacity:
            self.array += [None] * diff
        elif self.arr_capacity > new_capacity:
            self.array = self.array[:-diff]
        self.arr_capacity = new_capacity

    def print_arr(self):
        print(self.array, self.idx_pointer)


def main():
    vec = MyVector(*list(range(9)))

    vec.print_arr()

    for i in range(10):
        vec.push(100)
    vec.print_arr()

    for i in range(14):
        vec.push(666)
    vec.print_arr()

    for i in range(17):
        vec.pop()
    vec.print_arr()


if __name__ == "__main__":
    main()
