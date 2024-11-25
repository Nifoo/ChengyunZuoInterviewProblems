from typing import List


class LinkedListNode:
    def __init__(self, v, nxt):
        self.val = v
        self.next = nxt

    def __str__(self):
        s = ""
        pt = self
        while pt:
            s = s + " -> " + str(pt.val)
            pt = pt.next
            # in case it's a circle linked list
            if pt == self:
                break
        return s


class LinkedList:
    def __init__(self, l: List):
        self.head = pt = LinkedListNode(l[0], None)
        for v in l[1:]:
            pt.next = LinkedListNode(v, None)
            pt = pt.next
        self.tail = pt


class DoubleLinkedListNode:
    def __init__(self, v, pre, nxt):
        self.val = v
        self.pre = pre
        self.next = nxt

    def __str__(self):
        s = ""
        pt = self
        while pt:
            s += " -> " + str(pt.val)
            pt = pt.next
        return s


class DoubleLinkedList:
    def __init__(self, l: List):
        self.head = pt = DoubleLinkedListNode(l[0], None, None)
        for v in l[1:]:
            pt.next = DoubleLinkedListNode(v, pt, None)
            pt = pt.next
