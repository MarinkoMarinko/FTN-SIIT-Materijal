from collections import deque

class TreeNode():
    def __init__(self, val, parent = None):
        self._val = val
        self._parent = parent
        self._children = []

class Tree():
    def __init__(self):
        self._root = None

    def __len__(self):
        if self._root is None:
            return 0
        return self._count_nodes(self._root)
    
    def _count_nodes(self, node):
        count = 1

        for child in node._children:
            count += self._count_nodes(child)

        return count
    
    def is_empty(self):
        return len(self) == 0
    
    def add_root(self, val):
        if self._root is not None:
            raise Exception("Root already exists!")
        
        self._root = TreeNode(val)
        return self._root
    
    def add_child(self, parent, val):
        if parent is None:
            raise Exception("Parent does not exist!")
        
        new_node = TreeNode(val, parent)
        parent._children.append(new_node)
        return new_node
    
    def root(self):
        return self._root
    
    def parent(self, node):
        return node._parent
    
    def num_children(self, node):
        return len(node._children)

    def is_leaf(self, node):
        return self.num_children(node) == 0

    def is_root(self, node):
        return node == self._root

    def replace(self, old, new):
        new._parent = old._parent
        new._children = old._children

        for child in new._children:
            child._parent = new

        if old == self._root:
            self._root = new
        else:
            parent = old._parent
            for i in range(len(parent._children)):
                if parent._children[i] == old:
                    parent._children[i] = new
                    break

        old._parent = None
        old._children = []    

    def depth(self, node):
        if self._root == node:
            return 0
        return 1 + self.depth(node._parent)
    
    def height(self):
        if self._root is None:
            return 0
        return self._height(self._root)
    
    def _height(self, node):
        if self.is_leaf(node):
            return 0
        
        max_height = 0

        for child in node._children:
            child_height = self._height(child)

            if child_height > max_height:
                max_height = child_height

        return 1 + max_height
    
    def preorder(self):
        if self.is_empty():
            return "Tree is empty!"
        self._preorder(self._root)
        print()

    def _preorder(self, node):
        print(node._val, end = " ")

        for child in node._children:
            self._preorder(child)

    def postorder(self):
        if self.is_empty():
            return "Tree is empty!"
        self._postorder(self._root)
        print()


    def _postorder(self, node):
        for child in node._children:
            self._postorder(child)

        print(node._val, end = " ")

    def breadth_first(self):
        if self.is_empty():
            return "Tree is empty!"
        queue = deque([self._root])
        while len(queue) > 0:
            current = queue.popleft()
            print(current._val, end = " ")
            for child in current._children:
                queue.append(child)
        print()

if __name__ == "__main__":
    t = Tree()

    a = t.add_root("A")

    b = t.add_child(a, "B")
    c = t.add_child(a, "C")
    d = t.add_child(a, "D")

    e = t.add_child(b, "E")
    f = t.add_child(b, "F")

    g = t.add_child(d, "G")

    print("Preorder:")
    t.preorder()          # A B E F C D G

    print("Postorder:")
    t.postorder()         # E F B C G D A

    print("Breadth-first:")
    t.breadth_first()     # A B C D E F G

    print("Root:")
    print(t.root()._val)  # A

    print("Parent of E:")
    print(t.parent(e)._val)  # B

    print("Children of A:")
    for child in a._children:
        print(child._val, end=" ")
    print()  # B C D

    print("Number of children of A:")
    print(t.num_children(a))  # 3

    print("Is E leaf?")
    print(t.is_leaf(e))  # True

    print("Is B leaf?")
    print(t.is_leaf(b))  # False

    print("Is A root?")
    print(t.is_root(a))  # True

    print("Is B root?")
    print(t.is_root(b))  # False

    print("Depth of A:")
    print(t.depth(a))  # 0

    print("Depth of G:")
    print(t.depth(g))  # 2

    print("Height:")
    print(t.height())  # 2

    print("Length:")
    print(len(t))  # 7