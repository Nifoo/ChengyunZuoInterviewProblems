from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def verify_substructure(a: TreeNode, b: TreeNode):
    # Verify a tree is a sub structure rooted from any node in b tree
    if b is None:
        return a is None
    # Now b is not None
    return verify_equal(a, b) or verify_substructure(a, b.left) or verify_substructure(a, b.right)


def verify_equal(p: TreeNode, q: TreeNode):
    # Verify p tree is a sub structure rooted from q
    if p is None:
        return True
    return p.val == q.val and verify_equal(p.left, q.left) and verify_equal(p.right, q.right)


if __name__ == "__main__":
    rt = TreeNode.build_an_example_tree()
    print("main tree")
    print_tree_anti_90(rt)

    nd2 = TreeNode(2)
    nd3 = TreeNode(3)
    nd5 = TreeNode(5)
    nd2.left = nd3
    nd3.right = nd5
    print("case 1")
    print_tree_anti_90(nd2)
    print(verify_substructure(nd2, rt))

    nd2 = TreeNode(2)
    nd3 = TreeNode(3)
    nd5 = TreeNode(5)
    nd2.right = nd3
    nd3.right = nd5
    print("case 2")
    print_tree_anti_90(nd2)
    print(verify_substructure(nd2, rt))

    print("case 3")
    print(verify_substructure(None, rt))
