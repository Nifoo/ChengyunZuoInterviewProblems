from utils.linked_list import LinkedListNode, LinkedList


def select_sort_linked_list(l: LinkedListNode):
    # new linked list pre-head and tail
    pre_h = tail_h = LinkedListNode(None, None)
    # old linked list pre_p and starting node p (we need pre_p because p could be removed)
    pre_p, p = LinkedListNode(None, l), l
    while p:
        # Search the min in [p, end], move into tail_h.next
        min_p = p2 = p
        pre_min_p = pre_p2 = pre_p
        # finding min in [p, end]
        while p2:
            if p2.val < min_p.val:
                min_p, pre_min_p = p2, pre_p2
            p2, pre_p2 = p2.next, pre_p2.next
        # Insert min_p following pre_p
        pre_min_p.next = min_p.next
        min_p.next = tail_h.next
        tail_h.next = min_p
        tail_h = tail_h.next
        p = pre_p.next
    return pre_h.next


if __name__ == "__main__":
    l = LinkedList([3, 5, 2, 1, 4, 0, 1, 4, 4, 2]).head
    print(select_sort_linked_list(l))
