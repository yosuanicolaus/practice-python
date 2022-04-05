class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, previous_node, new_data):
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        found = False

        if temp.data == key:
            self.head = temp.next
            del temp
            return

        while (temp):
            if temp.data == key:
                found = True
                break
            prev = temp
            temp = temp.next

        if found:
            prev.next = temp.next
            del temp

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' - ')
            temp = temp.next
        print()


def main():
    foo = LinkedList()
    foo.head = Node(10)
    second = Node(15)
    third = Node(20)
    fourth = Node(25)

    foo.head.next = second
    second.next = third
    third.next = fourth

    foo.print_list()  # 10 15 20 25
    foo.push(1000)
    foo.print_list()  # 1000 10 15 20 25
    foo.insert_after(second, 17)
    foo.print_list()  # 1000 10 15 17 20 25
    foo.append(999)
    foo.print_list()  # 1000 10 15 17 20 25 999

    foo.delete_node(1000)
    foo.print_list()  # 10 15 17 20 25 999


if __name__ == "__main__":
    main()
