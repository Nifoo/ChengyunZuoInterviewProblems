def find_right_first_smaller_index(s):
    """
    Solution1: Scan once from right to left, keep popping stack until top element is smaller than the current element, push the current element.
    Which means the stack is a Bigger->Smaller from top down.
    """
    n = len(s)
    stk = []
    res = [-1] * n
    for i in range(n - 1, -1, -1):
        while stk and s[stk[-1]] >= s[i]:
            stk.pop()
        if stk:
            res[i] = stk[-1]
        stk.append(i)
    return res


def find_left_first_smaller_index(s):
    s.reverse()
    r = find_right_first_smaller_index(s)
    rr = [len(s) - 1 - i if i != -1 else -1 for i in r]
    rr.reverse()
    return rr


def find_right_first_smaller_index2(s):
    """
    Solution 2: determine both left nearest smaller / right nearest smaller elements at ONE run.

    """
    n = len(s)
    stk = []
    res = []
    for i in range(n):
        res.append([-1, -1])
    for i in range(n - 1, -1, -1):
        while stk and s[stk[-1]] > s[i]:
            x = stk.pop()
            # left nearest strictly smaller of x
            res[x][1] = i
        if stk:
            # right nearest strictly smaller of i
            # If the stack top is equal to the new element, use its result.
            if s[i] == stk[-1]:
                res[i][0] = res[stk[-1]][0]
            else:
                res[i][0] = stk[-1]
        stk.append(i)
    return res


if __name__ == "__main__":
    s = [3, 4, 1, 5, 6, 2, 7]
    l = find_right_first_smaller_index(s)
    r = find_left_first_smaller_index(s)
    print(l)
    print(r)
    s = [3, 4, 1, 5, 6, 2, 7]
    res2 = find_right_first_smaller_index2(s)
    print(res2)
