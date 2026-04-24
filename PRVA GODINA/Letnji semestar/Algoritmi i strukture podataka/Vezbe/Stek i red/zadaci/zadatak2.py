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


def convert_to_hex(remainder):
    if  9 >= remainder >= 0:
        return remainder
    else:
        letters = ["A", "B", "C", "D", "E", "F"]
        index = remainder - 10
        return letters[index]


if __name__ == "__main__":
    n = 734
    temp = n
    stack = Stack()
    while temp != 0:
        remainder = temp % 16
        stack.push(convert_to_hex(remainder))
        temp = temp // 16
    output = ""
    while len(stack) != 0:
        output += str(stack.pop())
    print(f"Number {n} in hexadecimal notation: {output}")
