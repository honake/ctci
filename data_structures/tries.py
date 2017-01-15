class Node:
    def __init__(self, char):
        self.children = []
        self.wc = 0
        self.char = char

    def add(self, s):
        if len(s) == 0:
            return
        l = len(self.children)
        for i in range(l):
            child = self.children[i]
            if child.char[0] == s[0]:
