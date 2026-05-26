from element import Element

class MinHeap():
    def __init__(self):
        self._elements = []
    
    def is_empty(self):             # O(1)
        return len(self._elements) == 0
    
    def _parent(self, index):        # O(1)
        return (index - 1) // 2
    
    def _left(self, index):          # O(1)
        return index * 2 + 1
    
    def _right(self, index):         # O(1)
        return index * 2 + 2
    
    def _has_left(self, index):     # O(1)
        return self._left(index) < len(self._elements)

    def _has_right(self, index):    # O(1)
        return self._right(index) < len(self._elements)
    
    def min(self):                  # O(1)
        if self.is_empty():
            raise Exception("Heap je prazan.")
        else:
            return self._elements[0]
    
    def upheap(self, index):         # O(logn)
        parent_index = self._parent(index)       

        if index > 0 and self._elements[index]._key < self._elements[parent_index]._key:
            self._elements[index]._key, self._elements[parent_index] = self._elements[parent_index]._key, self._elements[index]._key
            self.upheap(parent_index)
    
    def add(self, key, value):      # O(logn)
        new_elem = Element(key, value)
        self._elements.append(new_elem)
        self.upheap(len(self._elements) - 1)

    def downheap(self, index):     # O(logn)
        if self._has_left():
            next_index = self._left(index)
            if self._has_right() and self._elements[self._right(index)]._key < self._elements[next_index]._key:
                next_index = self._right(index)
            
            if self._elements[next_index]._key < self._elements[index]._key:
                self._elements[next_index]._key, self._elements[index]._key = self._elements[index]._key ,self._elements[next_index]._key
                self.downheap(next_index)

    def remove_min(self):     # O(logn)
        if self.is_empty():
            raise Exception("Heap je prazan.")
        self._elements[0], self._elements[-1] = self._elements[-1], self._elements[0]
        self._elements.pop()
        if not self.is_empty():
            self.downheap(0)

    def build_min_heap(self, items):    # O(n)
        self._elements = []

        for key, value in items:
            self._elements.append(Element(key, value))
        
        for i in range((len(self._elements) - 2) // 2, -1, -1):
            self.downheap(i)

    def __str__(self):              # O(n)
        return "[ " + ", ".join(str(element) for element in self._elements) + " ]"
    


# MinHeap - nepotpuno binarno stablo, gde kljucevi (kada se krecemo od root-a na dole) rastu, tj. root ima najmanji kljuc, a leafovi najvece kljuceve. 

# Levo dete se dobija formulom: 2 * index_roditelja + 1
# Desno dete se dobija formulom: 2 * index_roditelja + 2

# Upheap postupak - cvor se poredi sa roditeljom (po kljucu), ako je manji od roditelja, menjaju mesta. Postupak se ponavlja dok cvor ne dodje na pravo mesto

# Add - cvor se dodaje uvek na kraj liste, pa se poziva upheap postupak koliko je potrebno.

# Upheap postupak je O(logn) jer ce, u najgorem slucaju, cvor preci celu visinu stabla, a ona je logn, gde je n broj cvorova. Takodje i Add je O(logn)

# Downheap postupak - levo i desno dete se porede po kljucevima, kako bi se naslo najmanje. Nakon toga, poredi se roditelj i najmanje dete, ako je roditelj veci od deteta (po kljucu), onda se menjaju. Postupak se ponavlja dok cvor ne dodje na pravo mesto. 

# Remove min - Najmanji clan je root stabla, pa se menja sa poslednjim elementom liste. Nakon zamene, poslednji element liste (root) se brise, a nad novim root-om stabla se ponavlja postupak downheap dok on ne dodje na pravo mesto.

# Downheap postupak je O(logn) jer ce se, u najgorem slucaju, cvor preci celu visinu stabla, a ona je logn, gde je n broj cvorova. Takodje i Remove min je O(logn)

# Heapify ili build_min_heap je postupak pretvaranja random liste u heap. Radi tako sto se nalazi poslednji roditelj u listi (on je na indeksu (n-2) // 2). Krece se iteracija od poslednjeg clana petlje do (n-2)//2 - og clana petlje i u svakoj iteraciji se poziva downheap postupak.