from typing import List


def get_visible_mountain_pairs_in_circle(heights: List[int]):
    n = len(heights)
    # Find the biggest ele
    max_i = 0
    for i in range(0, n):
        if heights[i] > heights[max_i]:
            max_i = i

    # Starting from max element, build monotonous max stack (max first in) to find nearest max element
    # Store [ele, count] in the stack. Count pair when element is popped out; count 'lower -> higher' pairs.
    h2 = heights[max_i:] + heights[0: max_i]
    max_stk = []
    visable_pair = 0
    for e in h2:
        while max_stk and max_stk[-1][0] < e:
            x, c = max_stk.pop()
            # c pairing internally with themselves
            visable_pair += c * (c - 1) / 2
            # x's right nearest higher element is e
            visable_pair += c
            # x's left nearest higher element is stack top
            if max_stk:
                visable_pair += c
        # push e
        if max_stk and max_stk[-1][0] == e:
            max_stk[-1][1] += 1
        else:
            max_stk.append([e, 1])

    while max_stk:
        x, c = max_stk.pop()
        # self
        visable_pair += c * (c - 1) / 2
        # from end to the head
        if max_stk:
            visable_pair += c
        # from end to previous, make sure it's not the same as above
        if len(max_stk) > 1 or (len(max_stk) == 1 and max_stk[-1][1] > 1):
            visable_pair += c

    return int(visable_pair)


if __name__ == "__main__":
    print(get_visible_mountain_pairs_in_circle([3, 1, 2, 4, 5]))
    print(get_visible_mountain_pairs_in_circle([4, 2, 4, 5, 3, 4, 5, 2, 3, 5, 4]))
