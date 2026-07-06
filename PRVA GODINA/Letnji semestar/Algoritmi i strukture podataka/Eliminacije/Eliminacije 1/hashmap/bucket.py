from element import Element


class BucketHash():
    def __init__(self, size):
        self._size = size
        self._fields = [[] for _ in range(self._size)]
        print(self._fields)
    
    def hash(self, key):
        return key % self._size
    
    def __contains__(self, key):
        index = self.hash(key)

        for element in self._fields[index]:
            if element._key == key:
                return True

        return False
    
    def __getitem__(self, key):
        index = self.hash(key)
        if key in self:
            for element in self._fields[index]:
                if element._key == key:
                    return element
        else:
            return None
    
    def __setitem__(self, key, val):
        index = self.hash(key)
        found = self[key]
        if found is None:
            self._fields[index].append(Element(key, val))
        else:
            found._val = val

    def __delitem__(self, key):
        index = self.hash(key)
        found = self[key]
        if found is None:
            raise Exception("Element with given key does not exist")
        else:
            self._fields[index].remove(found)
    
    def __iter__(self):
        for field in self._fields:
            for element in field:
                yield element._key
    
    def keys(self):
        result = []

        for key in self:
            result.append(key)

        return result
    
    def values(self):
        result = []

        for key in self:
            result.append(self[key]._val)
        
        return result
    
    def items(self):
        result = []

        for key in self:
            result.append(self[key])
        
        return result
    
    def __str__(self):
        result = []

        for i in range(self._size):
            field = self._fields[i]
            field_data = []
            for element in field:
                field_data.append(str(element))
            result.append(f"{i}: {field_data}")

        return "\n".join(result)
    
if __name__ == "__main__":
    b = BucketHash(5)

    b[7] = "A"
    b[12] = "B"
    b[3] = "C"
    b[8] = "D"
    b[17] = "E"

    print("Cela mapa:")
    print(b)

    print("Element sa ključem 12:")
    print(b[12])

    print("Da li postoji ključ 7?")
    print(7 in b)

    print("Da li postoji ključ 99?")
    print(99 in b)

    
    print("Menjam vrednost za ključ 12")
    b[12] = "Nova vrednost"
    print(b)

    print("Brišem ključ 7")
    del b[7]
    print(b)
