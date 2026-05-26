from element import Element

class UnsortedPQ():
    def __init__(self):
        self._elements = []

    def is_empty(self):             # O(1)
        return len(self._elements) == 0
    
    def add(self, key, val):                # O(1), a ako se popuni niz, duzina niza se udvostruci pa bude O(n) (redja situacija)
        self._elements.append(Element(key, val))

    def _min_index(self):           # O(n) - pomocna funkcija
        if self.is_empty():
            raise Exception("Red je prazan.")
        else:
            min_index = 0
            for i in range(1, len(self._elements)):
                if self._elements[i]._key < self._elements[min_index]._key:
                    min_index = i
            return min_index

    def min(self):                  # O(n)
        min_index = self._min_index()
        return self._elements[min_index]
    
    def remove_min(self):           # O(n)
        min_index = self._min_index()
        del self._elements[min_index]
    
    def __str__(self):              # O(n)
        return "[ " + ", ".join(str(element) for element in self._elements) + " ]"
    

if __name__ == "__main__":
    try:
        unsorted_pq = UnsortedPQ()
        unsorted_pq.add(1, "a")
        unsorted_pq.add(3, "b")
        unsorted_pq.add(0, "d")
        unsorted_pq.add(2, "c")
        print(unsorted_pq)
        print(unsorted_pq.min())
        unsorted_pq.remove_min()
        print(unsorted_pq)
    except Exception as e:
        print(e)

# Dakle, kod unsortedPQ, element se uvek dodaje na kraj, najprioritetniji element se ne nalazi nuzno na prvom mestu, pa se mora naci tokom izvrsavanja remove_min() i min().