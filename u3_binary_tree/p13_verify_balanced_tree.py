from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def verify_balanced_tree(rt: TreeNode) -> (bool, int):
    # Verify for any node, the diff of heights of left subtree and right subtree is no more than 1
    if rt is None:
        return True, 0
    balance_l, h_l = verify_balanced_tree(rt.left)
    balance_r, h_r = verify_balanced_tree(rt.right)
    print(rt.val, balance_l and balance_r and abs(h_l - h_r) <= 1, max(h_l, h_r) + 1)
    return balance_l and balance_r and abs(h_l - h_r) <= 1, max(h_l, h_r) + 1


if __name__ == "__main__":
    ndx = TreeNode.build_an_example_tree()
    print("case 1")
    print_tree_anti_90(ndx)
    print(verify_balanced_tree(ndx))

    nd2 = TreeNode(2)
    nd3 = TreeNode(3)
    nd4 = TreeNode(4)
    nd5 = TreeNode(5)
    nd2.left = nd3
    nd2.right = nd4
    nd3.right = nd5
    print("case 2")
    print_tree_anti_90(nd2)
    print(verify_balanced_tree(nd2))
