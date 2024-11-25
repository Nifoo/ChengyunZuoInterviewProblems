from utils.linked_list import LinkedListNode, LinkedList


def find_circle_in_linked_list(p: LinkedListNode):
    """
    return null if there's no circle; return the first node in the circle if there's.
    """
    if not p:
        return None
    pre_h = LinkedListNode(None, p)
    p1 = p2 = pre_h
    while p1 and p2 and p2.next and (p1 != p2 or p1 == p2 == pre_h):
        p1 = p1.next
        p2 = p2.next.next
    if not p1 or not p2 or not p2.next:
        return None
    # Now starting from pre_h, p1 (p2), walk again, they will intercept at the the 1st node in the circle
    # If dray a graph to explain, the linked list consists of x, y, z 3 segments and satisfy
    # 2(x+y)=x+2y+z => x=z
    p3 = pre_h
    while p3 != p1:
        p3, p1 = p3.next, p1.next
    return p3


def find_intersect_of_2_linked_lists(l1: LinkedListNode, l2: LinkedListNode):
    """
    Return the intersect node if do intersect, otherwise return None.

    1. If 1 has circle 1 doesn't, then return None
    2. If 2 both have no circles: just walk through, swap to the other's start when reach the tail, check if they meet before reach the end
    3. If 2 both have circles, assume the returned nodes are c1, c2:
      1. If the circle starting node is the same, which means they intersect before entering the loop, so similar to 2 but consider c1 (c2) as the tail
      2. If not, they must be in a "66" shape or "A" shape. To pick "A" shape out:
      Only need to check if c1 and c2 both exist in one line
    """
    c1, c2 = find_circle_in_linked_list(l1), find_circle_in_linked_list(l2)
    if (c1 and not c2) or (not c1 and c2):
        # Case 1
        return None
    if not c1 and not c2:
        # Case 2
        p1, p2 = l1, l2
        while p1 and p2 and p1 != p2:
            p1 = l2 if not p1 else p1.next
            p2 = l1 if not p2 else p2.next
        if p1 and p2 and p1 == p2:
            return p1
        else:
            return None
    elif c1 == c2:
        # Case 3.1
        p1, p2 = l1, l2
        while p1 != c1 and p2 != c1 and p1 != p2:
            p1 = l2 if not p1 else p1.next
            p2 = l1 if not p2 else p2.next
        if p1 and p2 and p1 == p2:
            return p1
        else:
            return None
    else:
        # Case 3.2
        p1 = l1
        count_c1 = 0
        while count_c1 <= 1:
            if p1 == c1:
                count_c1 += 1
            if p1 == c2:
                # c1, c2 both exist in l1 line
                return c1
        return None


# TODO: Pending Verification
if __name__ == "__main__":
    pass
