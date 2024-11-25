import logging

from utils.linked_list import LinkedListNode, LinkedList

log = logging.getLogger()


def add(l1: LinkedListNode, l2: LinkedListNode):
    """
    l1: 1->2->3
    l2: 8->9
    return 2->1->2
    """
    l1_r = reverse(l1)
    l2_r = reverse(l2)

    p1, p2 = l1_r, l2_r
    s, d = 0, 0
    res = None
    while p1 or p2 or d:
        p1v = 0 if p1 is None else p1.val
        p2v = 0 if p2 is None else p2.val
        s = p1v + p2v + d
        res = LinkedListNode(s % 10, res)
        d = s // 10
        p1, p2 = p1.next if p1 else None, p2.next if p2 else None

    reverse(l1_r)
    reverse(l2_r)
    return reverse(res)


def reverse(l: LinkedListNode):
    pre = LinkedListNode(None, None)
    p = l
    while p:
        pre_nxt, p_nxt = pre.next, p.next
        pre.next, p.next = p, pre_nxt
        p = p_nxt
    return pre.next


if __name__ == "__main__":
    l1 = LinkedList([1, 2, 3]).head
    l2 = LinkedList([8, 9]).head
    print(add(l1, l2))
