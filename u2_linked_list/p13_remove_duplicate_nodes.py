from utils.linked_list import LinkedListNode, LinkedList


def remove_duplicate_nodes(l: LinkedListNode):
    appeared_nums = set()
    pre_p, p = LinkedListNode(None, l), l
    pre_hd = pre_p
    while p:
        if p.val in appeared_nums:
            pre_p.next = p.next
            p = p.next
        else:
            appeared_nums.add(p.val)
            p = p.next
            pre_p = pre_p.next
    return pre_hd.next


if __name__ == "__main__":
    l = LinkedList([1, 2, 3, 3, 4, 4, 2, 1, 1]).head
    print(remove_duplicate_nodes(l))
