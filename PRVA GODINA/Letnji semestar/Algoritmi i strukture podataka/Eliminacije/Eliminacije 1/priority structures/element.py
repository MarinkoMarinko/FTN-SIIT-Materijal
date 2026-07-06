class Element():
    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __str__(self):
        return f"({self._key}, {self._val})"