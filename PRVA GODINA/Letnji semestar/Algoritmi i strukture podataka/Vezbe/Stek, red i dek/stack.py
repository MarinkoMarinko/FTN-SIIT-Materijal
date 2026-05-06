class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self._values = []
    def top(self):
        if len(self._values) == 0:
            raise EmptyStackError("Stack is empty!")
        return self._values[-1]
    def __len__(self):
        return len(self._values)
    def push(self, num):
        self._values.append(num)
    def pop(self):
        if len(self._values) == 0:
            raise EmptyStackError("Stack is already empty!")
        return self._values.pop()
    def __str__(self):
        return str(self._values)
    
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack)
    stack.pop()
    print(stack.top())
    stack.pop()
    stack.pop()