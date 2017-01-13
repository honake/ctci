""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

MIN = 0
MAX = 10**4


def check_subtree(root, min_val, max_val):
    if root is None:
        return True
    elif root.data > min_val and root.data < max_val:
        return check_subtree(root.left, min_val, root.data) and check_subtree(root.right, root.data, max_val)
    else:
        return False


def check_binary_search_tree_(root):
    return check_subtree(root, MIN, MAX)
