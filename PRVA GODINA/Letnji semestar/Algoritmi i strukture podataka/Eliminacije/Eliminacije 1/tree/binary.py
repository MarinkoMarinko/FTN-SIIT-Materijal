from collections import deque

class Node():
    def __init__(self, val, parent = None):
        self._val = val
        self._parent = parent
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._val)
    
class BinaryTree():
    def __init__(self):
        self._root = None
    
    def is_empty(self):
        return self._root is None
    
    def add_root(self, node):
        if self._root is not None:
            raise Exception("Root already exists!")
        self._root = node
        return self._root

    def add_child(self, parent, node):
        if parent._left is None:
            parent._left = node
            node._parent = parent
            return parent._left
        elif parent._right is None:
            parent._right = node
            node._parent = parent
            return parent._right
        else:
            raise Exception("Parent already has both childs.")
    
    def is_root(self, node):
        return self._root == node

    def is_leaf(self, node):
        return node._left == None and node._right == None
    
    def depth(self, node):
        if self.is_root(node):
            return 0
        return 1 + self.depth(node._parent)
    
    def height(self):
        if self.is_empty():
            return 0
        return self._height(self._root)
    
    def _height(self, node):
        if self.is_leaf(node):
            return 0
        
        left = float("-inf")
        right = float("-inf")

        if node._left is not None:
            left = self._height(node._left)
        if node._right is not None:
            right = self._height(node._right)
        
        return 1 + max(left, right)
    
    def preorder(self):
        if self._root is None:
            return []
        self._preorder(self._root)
        print()

    
    def _preorder(self, node):
        print(node, end = " ")

        if self.is_leaf(node):
            return
        
        if node._left is not None:
            self._preorder(node._left)
        
        if node._right is not None:
            self._preorder(node._right)
        
    def postorder(self):
        if self._root is None:
            return []
        self._postorder(self._root)
        print()

    def _postorder(self, node):        
        if node._left is not None:
            self._postorder(node._left)

        if node._right is not None:
            self._postorder(node._right)

        print(node, end = " ")
        return
    
    def breadth_first(self):
        if self._root is None:
            return []
        
        deq = deque([self._root])
        while len(deq) > 0:
            node = deq.popleft()
            print(node, end = " ")
            if node._left is not None:
                deq.append(node._left)
            if node._right is not None:
                deq.append(node._right)   
        print()

if __name__ == "__main__":
    try:
        t = BinaryTree()

        root = Node(1)
        n1 = Node(2)
        n2 = Node(3)
        n3 = Node(4)
        n4 = Node(5)

        t.add_root(root)
        t.add_child(root, n1)
        t.add_child(root, n2)
        t.add_child(n1, n3)
        t.add_child(n1, n4)

        print(t.height())
        print(t.depth(n3))
        t.preorder()
        t.postorder()
        t.breadth_first()

    except Exception as e:
        print(e)