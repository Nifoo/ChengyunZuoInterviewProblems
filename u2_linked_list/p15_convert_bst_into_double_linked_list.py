from utils.trees import TreeNode


def convert_bst_into_double_linked_list(rt: TreeNode) -> (TreeNode, TreeNode):
    """
    A Boring problem... in-place conversion with in-order traversal (so like sorted)
    :param rt: root node of a BST
    :return: (head node, tail node) of the converted double linked list
    """
    if rt.left is None and rt.right is None:
        return rt, rt
    if rt.left is None:
        r_hd, r_tail = convert_bst_into_double_linked_list(rt.right)
        rt.right = r_hd
        r_hd.left = rt
        return rt, r_tail
    if rt.right is None:
        l_hd, l_tail = convert_bst_into_double_linked_list(rt.left)
        l_tail.right = rt
        rt.left = l_tail
        return l_hd, rt

    l_hd, l_tail = convert_bst_into_double_linked_list(rt.left)
    r_hd, r_tail = convert_bst_into_double_linked_list(rt.right)
    l_tail.right, rt.left = rt, l_tail
    rt.right, r_hd.left = r_hd, rt
    return l_hd, r_tail


# Simplified version of above
def convert_bst_into_double_linked_list_2(rt: TreeNode) -> (TreeNode, TreeNode):
    if rt is None:
        return None, None

    l_hd, l_tail = convert_bst_into_double_linked_list(rt.left)
    r_hd, r_tail = convert_bst_into_double_linked_list(rt.right)
    if l_tail is None:
        l_hd = rt
    else:
        l_tail.right, rt.left = rt, l_tail
    if r_hd is None:
        r_tail = rt
    else:
        rt.right, r_hd.left = r_hd, rt
    return l_hd, r_tail
