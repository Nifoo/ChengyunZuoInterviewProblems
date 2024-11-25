from collections import deque

"""
Reverse a stack using recursion with space complexity O(1)
"""


def reverse_stk_by_recursion(stk):
    if len(stk) <= 1:
        return
    e_bottom = get_and_remove_bottom_ele(stk)
    reverse_stk_by_recursion(stk)
    stk.append(e_bottom)


def get_and_remove_bottom_ele(stk):
    if len(stk) == 1:
        return stk.pop()
    e_top = stk.pop()
    e_bottom = get_and_remove_bottom_ele(stk)
    stk.append(e_top)
    return e_bottom


if __name__ == "__main__":
    # Time O(n^2)
    stk = [1, 2, 3, 4]
    reverse_stk_by_recursion(stk)
    print(stk)
