from collections import deque

class Node:
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._val)


class Tree:
    def __init__(self):
        self._root = None

    def is_empty(self):                 # O(1)
        return self._root is None

    def nodes(self):                    # O(n)
        if self._root is None:
            return

        queue = deque([self._root])

        while queue:
            current = queue.popleft()
            yield current

            if current._left is not None:
                queue.append(current._left)

            if current._right is not None:
                queue.append(current._right)

    def root(self):                     # O(1)
        return self._root

    def children(self, node):           # O(1)
        result = []

        if node._left is not None:
            result.append(node._left)

        if node._right is not None:
            result.append(node._right)

        return result

    def num_children(self, node):       # O(1)
        count = 0

        if node._left is not None:
            count += 1

        if node._right is not None:
            count += 1

        return count

    def is_root(self, node):            # O(1)
        return node == self._root

    def is_leaf(self, node):            # O(1)
        return self.num_children(node) == 0

    def parent(self, node):             # O(n)
        if self._root is None:
            return None

        if node == self._root:
            return None

        for current in self.nodes():
            if current._left == node or current._right == node:
                return current

        return None

    def __len__(self):                  # O(n)
        count = 0

        for node in self.nodes():
            count += 1

        return count

    def add_root(self, val):            # O(1)
        if self._root is not None:
            raise Exception("Stablo već ima koren.")

        self._root = Node(val)
        return self._root

    def add_left(self, node, val):      # O(1)
        if node._left is not None:
            raise Exception("Levo dete već postoji.")

        node._left = Node(val)
        return node._left

    def add_right(self, node, val):     # O(1)
        if node._right is not None:
            raise Exception("Desno dete već postoji.")

        node._right = Node(val)
        return node._right