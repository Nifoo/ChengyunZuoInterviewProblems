import math

from utils.trees import TreeNode

# width of each node with space padding.
UNIT_LEN = 10


def print_tree_anti_90(rt: TreeNode):
    rev_inorder(rt, '', 0)


# right-mid-left traversal (anti-clock-wise 90 degree)
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


# left-mid-right traversal (clock-wise 90 degree)
def print_tree_clockwise_90(node: TreeNode):
    _inorder(node, '', 1, _get_height(node))


def _get_height(node: TreeNode):
    if not node:
        return 0
    return 1 + max(_get_height(node.left), _get_height(node.right))


def _inorder(node: TreeNode, prefix, level, total_level):
    if node is None:
        return
    _inorder(node.left, '\\', level+1, total_level)
    pre_spc = math.floor((UNIT_LEN - 1 - len(str(node.val))) / 2)
    suf_spc = UNIT_LEN - pre_spc - len(str(node.val)) - 1
    print( " " * (total_level - level) * UNIT_LEN + " " * pre_spc + str(node.val) + prefix + " " * suf_spc)
    _inorder(node.right, '/', level+1, total_level)


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

    print_tree_anti_90(rt0)
    print("----------------")
    print_tree_clockwise_90(rt0)
