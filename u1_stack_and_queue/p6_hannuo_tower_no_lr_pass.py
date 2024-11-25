from collections import deque
from typing import List, Deque

POLE_MAP = {
    0: "left",
    1: "mid",
    2: "right"
}


def print_hannuo_steps(plates: List[Deque[int]], k, src, dst):
    """
    Print steps for moving k plates rom src to dst (src, dst: 0, 1, 2), with the rule that only allowing move between adjacent poles.
    Assume now the k plates are in order and adjacent (+1, +1, ...).
    Each step has format "Move #plate from left to mid".
    :param plates: a list of 3 stacks (appendleft, popleft) to present 3 poles with plates numbers, like [[1, 2], [3], []]
    :param k:
    :param src:
    :param dst:
    :return:
    """
    if k == 0:
        return
    if src == 0 or src == 2:
        print_hannuo_steps(plates, k - 1, src, 2 - src)
        print(f"Move {plates[src][0]} from {POLE_MAP[src]} to {POLE_MAP[1]}")
        plates[1].appendleft(plates[src].popleft())
        print_hannuo_steps(plates, k - 1, 2 - src, 1)
        if dst == 1:
            return
        else:
            print_hannuo_steps(plates, k, 1, dst)
    else:
        print_hannuo_steps(plates, k - 1, src, 3 - src - dst)
        print(f"Move {plates[src][0]} from {POLE_MAP[src]} to {POLE_MAP[dst]}")
        plates[dst].appendleft(plates[src].popleft())
        print_hannuo_steps(plates, k - 1, 3 - src - dst, dst)


if __name__ == "__main__":
    k = 2
    print_hannuo_steps([deque(range(1, k + 1)), deque(), deque()], k, 0, 2)
