from u3_binary_tree.p3_print_binary_tree_pretty import print_tree_anti_90
from utils.trees import TreeNode


def find_longest_path_from_rt_given_sum(s, rt: TreeNode):
    if rt is None:
        return 0
    return max(find_longest_path_from_rt_given_sum(s-rt.val, rt.left), find_longest_path_from_rt_given_sum(s-rt.val, rt.right)) + 1


# This is the correct solution to thq Q in the book.
# Traverse the tree, maintain the highest node level whose sum of the path starting from root is s: highest_level[s], also the sum of the path from root itself s.
# So we will know for the current node value x level lx, from this node highest_level[target_s - x] to the current node has the sum target_s.
# Complexity: t: O(n), s: O(n). n = # of nodes.
def find_longest_section_given_sum(s, rt: TreeNode):
    highest_level = {0: 0}
    # if returns 0, it means there's no such section that has expected sum s
    return find_longest_section_given_sum_solution(s, rt, highest_level, 0, 0)


# Get the length of the longest section with sum target_s:
# ans_cur: any node above to current node
# ans_left: any node above to any node in the left subtree
# ans_right: any node above to any node in the right subtree
# return the max of them, which is any node above to any node in this current node rooted tree.
# 0 means there's no such section
def find_longest_section_given_sum_solution(target_s, rt: TreeNode, highest_level, cur_s, cur_l):
    if not rt:
        return 0
    cur_l += 1
    cur_s += rt.val
    update_highest_map = False
    if cur_s not in highest_level:
        highest_level[cur_s] = cur_l
        update_highest_map = True

    if target_s - cur_s in highest_level:
        ans_cur = cur_l - highest_level[target_s - cur_s]
    else:
        ans_cur = 0
    ans_left = find_longest_section_given_sum_solution(target_s, rt.left, highest_level, cur_s, cur_l)
    ans_right = find_longest_section_given_sum_solution(target_s, rt.right, highest_level, cur_s, cur_l)
    if update_highest_map:
        del highest_level[cur_s]
    return max(ans_cur, ans_left, ans_right)


if __name__ == "__main__":
    rt = TreeNode.build_an_example_tree()
    print_tree_anti_90(rt)
    print(find_longest_path_from_rt_given_sum(10, rt))
    print(find_longest_section_given_sum(10, rt))
