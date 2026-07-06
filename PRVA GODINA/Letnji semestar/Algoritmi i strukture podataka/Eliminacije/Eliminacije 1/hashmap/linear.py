from element import Element

class HashMapLinear:
    _AVAILABLE = object()

    def __init__(self, capacity = 10):
        self._capacity = capacity
        self._table = [None] * capacity
        self._size = 0

    def _hash(self, key):
        return hash(key) % self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _find_slot(self, key):
        index = self._hash(key)
        first_available = None

        for i in range(self._capacity):
            current_index = (index + i) % self._capacity
            current = self._table[current_index]

            if current is None:
                if first_available is None:
                    return False, current_index
                else:
                    return False, first_available

            elif current is HashMapLinear._AVAILABLE:
                if first_available is None:
                    first_available = current_index

            elif current._key == key:
                return True, current_index

        if first_available is not None:
            return False, first_available

        raise Exception("Hash map is full!")

    def __setitem__(self, key, value):
        found, index = self._find_slot(key)

        if found:
            self._table[index]._value = value
        else:
            self._table[index] = Element(key, value)
            self._size += 1

    def __getitem__(self, key):
        found, index = self._find_slot(key)

        if not found:
            raise KeyError("Key does not exist!")

        return self._table[index]._value

    def __delitem__(self, key):
        found, index = self._find_slot(key)

        if not found:
            raise KeyError("Key does not exist!")

        self._table[index] = HashMapLinear._AVAILABLE
        self._size -= 1

    def __contains__(self, key):
        found, index = self._find_slot(key)
        return found

    def __iter__(self):
        for entry in self._table:
            if entry is not None and entry is not HashMapLinear._AVAILABLE:
                yield entry._key

    def keys(self):
        result = []

        for key in self:
            result.append(key)

        return result

    def values(self):
        result = []

        for entry in self._table:
            if entry is not None and entry is not HashMapLinear._AVAILABLE:
                result.append(entry._value)

        return result

    def items(self):
        result = []

        for entry in self._table:
            if entry is not None and entry is not HashMapLinear._AVAILABLE:
                result.append((entry._key, entry._value))

        return result

    def __str__(self):
        result = []

        for i in range(self._capacity):
            entry = self._table[i]

            if entry is None:
                result.append(f"{i}: None")
            elif entry is HashMapLinear._AVAILABLE:
                result.append(f"{i}: X")
            else:
                result.append(f"{i}: {entry}")

        return "\n".join(result)