from typing import List

from utils.trees import TreeNode


# Recursive solutions:
def recur_pre_order_traverse(rt: TreeNode, l: List):
    if rt is None:
        return
    l.append(rt)
    recur_pre_order_traverse(rt.left, l)
    recur_pre_order_traverse(rt.right, l)


def recur_in_order_traverse(rt: TreeNode, l: List):
    if rt is None:
        return
    recur_in_order_traverse(rt.left, l)
    l.append(rt)
    recur_in_order_traverse(rt.right, l)


def recur_post_order_traverse(rt: TreeNode, l: List):
    if rt is None:
        return
    recur_post_order_traverse(rt.left, l)
    recur_post_order_traverse(rt.right, l)
    l.append(rt)


# Non-recursive solutions
def stack_pre_order_traverse(rt: TreeNode, l: List):
    stk = [rt]
    while stk:
        p = stk.pop()
        l.append(p)
        if p.right: stk.append(p.right)
        if p.left: stk.append(p.left)


def stack_in_order_traverse(rt: TreeNode, l: List):
    stk = [rt]
    left_sub_end = False
    while stk:
        p = stk[-1]
        # push all the left side
        # If the last loop didn't push a right node, then that means a left subtree just ended,
        # we shouldn't push left subtree again for current stack top node
        if not left_sub_end:
            while p.left:
                stk.append(p.left)
                p = p.left
        # pop out, process
        p = stk.pop()
        l.append(p)
        # push its right node
        if p.right:
            stk.append(p.right)
            left_sub_end = False
        else:
            left_sub_end = True


# # Wrong
# def stack_in_order_traverse2(rt: TreeNode, l: List):
#     stk = [rt]
#     while stk:
#         p = stk.pop()
#         if p.right:
#             stk.append(p.right)
#         if p.left:
#             stk.append(p)
#             stk.append(p.left)
#         else:
#             l.append(p)


def double_stacks_post_order_traverse(rt: TreeNode, l: List):
    # Use stk1 to do a 'pre-order' traverse but in "root-right-left" order,
    # Store the visit order into stk2, pop stk2 as the post-order traverse "left-right-root"
    stk1 = [rt]
    stk2 = []
    while stk1:
        rt = stk1.pop()
        stk2.append(rt)
        if rt.left: stk1.append(rt.left)
        if rt.right: stk1.append(rt.right)
    while stk2:
        l.append(stk2.pop())


def single_stack_post_order_traverse(rt: TreeNode, l: List):
    # h: the most recent processed node
    # c: the stack top node
    # The key point is: every time we visit element in the stack, we should differentiate:
    # (1) neither left nor right sub tree has been processed
    # (2) left sub tree has been processed, right sub tree hasn't been processed
    # (3) both left and right sub trees have been processed
    stk = [rt]
    h = None
    while stk:
        c = stk[-1]
        if c.left and h != c.left and (h is None or h != c.right):
            # case (1)
            stk.append(c.left)
        elif c.right and h != c.right:
            # case (2)
            stk.append(c.right)
        else:
            # case (3)
            # Process the node
            l.append(stk.pop())
            h = c


if __name__ == "__main__":
    rt0 = TreeNode.build_an_example_tree()

    # Recursion
    l = []
    recur_pre_order_traverse(rt0, l)
    print(l)

    l = []
    recur_in_order_traverse(rt0, l)
    print(l)

    l = []
    recur_post_order_traverse(rt0, l)
    print(l)

    # Stack
    l = []
    stack_pre_order_traverse(rt0, l)
    print(l)

    l = []
    stack_in_order_traverse(rt0, l)
    print(l)

    l = []
    double_stacks_post_order_traverse(rt0, l)
    print(l)

    l = []
    single_stack_post_order_traverse(rt0, l)
    print(l)
