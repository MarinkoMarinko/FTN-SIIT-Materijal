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
    input = "732*-"
    stack = Stack()
    for s in input:
        if s not in ["+", "-", "*", "/"]:
            stack.push(s)
        else:
            second_num = stack.pop()
            first_num = stack.pop()
            result = f"{first_num}{s}{second_num}"
            stack.push(str(eval(result)))
    print(f"Result: {stack.top()}")