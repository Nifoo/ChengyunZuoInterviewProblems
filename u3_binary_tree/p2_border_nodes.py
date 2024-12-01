# BFS store head and tail with 'l / r'
from collections import deque

from utils.trees import TreeNode


# # Wrong: 1. Space cost is O(2^h); 2. It misses all the leaf nodes in the middle
# def get_border_nodes(rt: TreeNode):
#     q = deque([])
#     q.append((rt, -1))  # presume rt is the upper node's left child
#     ls = rs = []
#     last_line = []
#     while q:
#         last_line = q.copy()
#         for i in range(0, len(q)):
#             p = q.popleft()
#             if i == 0:
#                 ls.append(p)
#             elif i == len(q) - 1:
#                 rs.append(p)
#             if p.left: q.append((p.left, -1))
#             if p.right: q.append((p.right, 1))
#     res1 = [e[0] for e in [ls + last_line[1:-1] + reversed(rs)]]
#     res2 = [e[0] for e in [[x for x in ls if x[1] == -1] + last_line[1:-1] + [x for x in reversed(rs) if x[1] == 1]]]
#     return res1, res2



# Keep first[height], last[height] 2 arrays while doing a traversal
# (pre/in/post order traversal all work since they all guarantee left comes first than right)
# Only update first[h] when it's not set; keep updating last[h] through the whole traversal
# also use another list mid_leaves to store all the leaf but not first/last nodes (leaves in the middle)
def get_border_nodes1(rt: TreeNode):
    height = _get_height(rt)
    first = [None] * height
    last = [None] * height
    _pre_order_traverse(rt, 0, first, last)
    mid_leaves = []
    _get_mid_leaves(rt, 0, first, last, mid_leaves)
    for p in first:
        print(p)
    for p in mid_leaves:
        print(p)
    for q in range(height-1, -1, -1):
        if last[q] is not None:
            print(last[q])


def _get_height(rt: TreeNode):
    if rt is None:
        return 0
    return 1 + max(_get_height(rt.left), _get_height(rt.right))


def _pre_order_traverse(rt: TreeNode, h: int, first: [int], last: [int]):
    if rt is None:
        return
    if first[h] is None:
        first[h] = rt.val
    else:
        last[h] = rt.val
    _pre_order_traverse(rt.left, h+1, first, last)
    _pre_order_traverse(rt.right, h+1, first, last)


def _get_mid_leaves(rt: TreeNode, h: int, first: [int], last: [int], mid_leaves: list[int]):
    if rt is None:
        return
    if rt.left is None and rt.right is None:
        if rt.val != first[h] and rt.val != last[h]:
            mid_leaves.append(rt.val)
    else:
        _get_mid_leaves(rt.left, h+1, first, last, mid_leaves)
        _get_mid_leaves(rt.right, h+1, first, last, mid_leaves)


# Parent node can determine whether its child nodes need to be output or not.
# Eg: if a parent node has left child node, then its right subtree shouldn't be output.
def get_border_nodes2(rt: TreeNode):
    # Find the first node that has both left and right nodes (first branch)
    rt_copy = rt
    print("top list above branch")
    while rt is not None and not (rt.left and rt.right):
        print(rt.val)
        rt = rt.left if rt.left else rt.right
    print(rt.val)
    if rt is not None:
        # Now rt.left and rt.right both exists
        first = []
        last = []
        _find_first(rt.left, first)
        _find_last(rt.right, last)
        # leaf nodes
        leaf_nodes = []
        rt = rt_copy
        _find_leaf_nodes(rt, leaf_nodes)

        print("first")
        for p in first:
            print(p)

        print("mid_leaves")
        for i in range(1, len(leaf_nodes)-1):
            print(leaf_nodes[i])

        print("last")
        for i in range(len(last)-1, -1, -1):
            print(last[i])


def _find_leaf_nodes(rt: TreeNode, leaf_nodes: list[int]):
    if not rt:
        return
    if rt.left is None and rt.right is None:
        leaf_nodes.append(rt.val)
    else:
        _find_leaf_nodes(rt.left, leaf_nodes)
        _find_leaf_nodes(rt.right, leaf_nodes)


def _find_first(rt: TreeNode, first: list[int]):
    if rt is None:
        return
    first.append(rt.val)
    if rt.left:
        _find_first(rt.left, first)
    else:
        _find_first(rt.right, first)


def _find_last(rt: TreeNode, last: list[int]):
    if rt is None:
        return
    last.append(rt.val)
    if rt.right:
        _find_last(rt.right, last)
    else:
        _find_last(rt.left, last)


if __name__ == "__main__":
    nd = [TreeNode(i, None, None) for i in range(1, 17)]
    nd[0].left = nd[1]
    nd[0].right = nd[2]
    nd[1].right = nd[3]
    nd[2].left = nd[4]
    nd[2].right = nd[5]
    nd[3].left = nd[6]
    nd[3].right = nd[7]
    nd[4].left = nd[8]
    nd[4].right = nd[9]
    nd[7].right = nd[10]
    nd[8].left = nd[11]
    nd[10].left = nd[12]
    nd[10].right = nd[13]
    nd[11].left = nd[14]
    nd[11].right = nd[15]

    print("Border nodes style 1")
    get_border_nodes1(nd[0])
    print("Border nodes style 2")
    get_border_nodes2(nd[0])
