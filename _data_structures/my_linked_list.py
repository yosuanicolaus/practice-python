class ListNode:
    def __init__(self, data=0, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self, *values) -> None:
        self.head = ListNode(None)
        self.tail = ListNode(None, self.head)
        self.head.next = self.tail
        self.list_size = 0

        for value in values:
            self.push_back(value)

    def size(self) -> int:
        return self.list_size

    def empty(self) -> bool:
        return self.list_size == 0

    def value_at(self, index: int) -> int:
        index = self._convert_index(index)
        temp = self.head
        while index >= 0:
            temp = temp.next
            index -= 1
        return temp.data

    def _first_push(self, data: int) -> None:
        self.head.next = ListNode(data, self.tail, self.head)
        self.tail.prev = self.head.next

    def _convert_index(self, index: int) -> int:
        if index >= self.list_size or index < -self.list_size:
            raise('index out of range!')
        if index < 0:
            index = self.list_size + index
        return index

    def push_front(self, data: int) -> None:
        if self.list_size == 0:
            self._first_push(data)
        else:
            current_first = self.head.next
            new_first = ListNode(data, self.head, current_first)
            current_first.prev = new_first
            self.head.next = new_first
        self.list_size += 1

    def pop_front(self) -> int:
        to_pop = self.head.next
        self.head.next = to_pop.next
        to_pop.next.prev = self.head
        data = to_pop.data
        self.list_size -= 1
        del to_pop
        return data

    def push_back(self, data: int) -> None:
        if self.list_size == 0:
            self._first_push(data)
        else:
            prev = self.tail.prev
            new_node = ListNode(data, prev, self.tail)
            prev.next = new_node
            self.tail.prev = new_node
        self.list_size += 1

    def pop_back(self) -> int:
        pop = self.tail.prev
        prev = pop.prev
        prev.next = self.tail
        self.tail.prev = prev
        data = pop.data
        self.list_size -= 1
        del pop
        return data

    def front(self) -> int:
        return self.head.next.data

    def back(self) -> int:
        return self.tail.prev.data

    def insert(self, index: int, data: int) -> None:
        index = self._convert_index(index)
        temp = self.head
        while index >= 0:
            temp = temp.next
            index -= 1
        new_node = ListNode(data, temp.prev, temp)
        temp.prev.next = new_node
        temp.prev = new_node
        self.list_size += 1

    def erase(self, index: int) -> None:
        index = self._convert_index(index)
        temp = self.head
        while index >= 0:
            temp = temp.next
            index -= 1
        # remove temp
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.list_size -= 1
        del temp

    def value_n_from_end(self, n: int) -> int:
        return self.value_at(-n)

    def reverse(self) -> None:
        prev, curr = self.head, self.head.next

        while curr.data != None:
            nxt = curr.next

            curr.next = prev
            curr.prev = nxt
            prev = curr
            curr = nxt

        self.tail.prev = self.head.next
        self.head.next = prev

    def remove_value(self, value: int) -> None:
        temp = self.head
        while temp.next.data != None:
            temp = temp.next
            if temp.data == value:
                if self.front() == temp.data:
                    self.head.next = temp.next
                elif self.back() == temp.data:
                    self.tail.prev = temp.prev
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del temp
                self.list_size -= 1
                break

    def print_list(self) -> None:
        temp = self.head
        print('- ', end='')
        while temp.next.data != None:
            print(temp.next.data, end=' - ')
            temp = temp.next
        print()

    def print_reverse_list(self) -> None:
        temp = self.tail
        print('(r) ', end='')
        while temp.prev.data != None:
            print(temp.prev.data, end=' - ')
            temp = temp.prev
        print()


def main():
    foo = MyLinkedList(3, 5, 7, 11, 23)

    foo.insert(2, 666)

    foo.print_list()


if __name__ == "__main__":
    main()
