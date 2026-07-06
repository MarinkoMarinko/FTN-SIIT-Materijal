from element import Element

class MaxHeap():
    def __init__(self):
        self._elements = []

    def is_empty(self):
        return len(self._elements) == 0
    
    def max(self):
        if self.is_empty():
            raise Exception("Max heap is empty!")
        return self._elements[0]
    
    def _left(self, index):
        return 2 * index + 1
    
    def _has_left(self, index):
        return self._left(index) < len(self._elements)
    
    def _right(self, index):
        return 2 * index + 2
    
    def _has_right(self, index):
        return self._right(index) < len(self._elements)
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _upheap(self, index):
        if index == 0:
            return
        
        parent_index = self._parent(index)

        if self._elements[index]._key > self._elements[parent_index]._key:
            self._elements[index], self._elements[parent_index] = self._elements[parent_index], self._elements[index]
            self._upheap(parent_index)

    def add(self, key, val):
        new_elem = Element(key, val)
        self._elements.append(new_elem)
        self._upheap(len(self._elements) - 1)

    def _downheap(self, index):
        if self._has_left(index):
            max_index = self._left(index)
            if self._has_right(index):
                right_index = self._right(index)
                if self._elements[right_index]._key > self._elements[max_index]._key:
                    max_index = right_index
                
            if self._elements[max_index]._key > self._elements[index]._key:
                self._elements[max_index], self._elements[index] = self._elements[index], self._elements[max_index]
                self._downheap(max_index)

    def remove_max(self):
        if self.is_empty():
            raise Exception("Max heap is empty!")
        self._elements[0], self._elements[len(self._elements) - 1] = self._elements[len(self._elements) - 1], self._elements[0]
        self._elements.pop()
        self._downheap(0)

    def __str__(self):
        return ", ".join(str(elem) for elem in self._elements)
    

if __name__ == "__main__":
    h = MaxHeap()
    h.add(1, 'A')
    h.add(2, 'B')
    h.add(3, 'C')
    print(h)
    h.remove_max()
    print(h)
    print(h.max())

