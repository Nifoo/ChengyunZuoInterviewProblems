from typing import Dict, List

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def find_max_bst_embedded(rt: TreeNode, bst_cnt: Dict[TreeNode, List[int]], max_bst_size, max_bst_root) -> (int, TreeNode):
    """
    This finds the max bst 'EMBEDDED' in the rt Tree, its leaves don't have to be the leaf nodes of rt Tree.
    1. It's easy to achieve in O(n^2): go through each node, expand from the node to get max BST.
    2. Here's the solution to achieve in O(n): post-traverse the tree, for each node rt, maintain BST topo contribute size count (l, r)
    to represent with the rt as root, how many valid nodes can rt's left/right subtree contribute respectively.
    So the tricky part is when we have topo contribute size for rooted at rt_l, rooted at rt_r, how to transfer to rooted at rt.
    We need go through the right boundary of rt_l and left boundary of rt_r until the node is out of range (> or < rt),
    then cut off and then update the size back through the path (in fact, no need to update the whole path, because only the rt.l, rt.r will be used later).
    Returns updated max_bst_size, max_bst_root
    :param rt:
    :param bst_cnt: bst_cnt[treeNode][0], bat_cnt[treeNode][1]: treeNode's left/right BST topo contribute size
    :param max_bst_size: current max bst size
    :param max_bst_root: the root of the current max bst
    """
    bst_cnt[rt] = [0, 0]
    if not rt:
        return max_bst_size, max_bst_root

    max_bst_size, max_bst_root = find_max_bst_embedded(rt.left, bst_cnt, max_bst_size, max_bst_root)
    max_bst_size, max_bst_root = find_max_bst_embedded(rt.right, bst_cnt, max_bst_size, max_bst_root)
    # Now we have BST topo contribute size count for rooted at rt.left, rt.right
    # left subtree's right boundary
    if rt.left:
        if rt.left.val > rt.val:
            # Cut off l_r
            rt.left = None
        else:
            p, l_r = rt.left, rt.left.right
            while l_r and l_r.val < rt.val:
                p = l_r
                l_r = l_r.right
            # Cut off l_r, update topo contribute at rt.left
            if l_r:
                bst_cnt[rt.left][1] -= bst_cnt[l_r][0] + bst_cnt[l_r][1] + 1
                p.right = None

    # right subtree's left boundary
    if rt.right:
        if rt.right.val < rt.val:
            # Cut off l_r
            rt.right = None
        else:
            p, r_l = rt.right, rt.right.left
            while r_l and r_l.val > rt.val:
                p = r_l
                r_l = r_l.left
            # Cut off r_l, update topo contribute at rt.right
            if r_l:
                bst_cnt[rt.right][0] -= bst_cnt[r_l][0] + bst_cnt[r_l][1] + 1 if r_l else 0
                p.left = None

    if rt.left:
        bst_cnt[rt][0] = bst_cnt[rt.left][0] + bst_cnt[rt.left][1] + 1
    if rt.right:
        bst_cnt[rt][1] = bst_cnt[rt.right][0] + bst_cnt[rt.right][1] + 1

    bst_size_rt = bst_cnt[rt][0] + bst_cnt[rt][1] + 1
    if bst_size_rt > max_bst_size:
        return bst_size_rt, rt
    else:
        return max_bst_size, max_bst_root


if __name__ == "__main__":
    nd6 = TreeNode(6)
    nd1 = TreeNode(1)
    nd12 = TreeNode(12)
    nd0 = TreeNode(0)
    nd3 = TreeNode(3)
    nd10 = TreeNode(10)
    nd13 = TreeNode(13)
    nd4 = TreeNode(4)
    nd14 = TreeNode(14)
    nd20 = TreeNode(20)
    nd16 = TreeNode(16)
    nd2 = TreeNode(2)
    nd5 = TreeNode(5)
    nd11 = TreeNode(11)
    nd15 = TreeNode(15)

    nd6.left, nd6.right = nd1, nd12
    nd1.left, nd1.right = nd0, nd3
    nd12.left, nd12.right = nd10, nd13
    nd10.left, nd10.right = nd4, nd14
    nd13.left, nd13.right = nd20, nd16
    nd4.left, nd4.right = nd2, nd5
    nd14.left, nd14.right = nd11, nd15

    print_tree_anti_90(nd6)
    bst_cnt = {}
    max_bst_size, max_bst_root = find_max_bst_embedded(nd6, bst_cnt, 0, None)
    print("max_bst_size = ", max_bst_size)
    print_tree_anti_90(max_bst_root)
    for k, v in bst_cnt.items():
        print(k, v)
