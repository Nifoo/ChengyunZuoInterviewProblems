from utils.linked_list import LinkedListNode


def delete_kth_node_from_tail(l, k):
    pre_head = LinkedListNode(None, l)
    p1, p2 = pre_head, pre_head
    for i in range(0, k):
        p2 = p2.next
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    # Now we should delete p1.next
    p1.next = p1.next.next
    return pre_head.next
