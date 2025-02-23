from collections import deque
from typing import List


class TreeNode:
    def __init__(self, v: int, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    @staticmethod
    def build_an_example_tree():
        #                        /4
        #              /2
        #                                  /5
        #                        \3
        #    0
        #              \1

        rt0 = TreeNode(0, None, None)
        rt1 = TreeNode(1, None, None)
        rt2 = TreeNode(2, None, None)
        rt3 = TreeNode(3, None, None)
        rt4 = TreeNode(4, None, None)
        rt5 = TreeNode(5, None, None)

        rt0.left = rt1
        rt0.right = rt2
        rt2.left = rt3
        rt2.right = rt4
        rt3.right = rt5
        return rt0
