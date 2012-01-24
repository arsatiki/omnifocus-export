import csv
import sys
from collections import defaultdict

class Node(object):
    def add(self, child):
        self.children.append(child)

    def __str__(self):
        children = '\n'.join(map(str, self.children))
        return self.level * '  ' + self['Task'] + children

class Root(Node):
    level = 0
    def __init__(self):
        self.children = []
    
    def add(self, child):
        self.children.append(child)
    
    def __getitem__(self, key):
        return ''

class Tree(Node):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.level = len(self['Task ID'].split('.'))

    def __getitem__(self, key):
        return self.data[key]

def make_tree(seq):
    stack = [Root()]
    
    for item in map(Tree, seq):
        while item.level <= stack[-1].level:
            stack.pop()
        stack[-1].add(item)
    
    return stack[0]

def read(filename):
    with open(filename) as f:
        return list(csv.DictReader(f))


def main():
    pass

if __name__ == '__main__':
    main()