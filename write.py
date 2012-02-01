# Type = Project, Action (voinee olla Folderkin)
# sit on Notes

def print_indented(s, level):
    for line in s.split('\n'):
        print '\t' * (level -1) + line

def print_node(n):
    fmts = {'Project': "%(Task)s:", 'Action': "- %(Task)s"}
    fmt = fmts[n['Type']]
    
    print_indented(fmt % n, n.level)
    if n['Notes']:
        print_indented(n['Notes'], n.level + 1)

def print_tree(node):
    if node.level:
        print_node(node)
    for c in node.children:
        print_tree(c)