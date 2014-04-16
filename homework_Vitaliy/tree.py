#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


class Node(object):
    lchild = None
    rchild = None

    def __init__(self, key):
        self.key = key

    def __str__(self):
        """
Самая простая реализация отображения узла дерева
"""
        return '\nkey: %s, lchild: %s, rchild: %s' % (self.key, self.lchild, self.rchild)


class Tree(object):
    def __init__(self, source):
        self.data = source
        self.root = Node(self.data.pop(0))
        self.nodes = []

    def __str__(self):
        return str(self.root)

    def build(self):
        for value in self.data:
            self.check(self.root, Node(value))

    def check(self, root, node):
        if root.key <= node.key:
            if root.rchild is None:
                root.rchild = node
            else:
                self.check(root.rchild, node)
        else:
            if root.lchild is None:
                root.lchild = node
            else:
                self.check(root.lchild, node)


if __name__ == '__main__':
    data = [33, 2, 56, 67, 36, 3, 52, 1, 65, 45, 4]

    tree = Tree(data)
    tree.build()

    print tree
