from collections import deque
from typing import List

from u3_binary_tree.p14_verify_bst_post_order_traversal import verify_bst_post_order_traversal, recreate_bst
from utils.trees import TreeNode


# Solution 1: if and only if the in-order traversal is an increasing sequence, the tree is a binary search tree;
def is_bst1(rt: TreeNode):
    return _is_inorder_increasing(rt, [None])


# in_order traversal: i.e. scan the tree from left to right, maintain a most right val (last_v[0])
def _is_inorder_increasing(rt: TreeNode, last_v: List):
    if not rt:
        return True
    left_bst = _is_inorder_increasing(rt.left, last_v)
    if not left_bst:
        return False
    rt_bst = last_v[0] is None or rt.val > last_v[0]
    if not rt_bst:
        return False
    last_v[0] = rt.val
    right_bst = _is_inorder_increasing(rt.right, last_v)
    return right_bst


# Solution 2: check if subtree is in a (lv, rv) range
def is_bst2(rt: TreeNode):
    return _is_bst_recursive(rt, None, None)


def _is_bst_recursive(rt: TreeNode, lv, rv):
    if not rt:
        return True
    if (not lv or lv < rt.val) and (not rv or rt.val < rv):
        return _is_bst_recursive(rt.left, lv, rt.val) and _is_bst_recursive(rt.right, rt.val, rv)
    else:
        return False


# BFS: once a node has no child, the other remaining nodes shouldn't have either.
def is_complete_tree(rt: TreeNode):
    nds = deque([rt])
    no_child_flag = False
    while nds:
        nd = nds.popleft()
        if nd.left:
            if not no_child_flag:
                nds.append(nd.left)
            else:
                return False
        else:
            if not no_child_flag:
                no_child_flag = True
        if nd.right:
            if not no_child_flag:
                nds.append(nd.right)
            else:
                return False
        else:
            if not no_child_flag:
                no_child_flag = True
    return True


def _get_complete_tree():
    nd0 = TreeNode(0)
    nd1 = TreeNode(1)
    nd2 = TreeNode(2)
    nd3 = TreeNode(3)
    nd0.left, nd0.right = nd1, nd2
    nd1.left = nd3
    return nd0


if __name__ == "__main__":
    # 1. BST
    # Reuse the code in previous question to construct a BST
    print("is BST?")
    arr = [2, 1, 3, 6, 5, 7, 4]
    isBST = verify_bst_post_order_traversal(arr)
    assert isBST
    rt = recreate_bst(arr)  # True
    print("solution 1: ", is_bst1(rt))
    print("solution 2: ", is_bst2(rt))

    rt_non_bst = TreeNode.build_an_example_tree()  # FaLSE
    print("solution 1: ", is_bst1(rt_non_bst))
    print("solution 2: ", is_bst2(rt_non_bst))

    # 2. Complete tree
    print("is complete Tree?")
    rt = _get_complete_tree()
    print(is_complete_tree(rt))  # True
    print(is_complete_tree(rt_non_bst))  # False
