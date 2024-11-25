from utils.linked_list import LinkedList, LinkedListNode, DoubleLinkedList, DoubleLinkedListNode


def reverse_linked_list(l: LinkedListNode):
    pre = LinkedListNode(None, None)
    while l != None:
        t = pre.next
        p_next = l.next
        pre.next = l
        l.next = t
        l = p_next
    return pre.next


def reverse_double_linked_list(l: DoubleLinkedListNode):
    pre = DoubleLinkedListNode(None, l, None)
    while l != None:
        l_next = l.next
        pre_next = pre.next

        pre.next = l
        l.pre = pre

        l.next = pre_next
        if pre_next:
            pre_next.pre = l

        l = l_next
    return pre.next


if __name__ == "__main__":
    l = LinkedList([1, 2, 3, 4])
    print(reverse_linked_list(l.head))

    l = DoubleLinkedList([1, 2, 3, 4])
    print(reverse_double_linked_list(l.head))
