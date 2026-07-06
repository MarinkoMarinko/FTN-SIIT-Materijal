class Node():
    def __init__(self, val, prev = None, next = None):
        self._prev = prev
        self._val = val
        self._next = next

class DoublyLinkedList():
    def __init__(self):
        self._head = self._tail = None

    def __len__(self):
        if self._head is None:
            return 0
        
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current._next
        return count
    
    def is_empty(self):
        return len(self) == 0
    
    def add_first(self, val):
        new_node = Node(val)

        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._head._prev = new_node
            new_node._next = self._head
            self._head = new_node
        
    def add_last(self, val):
        new_node = Node(val)

        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail._next = new_node
            new_node._prev = self._tail
            self._tail = new_node
    
    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty!")
        
        if self._head == self._tail:
            self._head = self._tail = None
        
        else:
            next_elem = self._head._next
            self._head._next = None
            next_elem._prev = None
            self._head = next_elem
    
    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty!")
        
        if self._head == self._tail:
            self._head = self._tail = None

        else:
            before_last = self._tail._prev
            self._tail = before_last
            self._tail._next = None

    def add_at(self, index, val):
        if index < 0 or index >= len(self):
            raise Exception("Index out of range!")

        if index == 0:
            self.add_first(val)
        elif index == len(self) - 1:
            self.add_last(val)
        else:
            counter = 1
            current = self._head._next
            while counter < index:
                current = current._next
                counter += 1
            new_elem = Node(val, current._prev, current)
            current._prev._next = new_elem
            current._prev = new_elem

    def remove_at(self, index):
        if index < 0 or index >= len(self):
            raise Exception("Index out of range!")

        if index == 0:
            self.remove_first()
        elif index == len(self) - 1:
            self.remove_last()
        else:
            counter = 1
            current = self._head._next
            while counter < index:
                current = current._next
                counter += 1
            prev_node = current._prev
            next_node = current._next
            current._prev = current._next = None
            prev_node._next = next_node
            next_node._prev = prev_node

    def __str__(self):
        result = []
        current = self._head
        while current is not None:
            result.append(str(current._val))
            current = current._next
        return str(result)
    
if __name__ == "__main__":
    try:
        ls = DoublyLinkedList()
        ls.add_first(1)
        ls.add_first(2)
        ls.add_last(3)
        print(ls)
        ls.remove_first()
        print(ls)
        ls.remove_last()
        print(ls)
        ls.add_first(5)
        ls.add_first(10)
        ls.add_first(15)
        print(ls)
        ls.remove_at(1)
        print(ls)
        ls.add_at(1, 1000)
        print(ls)
    except Exception as e:
        print(e)