# -*- coding: utf-8 -*-

'''
stack = [10,1]
while True:
    x = raw_input('введите значение :')
    def push(x,stack):
        if stack[1]==stack[0]:
            print 'so'
            return                        # стек
        stack[1]+=1
        stack.insert(stack[1],x)
        print stack[2:]
    push(x,stack)
'''

'''
def pop (stack):
    if stack[1]==1:
        print 'empty'
        return None
    result = stack[stack[1]]     # pop не доделан
    stack[1]-=1
    return stack[stack[1]+1]
'''


class Tree(object):
    def __init__(self, stack):
        self.stack = stack
        self.root = stack[-1]
        self.nodes = []
        self.add_node(Node(stack.pop()))

    def __str__(self):
        return str(self.nodes)

    def add_node(self, node):
        self.nodes.append(node)


class Node(object):
    def __init__(self, key):
        self.key = key
        self.l_child = self.r_child = None


if __name__ == '__main__':
    stack = [1, 2, 5, 3, 58, 6, 56]
    tree = Tree(stack)
    print tree