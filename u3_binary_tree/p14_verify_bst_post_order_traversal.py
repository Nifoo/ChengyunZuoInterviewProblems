from utils.trees import TreeNode


def verify_bst_post_order_traversal(l: list[int]):
    # If for each root, the left/right nodes can be divided at somewhere in the middle
    # so that all left are smaller and right are bigger,
    # Then the post-order can be turned back to a BST
    if len(l) == 0:
        return True
    v = l[-1]
    i = 0
    while l[i] < v and i < len(l) - 1:
        i += 1
    m = i
    while l[i] > v and i < len(l) - 1:
        i += 1
    # If i==len(l)-1, then l can be divided at m.
    # If m==0, then all l are larger than p; If m==len(l)-1, then all l are smaller than p.
    return i == len(l) - 1 and verify_bst_post_order_traversal(l[:m]) and verify_bst_post_order_traversal(l[m + 1:])


def recreate_bst(l: list[int]):
    if len(l) == 0:
        return None
    v = l[-1]
    i = 0
    while l[i] < v and i < len(l) - 1:
        i += 1
    m = i
    rt = TreeNode(v)
    rt.left = recreate_bst(l[:m])
    rt.right = recreate_bst(l[m+1:])
    return rt


if __name__ == "__main__":
