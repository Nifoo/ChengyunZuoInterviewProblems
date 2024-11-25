from utils.linked_list import LinkedListNode, LinkedList


def reverse_every_k_nodes(p: LinkedListNode, k: int):
    pre = LinkedListNode(None, p)
    p_st = p_en = pre
    while True:
        for i in range(0, k):
            p_en = p_en.next
            if p_en is None:
                return pre.next
        # Now reverse [p_st.next, p_en]
        p_tmp = new_tail = p_st.next
        p_en_next = p_st.next = p_en.next
        while p_tmp != p_en_next:
            p_st_next, p_tmp_next = p_st.next, p_tmp.next
            p_st.next, p_tmp.next = p_tmp, p_st_next
            p_tmp = p_tmp_next
        p_st = p_en = new_tail
    return pre.next


if __name__ == "__main__":
    l = LinkedList([1, 2, 3, 4, 5, 6, 7, 8]).head
    print(reverse_every_k_nodes(l, 3))
