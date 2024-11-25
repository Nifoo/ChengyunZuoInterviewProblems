from utils.linked_list import LinkedListNode, LinkedList


def sml_sort(l: LinkedListNode, v):
    # 1. Maintain 3 pointers: tail node of s/m/l
    # 2. Another more straight forward solution is init 3 linked lists when scanning, then connect together.
    # 3. A similar problem but in array not linked list: https://leetcode.com/problems/sort-colors/submissions/740768371/,
    # move previous head to tail to get space for current element (thus order is not maitained)
    pre_h = LinkedListNode(None, None)
    ps_tail = pm_tail = pl_tail = pre_h
    while l:

        l_next = l.next
        if l.val < v:
            ps_next = ps_tail.next

            ps_tail.next = l
            l.next = ps_next

            if ps_tail == pm_tail:
                pm_tail = l
            if ps_tail == pl_tail:
                pl_tail = l

            ps_tail = l

        elif l.val == v:
            pm_next = pm_tail.next

            pm_tail.next = l
            l.next = pm_next

            if pm_tail == pl_tail:
                pl_tail = l
            pm_tail = l

        else:
            pl_next = pl_tail.next
            pl_tail.next = l
            l.next = pl_next
            pl_tail = l

        # print(ps_tail.val, pm_tail.val, pl_tail.val, l.val, pre_h.next)
        l = l_next

    return pre_h.next


if __name__ == "__main__":
    l = LinkedList([9, 0, 4, 5, 3, 3, 1])
    print(sml_sort(l.head, 3))
