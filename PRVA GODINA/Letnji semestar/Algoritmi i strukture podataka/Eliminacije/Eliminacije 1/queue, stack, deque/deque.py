class Deque():
    def __init__(self):
        self._values = []

    def is_empty(self):
        return len(self._values) == 0

    def add_first(self, val):
        self._values.insert(0, val)

    def add_last(self, val):
        self._values.append(val)

    def remove_first(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._values.pop(0)
    
    def remove_last(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._values.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._values[0]
    
    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty!")
        return self._values[-1]
    
    def __str__(self):
        return "front -> " + " ".join(str(val) for val in self._values) + " <- rear"
    
if __name__ == "__main__":
    try:
        d = Deque()
        d.add_first(1)
        d.add_first(2)
        d.add_last(3)
        print(d)
        d.remove_first()
        print(d)
        d.remove_last()
        print(d)
    except Exception as e:
        print(e)