# in-order traverse:
# 1. if there's 1 descending pair [a, b], then they are swapped;
# 2. if there are 2 descending pairs [a, b] [c, d], then a and d are swapped.
# when return the swapped nodes, the res should include their 'env' including parent node and children nodes.
from typing import List

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


class Res:
    def __init__(self, node: TreeNode, parent: TreeNode):
        self.node = node
        self.parent = parent


# Global var to store the 'last node' during the traversal.
# Can also be implemented using a list/dict/obj of one single ele passed around; or Closure, etc.
_last_rt: Res = None


def find_swapped_nodes(rt: Res, res: List[Res]):
    global _last_rt
    if not rt.node:
        return
    find_swapped_nodes(Res(rt.node.left, rt.node), res)
    if _last_rt and rt.node.val < _last_rt.node.val:
        # descending pair
        if len(res) == 0:
            # Found 1st pair
            res.append(_last_rt)
            res.append(rt)
        else:
            # Found 2nd pair
            res.pop()
            res.append(rt)
    _last_rt = rt
    find_swapped_nodes(Res(rt.node.right, rt.node), res)


def swap_nodes(n1: Res, n2: Res):
    # If n1 and n2 are parent-child relationship
    if n1.parent == n2.node or n2.parent == n1.node:
        if n1.parent == n2.node:
            p, c = n2.node, n1.node
            pp = n2.parent
        else:
            p, c = n1.node, n2.node
            pp = n1.parent
        pl, pr = p.left, p.right
        cl, cr = c.left, c.right
        # Put c as child of pp
        if pp.left == p:
            pp.left = c
        else:
            pp.right = c
        # Put p at original c position
        p.left, p.right = cl, cr
        # Put c at original p potions based on it was p's left or right child
        if pl == c:
            c.left, c.right = p, pr
        else:
            c.left, c.right = pl, p
        return

    n1cl, n1cr = n1.node.left, n1.node.right
    n2cl, n2cr = n2.node.left, n2.node.right
    n1.node.left, n1.node.right = n2cl, n2cr
    n2.node.left, n2.node.right = n1cl, n1cr
    p1, p2 = n1.parent, n2.parent
    if p1.left == n1.node:
        p1.left = n2.node
    else:
        p1.right = n2.node
    if p2.left == n2.node:
        p2.left = n1.node
    else:
        p2.right = n1.node


def find_and_reset(rt: TreeNode) -> TreeNode:
    res = []
    virtual_p = TreeNode(0, rt, None)
    find_swapped_nodes(Res(rt, virtual_p), res)
    if len(res) != 2:
        raise RuntimeError("Invalid Res ", [r.node.val for r in res])
    swap_nodes(res[0], res[1])
    return virtual_p.left


def _reset_nodes(ns: List[TreeNode]):
    for n in ns:
        n.left = n.right = None


if __name__ == "__main__":
    nd5 = TreeNode(5)
    nd3 = TreeNode(3)
    nd6 = TreeNode(6)
    nd2 = TreeNode(2)
    nd4 = TreeNode(4)
    nd7 = TreeNode(7)

    print("Case 1")
    # Swap 4, 5
    _last_rt = None
    nd4.left, nd4.right = nd3, nd6
    nd3.left, nd3.right = nd2, nd5
    nd6.right = nd7
    print_tree_anti_90(nd4)
    rt = find_and_reset(nd4)
    print_tree_anti_90(rt)

    print("Case 2")
    _reset_nodes([nd7, nd4, nd5, nd3, nd6, nd2])
    _last_rt = None
    # Swap 4, 6
    nd5.left, nd5.right = nd3, nd4
    nd3.left, nd3.right = nd2, nd6
    nd4.right = nd7
    print_tree_anti_90(nd5)
    rt = find_and_reset(nd5)
    print_tree_anti_90(rt)

    print("Case 3")
    _reset_nodes([nd7, nd4, nd5, nd3, nd6, nd2])
    _last_rt = None
    # Swap 3, 5 (parent-child pair)
    nd3.left, nd3.right = nd5, nd6
    nd5.left, nd5.right = nd2, nd4
    nd6.right = nd7
    print_tree_anti_90(nd3)
    rt = find_and_reset(nd3)
    print_tree_anti_90(rt)
