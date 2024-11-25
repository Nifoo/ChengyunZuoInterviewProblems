import math

from utils.trees import TreeNode

# width of each node with space padding.
UNIT_LEN = 10


def print_tree(rt: TreeNode):
    rev_inorder(rt, '', 0)


# right-mid-left traversal
# 1. To easily determine the relative position of sibling nodes, the best traversal order is like a left-right or right-left scan,
# which actually is the inorder traversal.
# 2. By rotating the tree 90 degree, the horizontal 'relative position of sibling nodes' becomes vertical which can
# be displayed by switching a new line.
def rev_inorder(node: TreeNode, prefix, heading_space):
    if node is None:
        return
    rev_inorder(node.right, '/', heading_space + 1)
    pre_spc = math.floor((UNIT_LEN - len(str(node.val)) - 1) / 2)
    suf_spc = UNIT_LEN - len(str(node.val)) - 1 - pre_spc
    print(" " * (heading_space * UNIT_LEN) + " " * pre_spc + prefix + str(node.val) + " " * suf_spc)
    rev_inorder(node.left, '\\', heading_space + 1)


if __name__ == "__main__":
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

    print_tree(rt0)
