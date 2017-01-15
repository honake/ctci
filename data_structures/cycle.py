"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    node = head
    memo = set()
    while True:
        if node == None:
            return False
        else:
            if node in memo:
                return True
            else:
                memo.add(node)
                node = node.next
