from other_problems.kmp import kmp_match
from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from u3_binary_tree.p4_serialization_deserialization import serialize
from utils.trees import TreeNode


def verify_subtree(p: TreeNode, s: TreeNode):
    # Verify if p is a subtree of s
    # leveraging serialization and kmp match
    p_str = serialize(p)
    s_str = serialize(s)
    res = kmp_match(s_str, p_str)
    return len(res) != 0


if __name__ == "__main__":
    rt = TreeNode.build_an_example_tree()
    print("main tree")
    print_tree_anti_90(rt)

    nd2 = TreeNode(2)
    nd3 = TreeNode(3)
    nd4 = TreeNode(4)
    nd5 = TreeNode(5)
    nd2.left = nd3
    nd2.right = nd4
    nd3.right = nd5
    print("case 1")
    print_tree_anti_90(nd2)
    print(verify_subtree(nd2, rt))

    nd2 = TreeNode(2)
    nd3 = TreeNode(3)
    nd5 = TreeNode(5)
    nd2.left = nd3
    nd3.right = nd5
    print("case 2")
    print_tree_anti_90(nd2)
    print(verify_subtree(nd2, rt))

    print("case 3")
    print(verify_subtree(None, rt))