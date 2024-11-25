from collections import deque


class MyQueue:
    def __init__(self):
        self.stk1 = deque()
        self.stk2 = deque()

    def push(self, e):
        self.stk1.append(e)

    def pop(self):
        if len(self.stk2) == 0:
            while len(self.stk1) > 0:
                self.stk2.append(self.stk1.pop())
        return self.stk2.pop()


if __name__ == "__main__":
    # 1 2 3
    m = MyQueue()
    m.push(1)
    print(m.pop())
    m.push(2)
    m.push(3)
    print(m.pop())
    print(m.pop())
