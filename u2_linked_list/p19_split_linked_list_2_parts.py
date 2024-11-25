from utils.linked_list import LinkedListNode, LinkedList


def split_linked_list_2_parts(l: LinkedListNode):
    if LinkedListNode is None:
        return None
    ll = LinkedListNode(None, l)
    p1 = p2 = l
    p = l.next
    p2.next = None
    odd_bit = False
    while p:
        p_next = p.next
        if odd_bit:
            p1_next = p1.next
            p1.next = p
            p.next = p1_next
            p1 = p1.next
        else:
            p2_next = p2.next
            p2.next = p
            p.next = p2_next
            p2 = p2.next
        p = p_next
        odd_bit = not odd_bit

    return ll.next


if __name__ == "__main__":
    l = LinkedList([1, 2, 3, 4])
    print(split_linked_list_2_parts(l.head))

    l = LinkedList([1, 2, 3])
    print(split_linked_list_2_parts(l.head))
