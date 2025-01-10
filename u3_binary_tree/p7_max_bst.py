from utils.trees import TreeNode

# This finds the max bst 'EMBEDDED' in the rt Tree, its leaves don't have to be the leaf nodes of rt Tree.
# Return the size of the max subtree under the rt (not rooted at rt),
# the size of max subtree rooted at rt, its leftest, rightest node values.
# then max_sub root value
def find_max_bst_embedded(rt: TreeNode):
    if not rt:
        return (0, 0, None, None, None)
    max_left_sub, max_left, ll, lr, max_left_rt_v = find_max_bst_embedded(rt.left)
    max_right_sub, max_right, rl, rr, max_right_rt_v = find_max_bst_embedded(rt.right)

    # rooted at rt
    max_rt = 1
    max_rt_l = max_rt_r = rt.val
    if max_left and lr < rt.val:
        max_rt += max_left
        max_rt_l = ll
    if max_right and rl > rt.val:
        max_rt += max_right
        max_rt_r = rr

    # not rooted at rt
    max_non_rt, max_non_rt_rt_v = find_the_max([
        (max_left_sub, max_left_rt_v), (max_left, rt.left.val if rt.left else None),
        (max_right_sub, max_right_rt_v), (max_right, rt.right.val if rt.right else None)
    ])

    return (max_non_rt, max_rt, max_rt_l, max_rt_r, max_non_rt_rt_v)


# rt_sz: list[(size, rt val)]
def find_the_max(sz_rts):
    max_sz_rt = sz_rts[0]
    for i in sz_rts:
        if i[0] is not None and i[0]>max_sz_rt[0]:
            max_sz_rt = i
    return max_sz_rt


# Similar to above, but this finds subtree whose leaf nodes are also rt Tree's leaf nodes
# (i.e. cut off is not allowed, the result subtree should exhaust all nodes below)
# Return the size of the max subtree under the rt (may or may not be rooted at rt, but can be determined by r val),
# its leftest, rightest node values.
# then max subtree root value.
def find_max_bst_to_the_leaves(rt: TreeNode):
    if not rt:
        return (0, None, None, None)
    max_left, ll, lr, max_left_rt_v = find_max_bst_to_the_leaves(rt.left)
    max_right, rl, rr, max_right_rt_v = find_max_bst_to_the_leaves(rt.right)

    # rooted at rt:
    # only possible when max_left's root is rt.left or the left is None,
    # and max_right's root is rt.right or the right is None,
    # and the lr, rl fit rt in BST.
    if (
            (rt.left is None or (max_left_rt_v == rt.left.val and rt.left.val < rt.val)) and
            (rt.right is None or max_right_rt_v == rt.right.val and rt.val < rt.right.val)
    ):
        max_rt, max_rt_l, max_rt_r = (
            1 + max_left + max_right,
            rt.val if rt.left is None else ll,
            rt.val if rt.right is None else rr
        )
    else:
        max_rt, max_rt_l, max_rt_r = 0, None, None

    # 3 candidates
    max_sz = max(max_rt, max_left, max_right)
    if max_sz == max_rt:
        return max_rt, max_rt_l, max_rt_r, rt.val
    elif max_sz == max_left:
        return max_left, ll, lr, max_left_rt_v
    else:
        return max_right, rl, rr, max_right_rt_v


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

    # Understanding 1
    max_sub, max_rt, max_rt_l, max_rt_r, max_sub_rt_v = find_max_bst_embedded(nd6)
    if max_sub > max_rt:
        print(max_sub, max_sub_rt_v)
    else:
        print(max_rt, nd6.val)

    # Understanding 2 (which is the same as the book)
    max_sub, max_rt_l, max_rt_r, max_sub_rt_v = find_max_bst_to_the_leaves(nd6)
    print(max_sub, max_sub_rt_v)


