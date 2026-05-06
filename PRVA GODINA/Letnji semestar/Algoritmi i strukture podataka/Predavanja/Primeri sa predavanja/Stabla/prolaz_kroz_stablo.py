# Depth - first VS breadth - first

from collections import deque

class Node():
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

def depth_first(root):
    if root is None:
        return None
    stack = [ root ]
    values = []
    while stack:
        node = stack.pop()
        values.append(node._val)
        if node._right is not None:
            stack.append(node._right)
        if node._left is not None:
            stack.append(node._left)
    return values


def breadth_first(root):
    if root is None:
        return None
    queue = deque([ root ])
    values = []
    while queue:
        node = queue.popleft()
        values.append(node._val)
        if node._left is not None:
            queue.append(node._left)
        if node._right is not None:
            queue.append(node._right)
    return values
if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a._left = b
    a._right = c
    b._left = d
    b._right = e
    c._right = f
    
#       a
#      / \
#     b  c
#    / \  \
#   d  e  f

    print(f"Depth - first search:   {depth_first(a)}")
    print(f"Breadth - first search: {breadth_first(a)}")
