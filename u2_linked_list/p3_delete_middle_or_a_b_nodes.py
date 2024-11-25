import math

from utils.linked_list import LinkedListNode, LinkedList


def delete_mid_node(l):
    """
    1-＞2，删除节点1；
    1-＞2-＞3，删除节点2；
    1-＞2-＞3-＞4，删除节点2；
    1-＞2-＞3-＞4-＞5，删除节点3；

    """
    pre_head = LinkedListNode(None, l)
    p1 = p2 = pre_head
    pre1 = None
    while p2 != None and p2.next != None:
        pre1, p1, p2 = p1, p1.next, p2.next.next
    # Now delete p1
    pre1.next = p1.next
    return pre_head.next


def delete_rate_a_b_node(l, a, b):
    """
    链表：1-＞2-＞3-＞4-＞5，假设a/b的值为r。
    如果r等于0，不删除任何节点；
    如果r在区间（0，1/5]上，删除节点1；
    如果r在区间（1/5，2/5]上，删除节点2；
    如果r在区间（2/5，3/5]上，删除节点3；
    如果r在区间（3/5，4/5]上，删除节点4；
    如果r在区间（4/5，1]上，删除节点5；
    如果r大于1，不删除任何节点。

    ceil(a*n / b)
    """
    pre_head = LinkedListNode(None, l)
    if a > b or a <= 0:
        return pre_head.next
    n = 0
    pt = l
    while pt != None:
        pt = pt.next
        n += 1

    c = math.ceil(a * n / b)

    pt = pre_head
    pre_pt = None
    for i in range(0, c):
        pre_pt, pt = pt, pt.next

    # Now delete pt
    pre_pt.next = pt.next
    return pre_head.next


def max_common_factor(a, b):
    if a < b:
        return max_common_factor(b, a)
    d = a % b
    if d == 0:
        return b
    else:
        return max_common_factor(b, d)


if __name__ == "__main__":
    l = LinkedList([1, 2]).head
    l = delete_mid_node(l)  # delete 1
    print(l)

    l = LinkedList([1, 2, 3, 4, 5]).head
    l = delete_mid_node(l)  # delete 3
    print(l)

    l = LinkedList([1, 2, 3, 4, 5]).head
    l = delete_rate_a_b_node(l, 3, 5)  # delete 3
    print(l)

    l = LinkedList([1, 2, 3, 4, 5]).head
    l = delete_rate_a_b_node(l, 5, 10)  # delete 3
    print(l)
