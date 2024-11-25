from utils.linked_list import LinkedListNode, LinkedList


def check_palindrome_linked_list(l):
    """
    Edit the linked list, compare, revert edit
    time O(n), space O(1)
    """
    p1 = p2 = ph = LinkedListNode(None, l)
    while p2 != None and p2.next != None:
        p1 = p1.next
        p2 = p2.next.next
    if p2 == None:
        # odd list
        p1_end = p1
        p2_st = p1.next
    else:
        # even list
        p1_end = p1.next
        p2_st = p1.next

    # Reverse [ph.next, p1_end)
    reverse_linked_list(ph, p1_end)

    # Compare [ph.next, None) and [p2_st, None)
    p1 = ph.next
    p2 = p2_st
    is_palindrome = True
    while p1 and p2:
        if p1.val != p2.val:
            is_palindrome = False
            break
        p1, p2 = p1.next, p2.next

    # Reverse [ph.next, None) back
    t = reverse_linked_list(ph, None)
    t.next = p1_end

    return is_palindrome


# Reverse [ph.next, end_node), return the tail node
def reverse_linked_list(ph, end_node):
    p1 = ph.next
    pre_p1 = ph
    ph.next = None
    while p1 and p1 != end_node:
        ph_next, p1_next = ph.next, p1.next
        ph.next = p1
        p1.next = ph_next
        pre_p1, p1 = p1, p1_next
    return pre_p1  # Return the tail node


if __name__ == "__main__":
    p = LinkedList([1, 2, 3, 2, 1])
    print(check_palindrome_linked_list(p.head))
    p = LinkedList([1, 2, 3, 4, 1])
    print(check_palindrome_linked_list(p.head))
    p = LinkedList([1, 2, 2, 1])
    print(check_palindrome_linked_list(p.head))
    p = LinkedList([1, 2, 3, 1])
    print(check_palindrome_linked_list(p.head))
    p = LinkedList([1])
    print(check_palindrome_linked_list(p.head))
