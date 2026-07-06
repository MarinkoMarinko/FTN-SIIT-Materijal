from element import Element

class Unsorted():
    def __init__(self):
        self._elements = []

    def is_empty(self):
        return len(self._elements) == 0
    
    def add(self, key, val):
        self._elements.append(Element(key, val))

    def min(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        
        min_elem = self._elements[0]
        for elem in self._elements:
            if elem._key < min_elem._key:
                min_elem = elem
        return min_elem
    
    def remove_min(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        
        min_elem = self.min()
        self._elements.remove(min_elem)

    def __str__(self):
        result = []

        for elem in self._elements:
            result.append(str(elem))

        return ", ".join(result)
        

if __name__ == "__main__":
    try:
        u = Unsorted()
        u.add(3, 'A')
        u.add(2, 'B')
        u.add(1, 'C')
        print(u)
        print(u.min())
        u.remove_min()
        print(u)
    except Exception as e:
        print(e)