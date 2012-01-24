import csv
import sys
from collections import defaultdict

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        path = self['Task ID']
        self.level = len(path.split('.')) if path else 0

    def add(self, child):
        self.children.append(child)

    def __getitem__(self, key):
        return self.data.get(key, '')

    def __str__(self):
        children = '\n'.join(map(str, self.children))
        return self.level * '  ' + self['Task'] + children

def make_tree(seq):
    root = Tree({})
    stack = [root]
    
    for item in map(Tree, seq):
        while item.level <= stack[-1].level:
            stack.pop()
        stack[-1].add(item)
    
    return root

def read(filename):
    with open(filename) as f:
        return list(csv.DictReader(f))


def main():
    pass

if __name__ == '__main__':
    main()