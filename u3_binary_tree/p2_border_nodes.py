# BFS store head and tail with 'l / r'
from collections import deque

from utils.trees import TreeNode


def get_border_nodes(rt: TreeNode):
    q = deque([])
    q.append((rt, -1))  # presume rt is the upper node's left child
    ls = rs = []
    last_line = []
    while q:
        last_line = q.copy()
        for i in range(0, q.size()):
            p = q.popleft()
            if i == 0:
                ls.append(p)
            elif i == q.size() - 1:
                rs.append(p)
            if p.left: q.append((p.left, -1))
            if p.right: q.append((p.right, 1))
    res1 = [e[0] for e in [ls + last_line[1:-1] + reversed(rs)]]
    res2 = [e[0] for e in [[x for x in ls if x[1] == -1] + last_line[1:-1] + [x for x in reversed(rs) if x[1] == 1]]]
    return res1, res2
