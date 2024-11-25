def sort_stk_by_stk(stk):
    """
    It's like a insert sort, O(n^2)
    :param stk:
    :return:
    """
    stk1 = []
    # stk2 is not a must-have. We can use original stk for stk2 use as well.
    stk2 = []
    while len(stk) > 0:
        tp = stk.pop()
        while len(stk1) > 0 and tp > stk1[-1]:
            stk2.append(stk1.pop())
        stk1.append(tp)
        while len(stk2) > 0:
            stk1.append(stk2.pop())
    return stk1


if __name__ == "__main__":
    stk = [5, 3, 4, 1, 2]
    stk_st = sort_stk_by_stk(stk)
    print(stk_st)
