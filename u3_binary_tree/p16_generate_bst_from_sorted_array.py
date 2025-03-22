from typing import List

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def generate_bst_from_sorted_array(arr: List):
    # [1, 2, 3, 4] There could be multiple BST matching this in-order traversal
    # Just pick the middle as root then do recursion
    if len(arr) == 0:
        return None
    m_i = len(arr) // 2
    l, m, r = arr[:m_i], arr[m_i], arr[m_i+1:]
    return TreeNode(m, generate_bst_from_sorted_array(l), generate_bst_from_sorted_array(r))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    rt = generate_bst_from_sorted_array(arr)
    print_tree_anti_90(rt)
