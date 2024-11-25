from collections import deque
from typing import List


def get_max_in_sliding_window(l: List, w):
    # Maintain a monotonous dequeue (bigger -> smaller):
    # Every time slide the window:
    # 1. popleft the 1st if that's equal to the one slides out;
    # 2. keep pop right until empty or the element in the queue dqual or bigger than the new element slides in;
    # The biggest ele in current window is the head of the queue.

    # Variation: use dq to store index, not element.

    n = len(l)
    dq = deque()
    res = [None] * n
    for i in range(0, n):
        if i >= w:
            # i-w element slides out
            if l[i - w] == dq[0]:
                dq.popleft()

        # i element slides in
        while dq and dq[-1] < l[i]:
            dq.pop()
        dq.append(l[i])

        res[i] = dq[0]
    return res[w - 1:]


if __name__ == "__main__":
    print(get_max_in_sliding_window([4, 3, 5, 4, 3, 3, 6, 7], 3))
