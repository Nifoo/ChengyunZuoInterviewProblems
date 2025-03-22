import attr

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90


@attr.define
class NodeP:
    val: int
    left: 'NodeP' = None
    right: 'NodeP' = None
    parent: 'NodeP' = None


def find_next_in_order_node(rt: NodeP) -> NodeP:
    """
    if rt has right child, then return its right subtree's most left node;
    Otherwise, if rt has parent node, keep finding the parent until current node is the left child of its parent, return that parent;
    if parent is null, then rt is the last node in the in-order traversal
    :param rt:
    :return:
    """
    rtx = rt
    if rtx.right:
        nxt = rtx.right
        while nxt.left:
            nxt = nxt.left
        return nxt
    rtx = rt
    prnt = rtx.parent
    while prnt:
        if prnt.left.val == rtx.val:
            return prnt
        prnt, rtx = prnt.parent, prnt
    return None


if __name__ == "__main__":
    nds = []
    for i in range(5):
        nds.append(NodeP(val=i))
    for i in range(5):
        if 2*i+1 < 5:
            nds[i].left = nds[2*i+1]
            nds[2*i+1].parent = nds[i]
        else:
            nds[i].left = None
        if 2*i+2 < 5:
            nds[i].right = nds[2*i+2]
            nds[2*i+2].parent = nds[i]
        else:
            nds[i].right = None
    print_tree_anti_90(nds[0])
    for i in range(5):
        print(nds[i].val, "'s next node is: ")
        x = find_next_in_order_node(nds[i])
        if x:
            print(x.val)
        else:
            print(x)
