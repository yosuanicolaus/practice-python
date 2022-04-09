class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2 == []:
            self.transfer()
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2 != []:
            return self.s2[-1]
        else:
            return self.s1[0]

    def transfer(self):
        while self.s1:
            self.s2.append(self.s1.pop())

    def empty(self) -> bool:
        return self.s1 == [] and self.s2 == []
