from collections import deque
from typing import List


class TreeNode:
    def __init__(self, v: int, l, r):
        self.val = v
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)
