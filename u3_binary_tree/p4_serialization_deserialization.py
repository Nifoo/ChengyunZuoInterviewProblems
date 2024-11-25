# Sol 1: DFS
# The key point is to denote the boundary of a subtree, which can be achieved by denoting the 'null' nodes.
# Preorder: 1,2,4,#,3,#,#,
from collections import deque

from u3_binary_tree.p3_print_binary_tree_pretty import print_tree
from utils.trees import TreeNode


def serialize(rt: TreeNode) -> str:
    if rt is None:
        return '#,'
    return str(rt.val) + ',' + serialize(rt.left) + serialize(rt.right)


# Instead of maintaining the index of s, we can also use a queue
def deserialize(s: str, kstart=0) -> (TreeNode, int):
    kend = s.find(',', kstart)
    if s[kstart: kend] == '#':
        return None, kend
    rt = TreeNode(int(s[kstart: kend]), None, None)
    rtl, kl = deserialize(s, kend + 1)
    rtr, kr = deserialize(s, kl + 1)
    rt.left = rtl
    rt.right = rtr
    return rt, kr


# Sol 2: BFS
def serialize_bfs(rt: TreeNode) -> str:
    q = deque([rt])
    s = ""
    while q:
        nd = q.popleft()
        if nd is None:
            s += "#,"
        else:
            s += str(nd.val) + ","
            q.append(nd.left)
            q.append(nd.right)
    return s


def deserialize_bfs(s: str):
    sq = s.split(',')[:-1]
    nds = [get_node(x) for x in sq]
    p_parent = 0
    p_child = 1
    while p_child < len(nds):
        while nds[p_parent] is None:
            p_parent += 1
        nds[p_parent].left = nds[p_child]
        p_child += 1
        nds[p_parent].right = nds[p_child]
        p_child += 1
        p_parent += 1
    return nds[0]


def get_node(x: str):
    if x == '#':
        return None
    return TreeNode(int(x), None, None)


if __name__ == "__main__":
    rt0 = TreeNode(0, None, None)
    rt1 = TreeNode(1, None, None)
    rt2 = TreeNode(2, None, None)
    rt3 = TreeNode(3, None, None)
    rt4 = TreeNode(4, None, None)
    rt5 = TreeNode(5, None, None)

    rt0.left = rt1
    rt0.right = rt2
    rt2.left = rt3
    rt2.right = rt4
    rt3.right = rt5

    # Sol 1
    s = serialize(rt0)
    print(s)
    rt_recreated, _ = deserialize(s)
    print_tree(rt_recreated)

    # Sol 2
    s2 = serialize_bfs(rt0)
    print(s2)
    rt_recreated2 = deserialize_bfs(s2)
    print_tree(rt_recreated2)
