from typing import List


def get_max_rect(rect: List[List[int]]):
    """
    Maintain max_height[] = [max height of continuous '1' built on current row]
    for each row: max_height = (max_height + 1) if current ele is 1 else 0
    for each row: based on max_height, use monotonous stack (top larger, bottom smaller; in fact, the smaller, the more valuable, so keep it even if it's far away)
    to find the nearest smaller index to the left/right, then calculate the max size
      1. Process from left to right: When push e, you know e's left nearest min from stack top; when pop x, you know x's right nearest min from the e to push.
      2. Be careful about stk[-1]==e case.
      3. Be careful to process popping remaining elements in stk at the end.
      4. Be careful about empty stk case. 3+4: make sure every elements are processed twice, left/right respectively.
    """
    m = len(rect)
    n = len(rect[0])
    max_height = [0] * n
    max_size = 0

    for row in rect:

        for j in range(0, n):
            max_height[j] = max_height[j] + 1 if row[j] == 1 else 0

        left_min_ind, right_min_ind = get_left_right_min_ind(max_height)

        # print("row: ", row)
        # print(max_height)
        # print(left_min_ind)
        # print(right_min_ind)

        for j in range(0, n):
            max_size = max(max_size, max_height[j] * (right_min_ind[j] - left_min_ind[j] - 1))

    return max_size


def get_left_right_min_ind(max_height):
    n = len(max_height)
    stk = []
    right_min_ind = [-1] * n
    left_min_ind = [-1] * n
    for j in range(0, n):
        while stk and max_height[stk[-1]] > max_height[j]:
            x = stk.pop()
            right_min_ind[x] = j
        if stk:
            if max_height[stk[-1]] == max_height[j]:
                left_min_ind[j] = left_min_ind[stk[-1]]
            else:
                left_min_ind[j] = stk[-1]
        else:
            # All elements to the left are smaller than j. Or default processing afterwards.
            left_min_ind[j] = -1
        stk.append(j)

    while stk:
        # All elements to the right are smaller than x. Or default processing afterwards.
        x = stk.pop()
        right_min_ind[x] = n

    return left_min_ind, right_min_ind


if __name__ == "__main__":
    rect = [
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0]
    ]
    print(get_max_rect(rect))

    rect = [
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 1, 0]
    ]
    print(get_max_rect(rect))

    rect = [
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1]
    ]
    print(get_max_rect(rect))
