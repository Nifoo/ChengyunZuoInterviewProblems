from utils.linked_list import LinkedListNode, LinkedList


def remove_specific_value_node(l: LinkedListNode, v: int):
    pre_h = LinkedListNode(None, l)
    pre_p, p = pre_h, l
    while p:
        if p.val == v:
            pre_p.next = p.next
            p = p.next
        else:
            pre_p, p = pre_p.next, p.next
    return pre_h.next


if __name__ == "__main__":
    l = LinkedList([1, 2, 3, 3, 4, 4, 2, 1, 1]).head
    print(remove_specific_value_node(l, 1))
