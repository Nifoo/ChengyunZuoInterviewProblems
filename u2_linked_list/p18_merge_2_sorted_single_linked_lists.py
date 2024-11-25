from utils.linked_list import LinkedListNode, LinkedList


def merge_2_sorted_linked_lists(l1: LinkedListNode, l2: LinkedListNode):
    p3 = l3 = LinkedListNode(None, None)
    p1 = l1
    p2 = l2
    while p1 or p2:
        if p1 and (p2 is None or p1.val < p2.val):
            p3.next = p1
            p1 = p1.next
        else:
            p3.next = p2
            p2 = p2.next
        p3 = p3.next
    p3.next = None
    return l3.next


if __name__ == "__main__":
    l1 = LinkedList([1, 5, 9])
    l2 = LinkedList([2, 4, 6])
    print(merge_2_sorted_linked_lists(l1.head, l2.head))

    l1 = LinkedList([1])
    print(merge_2_sorted_linked_lists(l1.head, None))
