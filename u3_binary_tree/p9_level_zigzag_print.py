from collections import deque

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def level_print(rt: TreeNode):
    dq = deque([])
    dq.append(rt)
    l = 0
    while dq:
        dq_nxt = deque([])
        l += 1
        print("Level %d:" % l, end=" ")
        while dq:
            x = dq.popleft()
            print(x.val, end=" ")
            if x.left:
                dq_nxt.append(x.left)
            if x.right:
                dq_nxt.append(x.right)
        print()
        dq = dq_nxt


def zigzag_print(rt: TreeNode):
    dq = deque([])
    dq.append(rt)
    l = 0
    while dq:
        dq_nxt = deque([])
        l += 1
        print("Level %d:" % l, end=" ")
        while dq:
            x = dq.popleft() if l % 2 == 1 else dq.pop()
            print(x.val, end=" ")
            if l % 2 == 1:
                if x.left:
                    dq_nxt.append(x.left)
                if x.right:
                    dq_nxt.append(x.right)
            else:
                if x.right:
                    dq_nxt.appendleft(x.right)
                if x.left:
                    dq_nxt.appendleft(x.left)
        print()
        dq = dq_nxt


# It's also easy to convert to solutions with only one dequeue, since we know the length of each level
if __name__ == "__main__":
    rt = TreeNode.build_an_example_tree()
    print_tree_anti_90(rt)
    level_print(rt)
    zigzag_print(rt)
