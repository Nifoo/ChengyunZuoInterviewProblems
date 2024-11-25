from utils.linked_list import LinkedList


def get_common_part_of_2_linked_lists(l1, l2):
    p1, p2 = l1, l2
    while p1 != p2:
        p1 = l2 if p1 == None else p1.next
        p2 = l1 if p2 == None else p2.next
    # Now p1=p2=the starting point of the common part
    return p1


if __name__ == "__main__":
    l1 = LinkedList([1, 2, 3, 4])
    l2 = LinkedList([5, 6])
    lc = LinkedList([10, 11, 12])
    l1.tail.next = lc.head
    l2.tail.next = lc.head
    p_common_st = get_common_part_of_2_linked_lists(l1.head, l2.head)
    while p_common_st:
        print(p_common_st.val)
        p_common_st = p_common_st.next
