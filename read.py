#!/usr/bin/python
import csv
import sys

def print_indented(s, level):
    for line in s.split('\n'):
        print '\t' * (level - 1) + line

def level(n):
    items = n['Task ID'].split('.')
    return len(items)

def print_row(n):
    lvl = level(n)
    if lvl == 0:
        return
        
    fmts = {'Project': "%(Task)s:", 'Action': "- %(Task)s"}
    fmt = fmts[n['Type']]
    
    print_indented(fmt % n, lvl)
    if n['Notes']:
        print_indented(n['Notes'], lvl + 1)

def handle(filename):
    with open(filename) as f:
        for row in csv.DictReader(f):
            print_row(row)

def main():
    if len(sys.argv) != 2:
        print "Usage: %s filename" % sys.argv[0]
        sys.exit(1)

    handle(sys.argv[1])


if __name__ == '__main__':
    main()