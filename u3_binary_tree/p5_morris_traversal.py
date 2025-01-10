# Time O(N), Space O(1) (no recursion): preorder/inorder/postorder traversal
# Morris Order
# key point:
# We know we visit a node at the second time when its left subtree's most right points to current node.
# Set a pointer from the 'most right of the left subtree' back to the root at 1st visit, set it back at 2nd visit,
# go through 'root -> left -> root -> right' order.
# If a root has left subtree then it will be visited twice.
# Morris order output list can be selected to output pre-order and in-order easily.
# Eg:
#                        /4
#              /2
#                                  /5
#                        \3
#    0
#              \1
# Morris order: 0 1 0 2 3 5 2 4
# Pre-order:    0 1   2 3 5   4  (skip the 2nd visit)
# In-order:       1 0   3 5 2 4  (skip the 1st visit if it has 2nd)
# Post-order requires some subtle adjustments:
# Skip the 1st visit of a node, for 2nd visit, output its left subtree's right boundary in reverse order,
# which can be achieved by revert the single linked list (i.e. the boundary) and recover again.
# At last, output the whole tree's right boundary.
# Post-order:   1 5 3 4 2 0

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def morris_order(rt: TreeNode):
    while rt is not None:
        print(rt.val, end=" ")
        if rt.left is not None:
            # Check left-subtree-most-right's right
            left_right = rt.left
            while left_right.right is not None and left_right.right != rt:
                left_right = left_right.right
            if left_right.right is None:
                # This is the 1st time visiting rt, point left-subtree-most-right's right points to rt self
                left_right.right = rt
                rt = rt.left
            else:
                # This is the 2nd time visiting rt, reset left-subtree-most-right's right pointer
                left_right.right = None
                rt = rt.right
        else:
            rt = rt.right


def preorder_morris(rt: TreeNode):
    while rt is not None:
        if rt.left is not None:
            # Check left-subtree-most-right's right
            left_right = rt.left
            while left_right.right is not None and left_right.right != rt:
                left_right = left_right.right
            if left_right.right is None:
                # This is the 1st time visiting rt, point left-subtree-most-right's right points to rt self
                print(rt.val, end=" ")
                left_right.right = rt
                rt = rt.left
            else:
                # This is the 2nd time visiting rt, reset left-subtree-most-right's right pointer
                left_right.right = None
                rt = rt.right
        else:
            # if current node doesn't have left subtree, then it will only be visited once
            # (there's no need to come back from its left), which is right now
            print(rt.val, end=" ")
            rt = rt.right


def inorder_morris(rt: TreeNode):
    while rt is not None:
        if rt.left is not None:
            # Check left-subtree-most-right's right
            left_right = rt.left
            while left_right.right is not None and left_right.right != rt:
                left_right = left_right.right
            if left_right.right is None:
                # This is the 1st time visiting rt, point left-subtree-most-right's right points to rt self
                left_right.right = rt
                rt = rt.left
            else:
                # This is the 2nd time visiting rt, reset left-subtree-most-right's right pointer
                print(rt.val, end=" ")
                left_right.right = None
                rt = rt.right
        else:
            # if current node doesn't have left subtree, then it will only be visited once
            # (there's no need to come back from its left), which is right now
            print(rt.val, end=" ")
            rt = rt.right


def postorder_morris(rt: TreeNode):
    rt_copy = rt
    while rt is not None:
        if rt.left is not None:
            # Check left-subtree-most-right's right
            left_right = rt.left
            while left_right.right is not None and left_right.right != rt:
                left_right = left_right.right
            if left_right.right is None:
                # This is the 1st time visiting rt, point left-subtree-most-right's right points to rt self
                left_right.right = rt
                rt = rt.left
            else:
                # This is the 2nd time visiting rt, reset left-subtree-most-right's right pointer
                left_right.right = None
                _output_reverse_right_boundary(rt.left)
                rt = rt.right
        else:
            # if current node doesn't have left subtree, then it will only be visited once
            # (there's no need to come back from its left), which is right now
            rt = rt.right
    _output_reverse_right_boundary(rt_copy)


def _output_reverse_right_boundary(rt: TreeNode):
    new_root = _reverse_right_boundary(rt)
    rt = new_root
    while rt is not None:
        print(rt.val, end=" ")
        rt = rt.right
    _reverse_right_boundary(new_root)


def _reverse_right_boundary(rt: TreeNode):
    rt_last = None
    while rt is not None:
        rt_next = rt.right
        rt.right = rt_last
        rt_last, rt = rt, rt_next
    return rt_last


if __name__ == "__main__":
    rt0 = TreeNode.build_an_example_tree()

    print_tree_anti_90(rt0)
    print("morris_order")
    morris_order(rt0)
    print_tree_anti_90(rt0)
    print("preorder_morris")
    preorder_morris(rt0)
    print_tree_anti_90(rt0)
    print("inorder_morris")
    inorder_morris(rt0)
    print_tree_anti_90(rt0)
    print("postorder_morris")
    postorder_morris(rt0)
