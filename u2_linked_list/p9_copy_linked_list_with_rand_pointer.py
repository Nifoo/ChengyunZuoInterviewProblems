from utils.linked_list import LinkedListNode


class LinkedListNodeRandPt(LinkedListNode):
    def __init__(self, v, nxt, rnd):
        super().__init__(v, nxt)
        self.rnd = rnd


def copy_linked_list_with_rand_pointer(l):
    """
    Create a copy in the original linked list after each node;
    Scan again link the rand pointers;
    Then separate these 2 linked lists.
    """
    if l is None:
        return None

    hd = LinkedListNode(None, l)
    p = hd.next
    while p:
        p_nxt = p.next
        p_nxt.next = LinkedListNodeRandPt(p.val, p_nxt, None)
        p = p_nxt

    p = hd.next
    while p:
        if p.rnd is None:
            p.next.rnd = None
        else:
            p.next.rnd = p.rnd.next
        p = p.next.next

    # Separate lists
    p = hd.next
    p2_st = p2 = p.next
    while p2.next:
        p_nxt, p2_nxt = p2.next, p2.next.next
        p.next, p2.next = p_nxt, p2_nxt
        p, p2 = p_nxt, p2_nxt
    p.next = p2.next = None

    return p2_st
