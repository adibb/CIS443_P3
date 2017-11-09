__author__ = 'adibb'

# Written by Alex Dibb
# Last edited 11/8/2017
# Doubly linked list, w/ and w/o loopback
# DEVNOTE: Implementation only includes necessary functions - expand later


# Doubly linked list
class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.handle = None

    def add(self, data):
        if self.head and self.tail:
            # Two or more nodes - expand the list
            self.tail.next = Node(data, self.tail, None)
            self.tail = self.tail.next
        elif self.head and not self.tail:
            # One node - add tail
            self.tail = Node(data, self.head, None)
            self.head.next = self.tail
        elif not self.head:
            # No nodes - add the first node
            self.head = Node(data, None, None)
            self.handle = self.head

    def move_left(self):
        if self.handle.prev:
            self.handle = self.handle.prev

    def move_right(self):
        if self.handle.next:
            self.handle = self.handle.next

    def peek_left(self):
        if self.handle.prev:
            return self.handle.prev.data
        else:
            return None

    def peek_right(self):
        if self.handle.next:
            return self.handle.next.data
        else:
            return None

    def look(self):
        return self.handle.data


# Doubly linked list with looparound
class LoopList(DLList):
    def __init__(self):
        super().__init__()

    def add(self, data):
        if self.head and self.tail:
            # Two or more nodes - expand the loop
            self.tail.next = Node(data, self.tail, self.head)
            self.tail = self.tail.next
            self.head.prev = self.tail
        elif self.head and not self.tail:
            # One node - add one and establish loop
            self.tail = Node(data, self.head, self.head)
            self.head.prev = self.tail
            self.head.next = self.tail
        elif not self.head:
            # No nodes - add the first node
            self.head = Node(data, None, None)
            self.handle = self.head


# Shared node class
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
