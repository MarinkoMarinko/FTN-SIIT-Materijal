class Stack:
    def __init__(self):
        self._values = []

    def is_empty(self):
        return len(self._values) == 0
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self._values[-1]
    
    def push(self, val):
        self._values.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        self._values.pop()
    
    def __str__(self):
        return " ".join(str(val) for val in self._values)
    

if __name__ == "__main__":
    try:
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        print(s)
        s.pop()
        print(s.top())
        print(s)
    except Exception as e:
        print(e)