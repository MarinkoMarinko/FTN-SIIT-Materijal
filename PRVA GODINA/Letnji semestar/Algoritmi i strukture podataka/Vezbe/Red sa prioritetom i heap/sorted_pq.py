from element import Element

class SortedPQ():
    def __init__(self):
        self._elements = []
    
    def is_empty(self):             # O(1)
        return len(self._elements) == 0
    
    def add(self, key, val):        # O(n)
        element = Element(key, val)
        index = 0
        while index < len(self._elements) and self._elements[index]._key < element._key:
            index += 1
        self._elements.insert(index, element)

    def min(self):                  # O(1)         
        if self.is_empty():
            raise Exception("Red je prazan.")
        else:
            return self._elements[0]
        
    def remove_min(self):           # O(n) (moze biti O(1) ako se koristi deque)
        if self.is_empty():
            raise Exception("Red je prazan.")
        else:
            del self._elements[0]
    
    def __str__(self):              # O(n)
        return "[ " + ", ".join(str(element) for element in self._elements) + " ]"
    

if __name__ == "__main__":
    try:
        sorted_pq = SortedPQ()
        sorted_pq.add(1, "a")
        sorted_pq.add(0, "b")
        sorted_pq.add(2, "c")
        print(sorted_pq)
        print(sorted_pq.min())
        sorted_pq.remove_min()
        print(sorted_pq)

    except Exception as e:
        print(e)

# Dakle, kod sortedPQ, element sa najprioritetnijim kljucem se nalazi uvek na pocetku reda, prilikom dodavanja se odmah poredi sa ostalim kljucevima i dodaje na odredjeno mesto.