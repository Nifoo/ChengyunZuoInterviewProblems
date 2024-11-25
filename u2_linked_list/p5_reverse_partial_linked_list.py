from utils.linked_list import LinkedListNode, LinkedList


def reverse_partial_linked_list(l: LinkedListNode, st, en):
    h = pt = LinkedListNode(None, l)
    ind = 0
    pre_st, pre_en = None, None
    while True:
        ind += 1
        pre_pt, pt = pt, pt.next
        if ind == st:
            pre_st = pre_pt
        if ind == en:
            pre_en = pre_pt
        if pre_st and pre_en:
            break

    # Reverse [st, en]
    # First, cut st, en out
    st = pre_st.next
    en = pre_en.next
    pre_st.next = en.next
    en.next = None
    p = st
    # Insert p into [pre_st, pre_st.next]
    while p:
        pre_st_next = pre_st.next
        p_next = p.next
        pre_st.next = p
        p.next = pre_st_next
        p = p_next

    return h.next


if __name__ == "__main__":
    l = LinkedList([1, 2, 3, 4, 5, 6])
    print(reverse_partial_linked_list(l.head, 3, 5))

    l = LinkedList([1, 2, 3, 4, 5, 6])
    print(reverse_partial_linked_list(l.head, 1, 5))

    l = LinkedList([1, 2, 3, 4, 5, 6])
    print(reverse_partial_linked_list(l.head, 4, 4))

    l = LinkedList([1, 2, 3, 4, 5, 6])
    print(reverse_partial_linked_list(l.head, 1, 6))
