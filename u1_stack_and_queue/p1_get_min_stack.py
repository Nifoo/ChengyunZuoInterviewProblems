from collections import deque


class MinStk:
    def __init__(self):
        self.stk = deque()
        self.min_stk = deque()

    def push(self, e):
        self.stk.append(e)
        if len(self.min_stk) == 0 or e <= self.min_stk[-1]:
            self.min_stk.append(e)

    def pop(self):
        if len(self.min_stk) == 0:
            return None
        p = self.stk.pop()
        if p == self.min_stk[-1]:
            self.min_stk.pop()
        return p

    def get_min(self):
        if len(self.min_stk) == 0:
            return None
        return self.min_stk[-1]


if __name__ == "__main__":
    m = MinStk()
    # Expect: 1 1 0 1
    m.push(1)
    print(m.get_min())
    m.push(2)
    print(m.get_min())
    m.push(0)
    print(m.get_min())
    m.pop()
    print(m.get_min())
