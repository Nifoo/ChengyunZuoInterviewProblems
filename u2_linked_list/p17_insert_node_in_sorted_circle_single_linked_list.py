from utils.linked_list import LinkedListNode, LinkedList


def insert_node(head: LinkedListNode, k: int):
    if head == None:
        x = LinkedListNode(k, None)
        x.next = x
        return x
    pre, nxt = head, head.next
    while nxt != head:
        if pre.val <= k <= nxt.val:
            pre.next = LinkedListNode(k, nxt)
            return head
        pre, nxt = pre.next, nxt.next
    # Now pre=tail, nxt=head, k is out of bound [head, tail] so insert between tail -> head
    pre.next = LinkedListNode(k, nxt)
    return head


if __name__ == "__main__":
    l = LinkedList([1, 5, 9])
    l.tail.next = l.head
    print(l.head)
    print(insert_node(l.head, 7))
    print(insert_node(l.head, 12))
    print(insert_node(l.head, -1))

    l = LinkedList([1])
    l.tail.next = l.head
    print(insert_node(l.head, 2))

    print(insert_node(None, 1))
