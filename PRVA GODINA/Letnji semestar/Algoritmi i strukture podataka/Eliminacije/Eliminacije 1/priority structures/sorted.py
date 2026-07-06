from element import Element


class Sorted():
    def __init__(self):
        self._elements = []

    def is_empty(self):
        return len(self._elements) == 0
    
    def min(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        return self._elements[0]
    
    def remove_min(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        self._elements.pop(0)

    def add(self, key, val):
        new_elem = Element(key, val)
        index = 0
        for i in range(len(self._elements)):
            if new_elem._key > self._elements[i]._key:
                index += 1
        self._elements.insert(index, new_elem)

    def __str__(self):
        result = []

        for elem in self._elements:
            result.append(str(elem))
        
        return ", ".join(result)

if __name__ == "__main__":
    try:
        s = Sorted()
        s.add(3, 'A')
        s.add(5, 'B')
        s.add(2, 'C')
        s.add(7, 'D')
        print(s)
        print(s.min())
        s.remove_min()
        print(s)
    except Exception as e:
        print(e)